import cv2
from parking_management import ParkingManagement     
import time
import requests
import time

URL = "https://evcharge-status.vercel.app/api/update-parking-data"  # Next.js 서버 주소

def send_parking_data(vehicle_times):
    data = {
        "parking_times":vehicle_times
    }
    response = requests.post(URL, json=data)
    if response.status_code == 200:
        print("Data sent successfully")
    else:
        print("Failed to send data")

# start webcam (라즈베리파이인 경우 수정)
from picamera2 import Picamera2
picam2 = Picamera2()
picam2.preview_configuration.main.size = (1280, 720)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()


json_file = "bounding_boxes.json"                       # 주차장 좌표값을 저장한 json파일 경로
test_parking_list = [0, 0, 0, 0, 0, 0, 0]               # 이전 주차공간 리스트
parking_list =  test_parking_list                       # 현재 주차공간 리스트
vehicle_times = [""] * len(test_parking_list)            # 각 주차 공간에서 차량이 머문 시간 (초 단위)
last_inference_time = time.time()                       # 마지막 추론시간 기록
inference_interval = 2                                  # 추론 간격 (초)
vehicle_entry_times = [None] * len(test_parking_list)   # 각 주차 공간의 차량 진입 시간
miss_count =  [0] * len(test_parking_list)              # 차량이 있다가 나간 순간 얼마나 없었는지 기록 ex) 추론간격 1초 일때 1초마다 카운트 1 증가
limit_counter = 2                                       # 차량이 없어진 후 몇초가 경과하면 떠났다고 판단할 수
x = 0                                                   # 추론할 공간 (x 좌표)
y = 0                                                   # 추론할 공간 (y 좌표)

print(vehicle_times)
parking_manager = ParkingManagement(model_path="yolov8n.pt") # 학습된 모델 불러오기  

while True:
    frame = picam2.capture_array()
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    jss_data = parking_manager.parking_regions_extraction(json_file)
    current_time = time.time()
    track_img = frame[x:, y:]

    # 일정시간마다 추론
    if current_time - last_inference_time >= inference_interval:

        # 차량 위치 탐색 후 객체 추적
        result = parking_manager.model.track(track_img, persist=True, show=False)

        # 객체가 있을 경우
        if result[0].boxes.id is not None:
            boxes = result[0].boxes.xyxy.cpu().tolist()                                       # 검출된 객체 박스 위지
            clss = result[0].boxes.cls.cpu().tolist()                                         # 검출된 class 이름
            parking_list = parking_manager.process_data(jss_data, frame, boxes, clss, x, y)   # 주차장 위치와 객체 위치 비교 후 주차여부 반환

        for idx in range(len(parking_list)):

            # 차량이 새로 들어오고 이전에 떠나지 않았을 경우
            if test_parking_list[idx] == 0 and parking_list[idx] == 1 and miss_count[idx] == 0:
                vehicle_entry_times[idx] = time.time()                            # 진입 시간 기록

            # 차량이 떠났을 경우
            elif test_parking_list[idx] == 1 and parking_list[idx] == 0:
                min_sec = int(time.time() - vehicle_entry_times[idx]) 
                minutes, seconds = divmod(min_sec, 60)
                vehicle_times[idx] = f"{minutes:02}:{seconds:02}"  # 머문 시간 계산
                miss_count[idx] += 1                                              # 떠난 시간 카운트 시작
            
            # 차량이 주차 공간에 있는 경우
            elif parking_list[idx] == 1:
                min_sec = int(time.time() - vehicle_entry_times[idx]) 
                minutes, seconds = divmod(min_sec, 60)
                vehicle_times[idx] = f"{minutes:02}:{seconds:02}"   # 머문 시간 계산
                miss_count[idx] = 0

            # 차량이 없는 경우 
            elif parking_list[idx] == 0:

                # 차량이 떠나지 않았던 경우
                if miss_count[idx] == 0:
                    vehicle_entry_times[idx] = 0   # 진입 시간 초기화
                    vehicle_times[idx] = ""        # 머문 시간 초기화

                # 차량이 떠난 후 'limit_counter'만큼 경과하면 
                elif miss_count[idx] > limit_counter:
                    miss_count[idx] = 0            # 떠난 시간 초기화
                    vehicle_entry_times[idx] = 0   # 진입 시간 초기화
                    vehicle_times[idx] = ""        # 머문 시간 초기화
                else:
                    miss_count[idx] += 1
            print(f"주차공간 {idx + 1}: {vehicle_times[idx]}초째 머물러 있습니다.")  

        print("------------",test_parking_list,"-------------")   # 이전 주차기록
        print("------------",parking_list,"-------------")        # 현재 주차기록
        print("------------",vehicle_times,"-------------")       # 차량이 머문시간(초)
        send_parking_data(vehicle_times)
        # 주차공간, 마지막 추론시간 업데이트
        test_parking_list = parking_list
        last_inference_time = current_time

    # 프레임을 표시
    #parking_manager.display_frames(frame)

    # q를 입력하면 종료
    if cv2.waitKey(1) == ord('q'):
        break
    
    


