# FACE_RECOGNITION
import pickle
import cvzone
import time
import numpy as np
import cv2
import os
import pygame.mixer
from PIL import Image
import tensorflow
import numbers
from tensorflow.keras import layers
from tensorflow.keras.models import load_model
from tensorflow.keras import models
from tkinter import *
from tkinter import messagebox
import managing_function
import time
from threading import Thread
import excel_attandance
import mysql.connector
from tensorflow.keras.preprocessing.image import img_to_array
from datetime import datetime

models = load_model('model-student2.h5')
models_anti_spoofing = load_model('model-anti-spoofing.h5')

Liveliness = ["Real","Fake"]
listResult = [("LeVanTrung","1"),( "PhamHuuNghia","2"),("HuynhQuangQuan","3")]
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
# imgBackground = cv2.imread('resources/background.jpg')
# count = 0
prev_img = None
motion_count = False
exit_if_True = False
user = ''
match_found = False
check_id = ''
pygame.init()
pygame.mixer.init()
# background 696x430
history_detecting_folder = "history_detecting"
global destination_history_detecting_folder
destination_history_detecting_folder = None
for root, dirs, files in os.walk('.'):
    if history_detecting_folder in dirs:
        destination_history_detecting_folder = os.path.join(root, history_detecting_folder)
        print(destination_history_detecting_folder)
        break
# Tải các img mode lên imgModeList
# folderModePath = 'resources/mode'
# modePathList = os.listdir(folderModePath)
# imgModeList = []

# for path in modePathList:
#     imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

# imgMode = imgModeList[2]

# Xác định vị trí trên ảnh nền để chèn ảnh frame
# x_offset = 0  # Vị trí Webcam ngang
# y_offset = 0  # Vị trí Webcam dọc
# modex_offset = 775  # Vị trí mode ngang
# modey_offset = 0  # Vị trí mode dọc

