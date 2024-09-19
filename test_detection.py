import cv2
import pickle
import cvzone
import numpy as np
import time
import os
import numbers
from datetime import datetime

def testing_anti_model(choice, load_model_flag):
    from tensorflow.keras.models import load_model
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    global cap
    cap = None
    if choice == 0:
        cap = cv2.VideoCapture(0)
    elif choice != 0:
        if os.path.exists(choice):
            print("File exists")
        else:
            print("File does not exist")
        print(f"Opening video file: {choice}")
        cap = cv2.VideoCapture(choice)
        if not cap.isOpened():
            print("Error opening video stream or file")
            return

    models = None # Rename 'models' to 'model' to avoid confusion

    if load_model_flag is True:
        models = load_model('model-anti-spoofing-softmax.h5', compile=False) # Correctly call load_model
    else:
        models = None

    listResult = ["Real","Fake"]
    ptime = 0
    while True:
        success, img = cap.read()
        if not success:
            print("Frame is empty")
            break
        # ---------fps-------#
        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime
        cv2.putText(
            img,
            f'FPS:{fps}',
            (20, img.shape[0] - 20),
            cv2.FONT_HERSHEY_DUPLEX,
            1,
            (255, 0, 255),
            1
        )
        faces = face_detector.detectMultiScale(img, scaleFactor=1.3, minNeighbors=3)

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
            print(w*h)
            cvzone.cornerRect(img, (x, y, w, h), rt=0)
            if w * h < 40000:
                pass
            else:
                cv2.putText(img, f'{listResult[result]}: {predictions[0][result]}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (255, 0, 0), 3)
                print("Anti-spoofing:")
                print(predictions[0][result])
                print(listResult[result])

        cv2.imshow("Webcam (press ESC to quit)", img)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()