# <center> :+1: 라즈베리파이 프로젝트의 흐름과 직접 진행하면서 기록한 내용입니다</center>


## 1. 개요 및 팀원역할 :dart:
  
**개요**
* 로드셀HX711(무게센서)로 음식무게측정 → 라즈베리파이의 YOLO모델로 이미지 분류 (음식탐지)→ 음식 Data와 무게 비례 → 칼로리, 단백질, 지방, 탄수화물, 기타 영양소 들을 출력



**팀원역할 및 담당**
- 홍인영(본인) - 라즈베리파이4를 이용 음식 무게 및 정보를 Flask로 출력
- 박ㅇㅇ(팀장) - 기획 및 관리, 이미지 분류모델 사용
- 임ㅇㅇ - 웹프론트엔드(html,css)
- 곽ㅇㅇ - 영양성분 데이터 수집 보조






## 2. 음식이미지 학습 과정 :pushpin:
 **노션에 음식이미지를 학습했던 과정을 기록했습니다**
 
  1. [yolo(다크넷 사용기록)](https://deeply-saturnalia-5c9.notion.site/yolo-948e9fa7376a4725be51f60f6693a1be)
  2. [코랩을 이용한 학습](https://deeply-saturnalia-5c9.notion.site/691a91b2f9844a71a608e14ffe25f79a)
  3. [접시,음식 구분(문제파악)](https://deeply-saturnalia-5c9.notion.site/1f9c5994065745749a9f354636d67be5)
  4. [여러(중국)음식 학습](https://deeply-saturnalia-5c9.notion.site/86921f77a6ec42338751fd1c412d9a47)
    
    
## 3. 라즈베리파이 사용 및 적용과정 :pushpin:
  **노션에 라즈베리파이를 겪은 과정을 기록했습니다**
  
  * [초기원격 접속](https://deeply-saturnalia-5c9.notion.site/PC-b42af89c934d431580515ce392cfdcbd)
  1. [무게센서 연동 및 영점조절](https://deeply-saturnalia-5c9.notion.site/4340635a6af14bedafa46705c0115041)
  2. [이미지 업로드 요청 -> 음식무게측정 -> 결과출력](https://deeply-saturnalia-5c9.notion.site/a93c72a97c8042569db3fd34be03da73)

<details>
<summary>깃허브 상의 코드입니다</summary>
<div markdown="1">       

1. [음식의 무게에 대한 정보추출](https://github.com/IT-HONGREAT/Raspberrypi/blob/6381902976344e83b7f679b9094fb6cd8bd769ff/Firstproject_for_versions/app.py#L20)
2. [무게센서 작동방식 및 음식무게 알고리즘](https://github.com/IT-HONGREAT/Raspberrypi/blob/6381902976344e83b7f679b9094fb6cd8bd769ff/Firstproject_for_versions/hx711py/example.py#L39)

</div>
</details>



## 4. 발표영상 및 결과 :movie_camera:

**이미지를 클릭하시면 4분 미만의 발표영상 링크로 이동합니다**

[![로고](https://user-images.githubusercontent.com/80932397/144426700-16ac06b9-39ea-47cb-9a2d-88dcb4c1f789.png)](https://youtu.be/kKvXxpI597g) 

### 결과
![image](https://user-images.githubusercontent.com/80932397/142378323-7c306e40-fe96-4f0f-b798-80fe49c53df3.png)

