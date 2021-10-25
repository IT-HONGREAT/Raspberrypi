# 우선적으로 써보는 큰 개요,계획(차후 지속적으로 수정)

1. 라즈베리파이 기본세팅
  - OS, 무게센서 세팅 (완료)
2. 음식이미지 데이터, 음식에 대한 영양성분 데이터 수집 및 정제
  - ~~AIHUB에 업로드한 2TB의 외식 및 한식 데이터를 사용하려 했으나--
  - 모델학습에는 이 보다는 적어도 괜찮기 때문에
  - https://aihub.or.kr/aidata/30747

3. yolo v3(우선 v3로) 모델을 이용, 음식이미지 분류
  - darknet을 이용 라즈베리파이에서 run 시켜보기

4. 라즈베리파이로 음식에 대한 무게 값을 측정 -> 마리아DB 연동
  - 무게에 대한 데이터를 올려야하는데, 지속적인 측정이 이뤄지고, 측정무게에 대한 데이터를 정리 해야하는 것이 관건.
  - 그리고 이미지 분류와의 순서에서 어떻게 플랜을 수정할 것인가?

5. 음식의 무게 + 음식이미지 분류로 어떤 음식인지 선별
  - 두 데이터를 어떤 방향으로 엮을 것인가? 가 관건

6. 해당 음식의 무게에 따른 영양성분 제공
  - 위 과정에서 문제를 보완하면 자연스레 해결 될 것

7. django로 배포
  - https://github.com/IT-HONGREAT/django_food_project 와 이어짐 
  - 개별적으로 웹에 대한 이해 및 이미지 분류 모델을 django로 배포하는 과정을 연구하고 구현해야함.
  - 본 repository 와 이어질 수 도 있는 서비스로 웹 자체의 디자인을 먼저 구상하고 어떤 방식으로 서비스를 할 것인지? 가 관
