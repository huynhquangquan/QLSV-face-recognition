import cv2
import pickle
import cvzone
import face_recognition
import numpy as np
from tkinter import *
from tkinter import messagebox
import managing_function
import time
from threading import Thread
import excel_attandance
import mysql.connector
import os
import pygame.mixer
from PIL import Image
import tensorflow
import numbers
from tensorflow.keras import models
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from imutils import face_utils
from scipy.spatial import  distance as dist
import dlib
from datetime import datetime
from os import sys

global online_mode
online_mode = messagebox.askyesno("Lựa chọn chế độ Camera","Bạn có muốn bật Camera ngoài để duyệt khuôn mặt?")

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
global cap
cap = None
prev_img = None
motion_count = False
# load encoding file

models = load_model('model-anti-spoofing-softmax.h5', compile=False)
file = open('model-student.p', 'rb')
listResult = ["Real","Fake"]
encodeListKnownIds = pickle.load(file)
file.close()
encodeListKnown, students = encodeListKnownIds
studentids = []
studentnames = []
for student in students:
    id_name = student.split('_')
    studentids.append(id_name[0])
    studentnames.append(id_name[1])

exit_if_True = False
# user = ''
check_id = ''
pygame.init()
pygame.mixer.init()

history_detecting_folder = "history_detecting"
global destination_history_detecting_folder
destination_history_detecting_folder = None
for root, dirs, files in os.walk('.'):
    if history_detecting_folder in dirs:
        destination_history_detecting_folder = os.path.join(root, history_detecting_folder)
        print(destination_history_detecting_folder)
        break

def select_camera(online_mode):
    global cap
    laptop_camera = cv2.VideoCapture(0)
    if laptop_camera.isOpened():
        print("Laptop camera is available.")
    else:
        print("Laptop camera is not available.")

    external_camera = cv2.VideoCapture(1)
    # external_camera = cv2.VideoCapture('http://192.168.1.15:8080/video') # Không Khuyến khích
    if external_camera.isOpened():
        print("External camera is available.")
    else:
        print("External camera is not available.")

    if online_mode:
        cap = laptop_camera
        if laptop_camera.isOpened():
            return cap
        else:
            return None
    else:
        cap = external_camera
        if external_camera.isOpened():
            return cap
        else:
            messagebox.showwarning("Lỗi Camera!", "Không có Camera ngoài, chuyển sang Camera mặc định!")
            return select_camera(True)

#Eyes detection ------
blink_thresh = 0.5
tt_frame = 3
count = 0
global eyes_movement
eyes_movement = None
detector = dlib.get_frontal_face_detector()
ln_model = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
#--Eyes id---
(L_start, L_end) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(R_start, R_end) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
ptime = 0
def EAR_cal(eye):
    #vertical#
    v1 =  dist.euclidean(eye[1],eye[5])
    v2 = dist.euclidean(eye[2],eye[4])

    #horizontal
    h1 = dist.euclidean(eye[0],eye[3])
    ear = (v1+v2)/h1
    return ear
#------------

