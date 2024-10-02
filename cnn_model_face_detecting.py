# COMPLETE FACE DETECTION
import cvzone
import time
import numpy as np
import cv2
import os
from PIL import Image
import tensorflow
import numbers
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam

model_path = 'model-student2.h5'

if os.path.exists(model_path):
    os.remove(model_path)
    print(f"Deleted existing model file: {model_path}")
else:
    print(f"No existing model file found: {model_path}")
# MODEL_DATA_TRAINING/MODEL_SAVES-------------------------------------------------------------------------------------------------------------------------
TRAIN_DATA = 'datasets/traindata'
TEST_DATA = 'datasets/testdata'


xtrain = [] # Ma trận
ytrain = [] # Nhãn

xtest = []
ytest = []
dict = {'1_trung': [1,0,0], '2_nghia': [0,1,0], "3_quan": [0,0,1],
        '1_testtrung': [1,0,0], '2_testnghia': [0,1,0], "3_testquan": [0,0,1]}

def getData(dirData,listData):
    for i in os.listdir(dirData):
        i_path = os.path.join(dirData,i)
        list_filename_path = []
        for filename in os.listdir(i_path):
            filename_path = os.path.join(i_path, filename) # Path cuối cùng dẫn đến thư viện IMG cần thiết (images/posName)
            label = filename_path.split('\\')[1] # Name nhận diện
            # for img in os.listdir(filename_path):
            #     pic = np.array(Image.open(os.path.join(img,filename_path))
            img = np.array(Image.open(filename_path)) # Dàn ma trận của Img
            list_filename_path.append((img, dict[label])) #để in ra tên folder chứa images

        listData.extend(list_filename_path) # Tổng các ma trận của các Imgs trong file Images
    return listData

xtrain = getData(TRAIN_DATA, xtrain)
xtest = getData(TEST_DATA, xtest)

np.random.shuffle(xtrain)
np.random.shuffle(xtrain)
np.random.shuffle(xtrain)
np.random.shuffle(xtrain)
np.random.shuffle(xtrain)
np.random.shuffle(xtrain)
np.random.shuffle(xtrain)
np.random.shuffle(xtrain)
np.random.shuffle(xtrain)
np.random.shuffle(xtrain)

# print(xtrain[3])

model_training_first = models.Sequential([
    layers.Conv2D(32, (3,3),padding='same',  input_shape=(280,280,3), activation='relu'),
    layers.MaxPool2D((2,2)),
    # layers.Dropout(0.5),

    layers.Conv2D(64, (3, 3), padding='same', activation='relu'),
    layers.MaxPool2D((2, 2)),
    # layers.Dropout(0.2),

    layers.Conv2D(128, (3,3),padding='same', activation='relu'),
    layers.MaxPool2D((2,2)),
    # layers.Dropout(0.2),

    layers.Flatten(),
    layers.Dense(512, activation='relu'),
    layers.Dense(128, activation='relu'),
    layers.Dense(3,activation='softmax'),
])
model_training_first.summary()

model_training_first.compile(optimizer=Adam(learning_rate=0.0001), #SGD=stochastic gradient decent
                             loss='categorical_crossentropy',
                             metrics=['accuracy'])

model_training_first.fit(np.array([x[0] for _,x in enumerate(xtrain)]),np.array([y[1] for _ ,y in enumerate(xtrain)]),batch_size=64, epochs=5, validation_data=(np.array([x[0] for _,x in enumerate(xtest)]),np.array([y[1] for _ ,y in enumerate(xtest)])),shuffle=True)


model_training_first.save('model-student2.h5')

# AUTO ENCODING MODEL/MODEL TRAINING/MODEL SAVES (UNFINISHED)----------------------------------------------------------------------------------------

# from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#
# # Đường dẫn đến thư mục chứa dữ liệu
# TRAIN_DATA = 'datasets/traindata'
# TEST_DATA = 'datasets/testdata'
#
# # Danh sách để lưu trữ tên thư mục và tệp
# labels = []
#
# # Hàm để lấy dữ liệu từ thư mục
# def getData(dirData):
#     data = []
#     for i in os.listdir(dirData):
#         i_path = os.path.join(dirData, i)
#         for filename in os.listdir(i_path):
#             filename_path = os.path.join(i_path, filename)
#             label = os.path.basename(i_path) # Sử dụng tên thư mục làm nhãn
#             img = np.array(Image.open(filename_path))
#             data.append((img, label))
#             labels.append(label) # Di chuyển dòng này vào trong vòng lặp tệp
#     return data
#
# # Lấy dữ liệu từ thư mục
# xtrain = getData(TRAIN_DATA)
# # xtest = getData(TEST_DATA)
# print(labels)
#
# # Tạo hot encoding cho nhãn
# label_encoder = LabelEncoder()
# encoded_labels = label_encoder.fit_transform(labels)
# one_hot_encoder = OneHotEncoder(sparse_output=False)
# one_hot_encoded_labels = one_hot_encoder.fit_transform(encoded_labels.reshape(-1, 1))
#
# # Tạo mô hình
# model_training_first = models.Sequential([
#     layers.Conv2D(64, (3,3), padding='same', input_shape=(128,128,3), activation='relu'),
#     layers.MaxPool2D((2,2)),
#     layers.Conv2D(64, (3, 3), padding='same', activation='relu'),
#     layers.MaxPool2D((2, 2)),
#     layers.Conv2D(128, (3,3), padding='same', activation='relu'),
#     layers.MaxPool2D((2,2)),
#     layers.Flatten(),
#     layers.Dense(512, activation='relu'),
#     layers.Dense(128, activation='relu'),
#     layers.Dense(one_hot_encoded_labels.shape[1], activation='softmax'),
# ])
# model_training_first.summary()
#
# # Compile và huấn luyện mô hình
# model_training_first.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# model_training_first.fit(np.array([x[0] for x in xtrain]), np.array([y[1] for y in xtrain]), batch_size=64, epochs=3, shuffle=True)
#
# # Lưu mô hình
# model_training_first.save('model-student3.h5')
#

