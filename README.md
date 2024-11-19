# 소중한 오픈 소스 활용SW 경진대회 

# 국립한밭대학교 이파이팀

|[김장환](https://github.com/wodeyuzhou)|[신은호](https://github.com/neungho1)|[이유진](https://github.com/runth)|[진경은](https://github.com/JinKyungEun000)|
|:---:|:---:|:---:|:--:|
|<img src="https://github.com/user-attachments/assets/2aa22ddc-f059-43be-b66e-7215e9068d59" width="100px" height="100px"/>|<img src="https://github.com/user-attachments/assets/2aa22ddc-f059-43be-b66e-7215e9068d59" width="100px" height="100px"/>|<img src="https://github.com/user-attachments/assets/2aa22ddc-f059-43be-b66e-7215e9068d59" width="100px" height="100px"/>|<img src="https://github.com/user-attachments/assets/2aa22ddc-f059-43be-b66e-7215e9068d59" width="100px" height="100px"/>|
|팀장 / 웹서버|객체 인식 모델|프론트엔드|데이터셋 구축|

## 웹사이트 주소
- https://evcharge-status.vercel.app (Vercel CI/CD repo: https://github.com/wodeyuzhou/evcharge-status)

## 주제 
- **엣지 디바이스 기반 실시간 전기차 충전소 자리 인식 시스템**
  
## 팀 구성 
- 20192390 김장환 중국어과/인공지능소프트웨어학과
- 20221055 신은호 인공지능소프트웨어학과
- 20221063 이유진 인공지능소프트웨어학과
- 20227005 진경은 인공지능소프트웨어학과

## Project Background
  - ### 개요
    <p>
    <img width="390" alt="image" src="https://github.com/user-attachments/assets/c7db1c89-ddab-45b3-bbbf-d6c46d9ac50f">
    &nbsp;
    <img width="415" alt="image" src="https://github.com/user-attachments/assets/22d64a10-9600-4a05-b58c-9f7f2b3ef896">
    </p>

    엣지 디바이스 환경에서 **자체적으로 객체 인식을 수행**하여 실시간으로 전기차 충전소의 주차 가능 여부와 사용중인 차량의 주차된 시간을 모니터링하고, </br>
    **그 결과를 웹페이지로 전송**하여 사용자들이 실시간 전기차 충전소 자리를 확인할 수 있는 시스템

  - ### 필요성
    기존에 전기차 충전소의 위치 정보를 통합하여 제공하는 플랫폼들이 존재하지만, **정보 연동의 한계로 인해 사용자들이 충전소의 정확한 사용 가능 여부와 상태를** </br>
    **실시간으로 파악하기 어려운 경우**가 있음. 이러한 문제를 해결하기 위해 **엣지 디바이스에서 객체 인식 모델을 구동하여 충전소 주차 자리와 주차 시간을 실시간으로 모니터링**하는 시스템을 제공하고자 함. </br>
    라즈베리파이와 같은 **엣지 디바이스가 현장에서 직접 객체 인식을 수행**함으로써,  신속하고 정확한 전기차 충전소 상태 정보를 제공 가능함. 
    
    또한, 이 시스템은 **기존 CCTV 및 기타 엣지 디바이스와의 통합을 통해 확장 가능**함. </br>
    예를 들어, 공공장소에 이미 설치된 CCTV와 연동하여 주차 자리 상태를 모니터링하거나, 여러 엣지 디바이스를 연계하는 등의 확장성 있는 시스템으로 발전 가능. </br>
    이러한 확장성은 기존 인프라를 활용하여 전기차 충전 인프라의 신뢰성을 높이는 데 기여할 수 있음.
    
## 프로젝트 내용
  - ### 구현 내용 - 웹페이지 및 모바일 환경에서의 충전소 자리 알람 기능 구현
    <p>
    <img width="640" alt="homepage" src="https://github.com/user-attachments/assets/4677bbb8-8ca8-4213-82ca-95e1072242b3">
    &nbsp;
    <img width="165" alt="homepage" src="https://github.com/user-attachments/assets/5975d8ca-6864-423a-8f4c-ba14f7377e1f">
    </p>

  - ### 시스템 구조 - 라즈베리파이 환경에서 실시간 객체 인식 수행
    <img width="850" alt="structure" src="https://github.com/user-attachments/assets/bde9ccac-2da9-446a-8419-c5e7aa28343c">

  - ### 적용 기술 - VisDrone-Dataset을 사용하여 Fine-Tuning
    <img width="853" alt="스크린샷 2024-11-19 21 35 48" src="https://github.com/user-attachments/assets/09c2e4ae-e69b-4501-81f8-507c6b3ae05e">

## References

- ### 개발 필요성 및 목적
    https://www.khan.co.kr/economy/auto/article/202405261450001 </br>
    https://www.hankyung.com/article/202312083584g


- ### Ultralytics YOLOv8
    ![image](https://github.com/user-attachments/assets/17691221-1e59-4d1f-8d17-dfef648d0a0e) </br>
    https://docs.ultralytics.com/ </br>
    https://github.com/ultralytics/ultralytics
    

- ### VisDrone-Dataset
    https://github.com/VisDrone/VisDrone-Dataset

- ### Next.js / Vercel / OpenCV
    <img width="89" alt="image" src="https://github.com/user-attachments/assets/4479830a-50a4-4900-ae4b-fcad14a77d89">

    [Next.js API Routes Guide](https://nextjs.org/docs/api-routes/introduction) </br>

    <img width="132" alt="image" src="https://github.com/user-attachments/assets/096ae1bc-6d6a-4add-9f0f-7e821bfc679c">
    
    [Vercel Documentation](https://vercel.com/docs) </br>

    <img width="65" alt="image" src="https://github.com/user-attachments/assets/e4461506-3ac4-4cb9-b5c3-1bd21471c53b">

    [OpenCV Documentation](https://docs.opencv.org/4.10.0/)

- ### 기타 웹사이트
    https://ganghee-lee.tistory.com/34 </br>
    https://en.wikipedia.org/wiki/Jaccard_index
    
