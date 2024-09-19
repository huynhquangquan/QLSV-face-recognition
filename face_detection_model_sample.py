# FACE DETECTION SAMPLES
import os
import time
import cv2
import numpy as np
import cvzone
from PIL import Image
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
imgBackground = cv2.imread('resources/background.jpg')
TRAIN_DATA = 'images'
# background 696x430

#Tải các img mode lên imgModeList
folderModePath = 'resources/mode'
modePathList = os.listdir(folderModePath)
imgModeList = []

for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))

imgMode = imgModeList[2]

# Xác định vị trí trên ảnh nền để chèn ảnh frame
x_offset = 0  # Vị trí Webcam ngang
y_offset = 0  # Vị trí Webcam dọc
modex_offset = 775  # Vị trí mode ngang
modey_offset = 0  # Vị trí mode dọc


# Quá trình nhận diện khuôn mặt
while True:
    success, frame = cap.read()
    frame = cv2.resize(frame, (773, 605))
    imgModeList[0] = cv2.resize(imgModeList[0], (205,214))

    # Kiểm tra xem kích thước của phần ảnh nền mà bạn muốn chèn ảnh frame vào có phù hợp với kích thước của ảnh frame hay không
    if imgBackground.shape[1] - x_offset < frame.shape[1] or imgBackground.shape[0] - y_offset < frame.shape[0]:
        print("Kích thước của ảnh frame không phù hợp với kích thước của phần ảnh nền mà bạn muốn chèn nó vào.")
        print(f'{imgBackground.shape[1]}-{x_offset}={imgBackground.shape[1]-x_offset}<{frame.shape[1]}')
        print(f'{imgBackground.shape[0]}-{y_offset}={imgBackground.shape[0]-y_offset}<{frame.shape[0]}')
        break

    # Chèn ảnh frame vào ảnh nền
    imgBackground[y_offset:y_offset+frame.shape[0], x_offset:x_offset+frame.shape[1]] = frame # Kết quả cuối cùng của Frame + Background
    imgBackground[modey_offset:modey_offset + imgMode.shape[0], modex_offset:modex_offset + imgMode.shape[1]] = imgMode # Kết quả cuối cùng của Frame + Mode


    faces = face_detector.detectMultiScale(imgBackground, 1.3, 5) # Rectangle nhận diện khuôn mặt

    err = 9999.9999
    #Quá trình nhận diện khuôn mặt với rectangle
    for (x, y, w, h) in faces:  #Tự động di chuyển rectangle nhận diện
        image_detection = cv2.resize(frame[y+2: y+h-2, x+2: x+w-2], (128,128)) # frame nhận diện về size 200,200
        image_path = os.path.join('face_detection_img', 'faces_detecting.jpg') # Path của folders mới
        cv2.imwrite(image_path, image_detection) # Lưu images_detected vào folder mới trong Path
        cvzone.cornerRect(imgBackground, (x, y, w, h), rt=0)
        # cv2.rectagle (imgBackground, (x, y), (x+w, y+h), (128,255,50), 3)

        # image_detection_real_time_data = cv2.imread('face_detection_img/faces_detecting.jpg', cv2.IMREAD_GRAYSCALE)

        # for i in os.listdir(TRAIN_DATA):
        #     i_path = os.path.join(TRAIN_DATA, i)
        #     for filename in os.listdir(i_path):
        #         filename_path = os.path.join(i_path,filename)  # Path cuối cùng dẫn đến thư viện IMG cần thiết (images/posName)
        #         label = filename_path.split('\\')[1]  # Name nhận diện
        #         images_from_folder = cv2.imread(filename_path, cv2.IMREAD_GRAYSCALE)
        #         err = np.sum((images_from_folder.astype("float") - image_detection_real_time_data.astype("float")) ** 2)
        #         err /= float(images_from_folder.shape[0] * image_detection_real_time_data.shape[1])
        #         print(err)
        #         if err < 1200:
        #             cvzone.cornerRect(imgBackground, (x,y,w,h), rt=0)
        #             print(label)
        #             print("Nhận diện thành công!")
        #         else:
        #             print("Không nhận diện được!")


    
    cv2.imshow('WEBCAM', imgBackground)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()