# Quá trình nhận diện khuôn mặt
while not exit_if_True:
    success, frame = cap.read()
    match_found = False
    # frame = cv2.resize(frame, (1100,800))
    # imgBackground = cv2.resize(imgBackground, (1350,800))
    # imgModeList[0] = cv2.resize(imgModeList[0],q (205, 214))

    # Kiểm tra xem kích thước của phần ảnh nền mà bạn muốn chèn ảnh frame vào có phù hợp với kích thước của ảnh frame hay không
    # if imgBackground.shape[1] - x_offset < frame.shape[1] or imgBackground.shape[0] - y_offset < frame.shape[0]:
    #     print("Kích thước của ảnh frame không phù hợp với kích thước của phần ảnh nền mà bạn muốn chèn nó vào.")
    #     print(f'{imgBackground.shape[1]}-{x_offset}={imgBackground.shape[1] - x_offset}<{frame.shape[1]}')
    #     print(f'{imgBackground.shape[0]}-{y_offset}={imgBackground.shape[0] - y_offset}<{frame.shape[0]}')
    #     break

    # Chèn ảnh frame vào ảnh nền
    # imgBackground[y_offset:y_offset + frame.shape[0],x_offset:x_offset + frame.shape[1]] = frame  # Kết quả cuối cùng của Frame + Background
    # imgBackground[modey_offset:modey_offset + imgMode.shape[0],modex_offset:modex_offset + imgMode.shape[1]] = imgMode  # Kết quả cuối cùng của Frame + Mode
    imgBackground=frame

    # gray = cv2.cvtColor(imgBackground, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(imgBackground, 1.3, 3)  # Rectangle nhận diện khuôn mặt
    # Quá trình nhận diện khuôn mặt với rectangle
    for (x, y, w, h) in faces:  # Tự động di chuyển rectangle nhận diện
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        if w < 0:
            x = 0
        if h < 0:
            y = 0
        detecting = cv2.resize(imgBackground[y:y+h, x:x+w], (280, 280))
        # detecting = cv2.cvtColor(detecting, cv2.COLOR_GRAY2BGR)
        # Giả sử `predictions` là mảng xác suất trả về từ mô hình
        predictions = models.predict(detecting.reshape(-1, 280, 280, 3))
        predictions_anti_spoofing = models_anti_spoofing.predict(detecting.reshape(-1,280,280,3))
        # Tìm lớp có độ chính xác cao nhất
        result = np.argmax(predictions)
        live = np.argmax(predictions_anti_spoofing)
        print("Student")
        print(models.predict(detecting.reshape(-1,280,280,3))) # student
        print((listResult[result])[0])
        print("Anti-Spoofing")
        print(models_anti_spoofing.predict(detecting.reshape(-1,280,280,3))) # liveliness
        print((Liveliness[live]))
        area = w * h
        print("Distance")
        print(area)
        if area < 40000:
            pass
        elif predictions[0][result] > 0.9:# and Liveliness[live] == "Real":
            # if x < 70 or x > 800:
            #     continue
            # if x + w > 1000:
            #     w = 1000 - x
            cvzone.cornerRect(imgBackground, (x, y, w, h), rt=0)
            cv2.putText(imgBackground,f'MSSV:{(listResult[result])[1]}',(x+10,y-40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,204,0), 5)
            cv2.putText(imgBackground, (listResult[result])[0], (x+10, y-15), cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 204, 0), 5)
            with open('result.txt', 'w') as f:
                f.write(str((listResult[result])[1]))
            with open('result.txt', 'r') as f:
                user = f.read().strip()
            connection, cursor = managing_function.connect_to_database()
            cursor.execute("SELECT idSinhVien FROM sinhvien WHERE idSinhVien = %s", (user,))
            result_db = cursor.fetchone()
            if result_db:
                check_id = result_db[0]
                if check_id == int((listResult[result])[1]):
                    match_found = True
            # if int((listResult[result])[1]) == 1:
            #     print("nghia")
            # if int((listResult[result])[1]) == 2:\
            #     print("son")
            # if int((listResult[result])[1]) == 3:
            #     print("quan")
            # image_path = os.path.join('datasets - TRAIN', f'{listResult[result][0]}_{count}.jpg')  # Path của folders mới/ check
            # cv2.imwrite(image_path, detecting)  # Lưu images khuôn mặt vào folder mới trong Path
            # count += 1 # check

    cv2.imshow("Webcam (press ESC to quit)", imgBackground)
    if match_found:
        pygame.mixer.Sound("sound effect.mp3").play()
        if messagebox.askyesno(title='Xác Nhận', message=f'Bạn có phải là sinh viên có ID {(listResult[result])[1]}'):
            connection, cursor = managing_function.connect_to_database()
            cursor.execute("SELECT hovaten FROM sinhvien WHERE idSinhVien = %s", (check_id,))
            username_found = cursor.fetchone()
            excel_attandance.diary_attandance(username_found[0],check_id)
            image_path = os.path.join(destination_history_detecting_folder, f'{check_id}_{datetime.now().strftime('%d-%m')}_{datetime.now().strftime('%Hh%Mm')}.jpg')

            print(f"Saving image to: {image_path}")
            succeed = cv2.imwrite(image_path, imgBackground)
            if not succeed:
                print(f"Failed to save image to {image_path}")
            else:
                print(f"Image saved successfully to {image_path}")

            print(image_path)
            if messagebox.askyesno(title='Đã Điểm Danh', message=f'Bạn có muốn vào ứng dụng không?'):
                exit_if_True = True
            else:
                with open('result.txt', 'w') as f:
                    f.write('')
                exit_if_True = True
        else:
            with open('result.txt', 'w') as f:
                f.write('')
            match_found = False
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     exit_if_True = True
    time.sleep(0.5)
    if cv2.waitKey(1) & 0xFF == 27:
        exit_if_True = True


########################################################################################################################################

