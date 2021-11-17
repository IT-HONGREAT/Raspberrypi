import base64
import io
import os
import time
import pandas as pd
import cv2
import numpy as np
from PIL import Image
from flask import Flask, request, render_template
from flask_ngrok import run_with_ngrok

from hx711py.example import make_weight

confthres = 0.3
nmsthres = 0.1
yolo_path = './'
#add food def
input_class = '짬뽕'
input_weight = 600

data = pd.read_csv('food/음식이미지 영양정보 402.csv')
def classifi(input_class, input_weight):
    for i in range(len(data)):
        if data.iloc[i,6] == input_class:
            nutrition = data.iloc[i]
    div = input_weight/nutrition.iloc[12]
    b = f'''입력받은 음식 무게는 {input_weight}g입니다.
        1회 제공량의 약 {round(div, 2)}배 입니다.
        식품명: {nutrition.iloc[6]}
        칼로리: {round(nutrition.iloc[16] * div, 2)} kcal
        탄수화물 {round(nutrition.iloc[23] * div, 2)}g
        단백질 {round(nutrition.iloc[20] * div, 2)}g
        지방 {round(nutrition.iloc[20] * div, 2)}g '''
    return b

def get_labels(labels_path):
    lpath = os.path.sep.join([yolo_path, labels_path])
    LABELS = open(lpath).read().strip().split("\n")
    return LABELS


def get_colors(LABELS):
    np.random.seed(42)
    COLORS = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")
    return COLORS


def get_weights(weights_path):
    weightsPath = os.path.sep.join([yolo_path, weights_path])
    return weightsPath


def get_config(config_path):
    configPath = os.path.sep.join([yolo_path, config_path])
    return configPath


def load_model(configpath, weightspath):
    print("[INFO] loading YOLO from disk...")
    net = cv2.dnn.readNetFromDarknet(configpath, weightspath)
    return net


def image_to_byte_array(image:Image):
    imgByteArr = io.BytesIO()
    image.save(imgByteArr, format='PNG')
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr


def get_predection(image, net, LABELS, COLORS):
    (H, W) = image.shape[:2]

    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
                                 swapRB=True, crop=False)
    net.setInput(blob)
    start = time.time()
    layerOutputs = net.forward(ln)
    print(layerOutputs)
    end = time.time()

    print("[INFO] YOLO took {:.6f} seconds".format(end - start))

    boxes = []
    confidences = []
    classIDs = []

    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]

            if confidence > confthres:
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")

                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))

                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)

    idxs = cv2.dnn.NMSBoxes(boxes, confidences, confthres, nmsthres)

    if len(idxs) > 0:
        for i in idxs.flatten():
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])

            color = [int(c) for c in COLORS[classIDs[i]]]
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
            text = "{}: {:.4f}".format(LABELS[classIDs[i]], confidences[i])
            print(boxes)
            print(classIDs)
            cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    return image


labelsPath = "weights/obj_c2.names"
cfgpath = "weights/yolov3_china2.cfg"
wpath = "weights/yolov3_11.09_final.weights"

Lables = get_labels(labelsPath)
CFG = get_config(cfgpath)
Weights = get_weights(wpath)
nets = load_model(CFG, Weights)
Colors = get_colors(Lables)

app = Flask(__name__)
run_with_ngrok(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def main():
    img = request.files["file"].read()
    img = Image.open(io.BytesIO(img))
    npimg = np.array(img)
    image = npimg.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    res = get_predection(image, nets, Lables, Colors)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
    np_img = Image.fromarray(image)
    img_encoded = image_to_byte_array(np_img)
    base64_bytes = base64.b64encode(img_encoded).decode("utf-8")
    nut = classifi(input_class, input_weight)

    return render_template('index.html', user_image=base64_bytes,num2=nut)


# @app.route('/')
# def weight_out():
#     # exec(Path("/home/pi/Downloads/raspberryproject001/versions/Raspberrypi/Firstproject_for_versions/hx711py/example.py").read_text())
#     temp = make_weight()
#     return render_template('index.html')

# start flask app
if __name__ == '__main__':
    app.run()

# host='0.0.0.0', port=3000, debug=True