# MODEL_LOADING
# models = models.load_model('model-student_5epochs.h5')


# FACE_DETECTING-------------------------------------------------------------------------------------------------------------------------
# listResult = [('quan','1'), ('nghia','2'), ('son','3')]
# face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#
# cap = cv2.VideoCapture("NhanDienKhuonMat/face_check/nghia.mp4")
# imgBackground = cv2.imread('resources/background.jpg')
# # background 696x430
#
# # Tải các img mode lên imgModeList
# # folderModePath = 'resources/mode'
# # modePathList = os.listdir(folderModePath)
# # imgModeList = []
#
# # for path in modePathList:
# #     imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))
#
# # imgMode = imgModeList[2]
#
# # Xác định vị trí trên ảnh nền để chèn ảnh frame
# x_offset = 0  # Vị trí Webcam ngang
# y_offset = 0  # Vị trí Webcam dọc
# # modex_offset = 775  # Vị trí mode ngang
# # modey_offset = 0  # Vị trí mode dọc
#
# # Quá trình nhận diện khuôn mặt
# while True:
#     success, frame = cap.read()
#     frame = cv2.resize(frame, (1100,800))
#     imgBackground = cv2.resize(imgBackground, (1350,800))
#     # imgModeList[0] = cv2.resize(imgModeList[0],q (205, 214))
#
#     # Kiểm tra xem kích thước của phần ảnh nền mà bạn muốn chèn ảnh frame vào có phù hợp với kích thước của ảnh frame hay không
#     if imgBackground.shape[1] - x_offset < frame.shape[1] or imgBackground.shape[0] - y_offset < frame.shape[0]:
#         print("Kích thước của ảnh frame không phù hợp với kích thước của phần ảnh nền mà bạn muốn chèn nó vào.")
#         print(f'{imgBackground.shape[1]}-{x_offset}={imgBackground.shape[1] - x_offset}<{frame.shape[1]}')
#         print(f'{imgBackground.shape[0]}-{y_offset}={imgBackground.shape[0] - y_offset}<{frame.shape[0]}')
#         break
#
#     # Chèn ảnh frame vào ảnh nền
#     imgBackground[y_offset:y_offset + frame.shape[0],x_offset:x_offset + frame.shape[1]] = frame  # Kết quả cuối cùng của Frame + Background
#     # imgBackground[modey_offset:modey_offset + imgMode.shape[0],modex_offset:modex_offset + imgMode.shape[1]] = imgMode  # Kết quả cuối cùng của Frame + Mode
#     # imgBackground=frame
#
#     faces = face_detector.detectMultiScale(imgBackground, 1.3, 5)  # Rectangle nhận diện khuôn mặt
#     # Quá trình nhận diện khuôn mặt với rectangle
#     for (x, y, w, h) in faces:  # Tự động di chuyển rectangle nhận diện
#         # image_detection = cv2.resize(frame[y + 2: y + h - 2, x + 2: x + w - 2],(128, 128))  # frame nhận diện về size 128,128
#         # image_path = os.path.join('face_detection_img', 'faces_detecting.jpg')  # Path của folders mới
#         # cv2.imwrite(image_path, image_detection)  # Lưu images_detected vào folder mới trong Path
#         detecting = cv2.resize(imgBackground[y: y+h,x: x+w],(128,128))
#         # result = np.argmax(models.predict(detecting.reshape((-1,128,128,3))))
#         # Giả sử `predictions` là mảng xác suất trả về từ mô hình
#         predictions = models.predict(detecting.reshape(-1, 128, 128, 3))
#
#         # Tìm lớp có độ chính xác cao nhất
#         result = np.argmax(predictions)
#         # time.sleep(0.5)
#         print(models.predict(detecting.reshape(-1,128,128,3)))
#         print(result)
#         if predictions[0][result] > 0.95:
#             if x < 70 or x > 800:
#                 continue
#             if x + w > 1000:
#                 w = 1000 - x
#             cvzone.cornerRect(imgBackground, (x, y, w, h), rt=0)
#             cv2.putText(imgBackground,(listResult[result])[0],(x+15,y-15),cv2.FONT_HERSHEY_SIMPLEX,1,(255,25,255), 5)
#             if int((listResult[result])[1]) == 1:
#                 print("id 1")
#         else:
#             cv2.putText(imgBackground, 'Loading', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 25, 255), 2)
#
#     cv2.imshow('WEBCAM', imgBackground)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows
# TRAIN_DATA: images, i_path: images/posName, filename_path: images/posName/images_{}.jpg