selected_camera = select_camera(not online_mode)
prev_frame = None
if selected_camera is not None:
    while not exit_if_True:
        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            cap.set(cv2.CAP_PROP_FRAMES,0)
        success, img = cap.read()
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #---------fps-------#
        ctime = time.time()
        fps = 1/(ctime-ptime)
        ptime = ctime
        cv2.putText(
            img,
            f'FPS:{fps}',
            (20,img.shape[0]-20),
            cv2.FONT_HERSHEY_DUPLEX,
            1,
            (255,0,0),
            1
        )


        match_found = False
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        faceCurFrame = face_recognition.face_locations(imgS)
        encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)
        for encoFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encoFace)
            facedis = face_recognition.face_distance(encodeListKnown, encoFace)
            matchIndex = np.argmin(facedis)
            faces = face_detector.detectMultiScale(img, 1.3, 3)

            for (x, y, w, h) in faces:
                if x < 0:
                    x = 0
                if y < 0:
                    y = 0
                if w < 0:
                    x = 0
                if h < 0:
                    y = 0
                detecting = cv2.resize(img[y:y + h, x:x + w], (128, 128))
                predictions = models.predict(detecting.reshape(-1, 128, 128, 3))
                result = np.argmax(predictions)
                # object_detecting = cv2.resize(img, (640, 480))
                # object_predictions = models_object.predict(object_detecting.reshape(-1, 640, 480, 3))
                # object_result = np.argmax(object_predictions)
                # print("Object")
                # print(object_predictions[0][result])
                # print(listResult_Object[result])
                print("Anti-spoofing:")
                print(predictions[0][result])
                print(listResult[result])
                print("Face_recognition diff:")
                print(facedis[matchIndex])
                print(students[matchIndex])
                area = w * h
                print(f'BoundingBox:{area}')
                if area < 40000:
                    # cvzone.cornerRect(img, (x, y, w, h), rt=0)
                    pass
                elif matches[matchIndex] and facedis[matchIndex] < 0.5:
                    # -------face detection------
                    faces_eyes = detector(img_gray)
                    for face_eye in faces_eyes:
                        # ---------landmarks---------
                        shapes = ln_model(img_gray, face_eye)
                        shape = face_utils.shape_to_np(shapes)

                        # --------Eye landmarks------
                        lefteye = shape[L_start:L_end]
                        righteye = shape[R_start:R_end]

                        # for Lpt, rpt in zip(lefteye, righteye):
                        #     cv2.circle(img, Lpt, 2, (200, 200, 0), 2)
                        #     cv2.circle(img, rpt, 2, (200, 200, 0), 2)  # Display the eyes detection
                        left_ear = EAR_cal(lefteye)
                        right_ear = EAR_cal(righteye)

                        avg = (left_ear + right_ear) / 2

                        if avg < blink_thresh:
                            count += 1
                        else:
                            if count > tt_frame:
                                eyes_movement = True
                                count = 0
                                if listResult[result] == "Real" and predictions[0][result] > 0.5:

                                    # global threshold
                                    # threshold = None
                                    #
                                    # if prev_frame is not None:
                                    #     gray_current_frame = cv2.cvtColor(detecting, cv2.COLOR_RGB2RGBA)
                                    #     gray_prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_RGB2RGBA)
                                    #
                                    #     diff = cv2.absdiff(gray_current_frame, gray_prev_frame)
                                    #     diff_sum = np.sum(diff)
                                    #     print(f'Motions:{diff_sum}')
                                    #     if 200000 > diff_sum > 100000:
                                    #         print("Có chuyển động")
                                    #         threshold = True
                                    #     else:
                                    #         print("Không có chuyển động")
                                    #         threshold = False
                                    # prev_frame = detecting.copy()
                                    # test_path = "test/prev.jpg"
                                    # test1_path = "test/current.jpg"
                                    # threshold_prev = cv2.imwrite(test_path, detecting)
                                    # threshold_current = cv2.imwrite(test1_path, prev_frame) # Debugging/Testing Result of threshold

                                    # if threshold is True:
                                    cvzone.cornerRect(img, (x, y, w, h), rt=0)
                                    cv2.putText(img, f'MSSV: {str(studentids[matchIndex])}', (x + 15, y - 40),
                                                cv2.FONT_HERSHEY_DUPLEX,
                                                1, (0, 204, 0), 3)
                                    cv2.putText(img, str(studentnames[matchIndex]), (x + 15, y - 15), cv2.FONT_HERSHEY_DUPLEX,
                                                1,
                                                (0, 204, 0), 3)
                                    with open('result.txt', 'w') as f:
                                        f.write(str(studentids[matchIndex]))
                                    with open('result.txt', 'r') as f:
                                        user = f.read().strip()
                                    connection, cursor = managing_function.connect_to_database()
                                    cursor.execute("SELECT idSinhVien FROM sinhvien WHERE idSinhVien = %s", (user,))
                                    temp = cursor.fetchone()
                                    result_db = temp[0]
                                    print(result_db)
                                    if result_db:
                                        check_id = int(result_db)
                                        if check_id == int(studentids[matchIndex]):
                                            match_found=True
                                    # print("Anti-spoofing:")
                                    # print(predictions[0][result])
                                    # print(listResult[result])
                                    # print("Face_recognition diff:")
                                    # print(facedis[matchIndex])
                                    # print(students[matchIndex])
                                    print(f'Facial movement detected: {eyes_movement}')
                                eyes_movement = False
                            else:
                                eyes_movement = False
                else: eyes_movement = False

        cv2.imshow("Webcam (press ESC to quit)", img)
        if match_found:
            pygame.mixer.Sound("sound effect.mp3").play()
            if messagebox.askyesno(title='Xác Nhận', message=f'Bạn có phải là sinh viên có ID {check_id}'):
                connection, cursor = managing_function.connect_to_database()
                cursor.execute("SELECT hovaten FROM sinhvien WHERE idSinhVien = %s", (check_id,))
                username_found = cursor.fetchone()
                excel_attandance.diary_attandance(username_found[0], check_id)

                image_path = os.path.join(destination_history_detecting_folder,f'{check_id}_{datetime.now().strftime('%d-%m')}_{datetime.now().strftime('%Hh%Mm')}.jpg')

                print(f"Saving image to: {image_path}")
                succeed = cv2.imwrite(image_path, img)
                if not succeed:
                    print(f"Failed to save image to {image_path}")
                else:
                    print(f"Image saved successfully to {image_path}")

                if messagebox.askyesno(title='Đã Điểm Danh', message=f'Bạn có muốn vào ứng dụng không?'):
                    pass
                else:
                    with open('result.txt', 'w') as f:
                        f.write('')
                    time.sleep(0.2)
                exit_if_True = True
            else:
                with open('result.txt', 'w') as f:
                    f.write('')
                match_found = False
        # time.sleep(0.5)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     exit_if_True = True
        if cv2.waitKey(1) & 0xFF == 27:
            exit_if_True = True
else:
    print("Không có Camera")
sys.exit()