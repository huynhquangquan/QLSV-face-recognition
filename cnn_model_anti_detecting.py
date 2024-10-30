
# COMPLETE FACE DETECTION
import cvzone
import time
import keras
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
from tensorflow.keras.layers import RandomFlip, RandomZoom, RandomRotation
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.callbacks import CSVLogger


# csv_logger_sigmoid = CSVLogger(f'training_log_sigmoid.csv', separator='-', append=False)
csv_logger_softmax = CSVLogger(f'training_log_softmax.csv', separator='-', append=False)

# model_sigmoid_path = 'model-anti-spoofing-sigmoid.h5'
model_softmax_path = 'model-anti-spoofing-softmax.h5'


def delete_exist_model(model_path):
    if os.path.exists(model_path):
        os.remove(model_path)
        print(f"Deleted existing model file: {model_path}")
    else:
        print(f"No existing model file found: {model_path}")


# delete_exist_model(model_sigmoid_path)
delete_exist_model(model_softmax_path)
# MODEL_DATA_TRAINING/MODEL_SAVES-------------------------------------------------------------------------------------------------------------------------
TRAIN_DATA = 'datasets-anti-spoofing/traindata'
TEST_DATA = 'datasets-anti-spoofing/testdata'

# sigmoid_xtrain = []  # Ma trận
# sigmoid_ytrain = []  # Nhãn
softmax_xtrain = []
softmax_ytrain = []

# sigmoid_xtest = []
# sigmoid_ytest = []
softmax_xtest = []
softmax_ytest = []
dict = {'1_REAL': [1, 0], '2_FAKE': [0, 1],
        '1_testREAL': [1, 0], '2_testFAKE': [0, 1]}


def getData(dirData, listData):
    for i in os.listdir(dirData):
        i_path = os.path.join(dirData, i)
        list_filename_path = []
        for filename in os.listdir(i_path):
            filename_path = os.path.join(i_path,
                                         filename)  # Path cuối cùng dẫn đến thư viện IMG cần thiết (images/posName)
            label = filename_path.split('\\')[1]  # Name nhận diện
            # for img in os.listdir(filename_path):
            #     pic = np.array(Image.open(os.path.join(img,filename_path))
            img = np.array(Image.open(filename_path))  # Dàn ma trận của Img
            list_filename_path.append((img, dict[label]))  # để in ra tên folder chứa images

        listData.extend(list_filename_path)  # Tổng các ma trận của các Imgs trong file Images
    return listData


# sigmoid_xtrain = getData(TRAIN_DATA, sigmoid_xtrain)
# sigmoid_xtest = getData(TEST_DATA, sigmoid_xtest)
softmax_xtrain = getData(TRAIN_DATA, softmax_xtrain)
softmax_xtest = getData(TEST_DATA, softmax_xtest)

# np.random.shuffle(sigmoid_xtrain)
# np.random.shuffle(sigmoid_xtrain)
# np.random.shuffle(sigmoid_xtrain)
# np.random.shuffle(sigmoid_xtrain)
# np.random.shuffle(sigmoid_xtrain)
# np.random.shuffle(sigmoid_xtrain)
# np.random.shuffle(sigmoid_xtrain)
# np.random.shuffle(sigmoid_xtrain)
# np.random.shuffle(sigmoid_xtrain)
# np.random.shuffle(sigmoid_xtrain)

np.random.shuffle(softmax_xtrain)
np.random.shuffle(softmax_xtrain)
np.random.shuffle(softmax_xtrain)
np.random.shuffle(softmax_xtrain)
np.random.shuffle(softmax_xtrain)
np.random.shuffle(softmax_xtrain)
np.random.shuffle(softmax_xtrain)
np.random.shuffle(softmax_xtrain)
np.random.shuffle(softmax_xtrain)
np.random.shuffle(softmax_xtrain)
global model_softmax
model_softmax = None

if len(softmax_xtrain)>=2000: #complete
    BS = 64
    EP = 3
    LR = 0.000001
    model_softmax = models.Sequential([
        layers.Conv2D(32, (3, 3), padding="same", input_shape=(128, 128, 3), activation='relu'),
        layers.BatchNormalization(axis=-1),
        layers.MaxPool2D((2, 2)),
        layers.Dropout(0.25),

        layers.Conv2D(64, (3, 3), padding="same", activation='relu'),
        layers.BatchNormalization(axis=-1),
        layers.MaxPool2D((2, 2)),

        layers.Conv2D(128, (3, 3), padding="same", activation='relu'),
        layers.BatchNormalization(axis=-1),
        layers.MaxPool2D((2, 2)),
        layers.Dropout(0.3),

        layers.Flatten(),
        layers.Dense(1024, activation='relu'),
        layers.Dense(256, activation='relu'),
        layers.Dense(2, activation='softmax'),
        # layers.Dropout(0.3)
    ])
elif len(softmax_xtrain)>=1200: #complete
    BS = 32
    EP = 4
    LR = 0.00001
    model_softmax = models.Sequential([
        layers.Conv2D(32, (3, 3), padding="same", input_shape=(128, 128, 3), activation='relu'),
        layers.BatchNormalization(axis=-1),
        layers.MaxPool2D((2, 2)),
        layers.Dropout(0.2),

        layers.Conv2D(64, (3, 3), padding="same", activation='relu'),
        layers.BatchNormalization(axis=-1),
        layers.MaxPool2D((2, 2)),

        layers.Conv2D(128, (3, 3), padding="same", activation='relu'),
        layers.BatchNormalization(axis=-1),
        layers.MaxPool2D((2, 2)),
        layers.Dropout(0.1),

        layers.Flatten(),
        layers.Dense(1024, activation='relu'),
        layers.Dense(256, activation='relu'),
        layers.Dense(2, activation='softmax'),
        # layers.Dropout(0.3)
    ])
elif len(softmax_xtrain)>=600: #complete
    BS = 32
    EP = 5
    LR = 0.00001
    model_softmax = models.Sequential([
        layers.Conv2D(32, (3, 3), padding="same", input_shape=(128, 128, 3), activation='relu'),
        layers.BatchNormalization(axis=-1),
        layers.MaxPool2D((2, 2)),
        layers.Dropout(0.2),

        layers.Conv2D(64, (3, 3), padding="same", activation='relu'),
        layers.BatchNormalization(axis=-1),
        layers.MaxPool2D((2, 2)),

        layers.Conv2D(128, (3, 3), padding="same", activation='relu'),
        layers.BatchNormalization(axis=-1),
        layers.MaxPool2D((2, 2)),
        layers.Dropout(0.1),

        layers.Flatten(),
        layers.Dense(1024, activation='relu'),
        layers.Dense(256, activation='relu'),
        layers.Dense(2, activation='softmax'),
        # layers.Dropout(0.3)
    ])
elif len(softmax_xtrain)>=300: #complete
    BS = 64
    EP = 10
    LR = 0.000001
    model_softmax = models.Sequential([
        layers.Conv2D(32, (3, 3), padding="same", input_shape=(128, 128, 3), activation='relu'),
        layers.BatchNormalization(axis=- 1),
        layers.MaxPool2D((2, 2)),
        layers.Dropout(0.2),

        layers.Conv2D(64, (3, 3), padding="same", activation='relu'),
        layers.BatchNormalization(axis=-1),
        layers.MaxPool2D((2, 2)),

        layers.Conv2D(128, (3, 3), padding="same", activation='relu'),
        layers.BatchNormalization(axis=-1),
        layers.MaxPool2D((2, 2)),
        # layers.Dropout(0.3),

        layers.Flatten(),
        layers.Dense(1024, activation='relu'),
        layers.Dense(256, activation='relu'),
        layers.Dense(2, activation='softmax'),
        # layers.Dropout(0.3)
    ])
else: #complete
    BS = 16
    EP = 10
    LR = 0.00001
    model_softmax = models.Sequential([
        layers.Conv2D(32, (3, 3), padding="same", input_shape=(128, 128, 3), activation='relu'),
        layers.BatchNormalization(axis=- 1),
        layers.MaxPool2D((2, 2)),

        layers.Conv2D(64, (3, 3), padding="same", activation='relu'),
        layers.BatchNormalization(axis=-1),
        layers.MaxPool2D((2, 2)),
        layers.Dropout(0.25),

        layers.Conv2D(64, (3, 3), padding="same", activation='relu'),
        layers.BatchNormalization(axis=-1),
        layers.MaxPool2D((2, 2)),

        layers.Conv2D(128, (3, 3), padding="same", activation='relu'),
        layers.BatchNormalization(axis=-1),
        layers.MaxPool2D((2, 2)),
        layers.Dropout(0.3),

        layers.Flatten(),
        layers.Dense(1024, activation='relu'),
        layers.Dense(256, activation='relu'),
        layers.Dense(2, activation='softmax'),
        # layers.Dropout(0.3)
    ])
# print(sigmoid_xtrain[3])
# data_augmentation = tensorflow.keras.Sequential([
#     RandomFlip("horizontal", input_shape=(128,128,3)),
#     RandomZoom(0.3),
#     RandomRotation(0.1),
# ])
datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode="nearest"
)

# model_sigmoid = models.Sequential([
#     layers.Conv2D(16, (3, 3), padding="same", input_shape=(128, 128, 3), activation='relu'),
#     layers.BatchNormalization(axis=-1),
#     layers.MaxPool2D((2, 2)),
#
#     layers.Conv2D(32, (3, 3), padding="same", activation='relu'),
#     layers.BatchNormalization(axis=-1),
#     layers.MaxPool2D((2, 2)),
#     layers.Dropout(0.2),
#
#     layers.Conv2D(64, (3, 3), padding="same", activation='relu'),
#     layers.BatchNormalization(axis=-1),
#     layers.MaxPool2D((2, 2)),
#
#     layers.Conv2D(128, (3, 3), padding="same", activation='relu'),
#     layers.BatchNormalization(axis=-1),
#     layers.MaxPool2D((2, 2)),
#     layers.Dropout(0.2),
#
#     layers.Flatten(),
#     layers.Dense(1024, activation='relu'),
#     layers.Dense(256, activation='relu'),
#     layers.Dense(2, activation='sigmoid'),
#     # layers.Dropout(0.3)
# ])

# model_softmax = models.Sequential([
#     layers.Conv2D(32, (3, 3), padding="same", input_shape=(128, 128, 3), activation='relu'),
#     layers.BatchNormalization(axis=-1),
#     layers.MaxPool2D((2, 2)),
#     layers.Dropout(0.2),
#
#     layers.Conv2D(64, (3, 3), padding="same", activation='relu'),
#     layers.BatchNormalization(axis=-1),
#     layers.MaxPool2D((2, 2)),
#
#     layers.Conv2D(128, (3, 3), padding="same", activation='relu'),
#     layers.BatchNormalization(axis=-1),
#     layers.MaxPool2D((2, 2)),
#     layers.Dropout(0.1),
#
#     layers.Flatten(),
#     layers.Dense(1024, activation='relu'),
#     layers.Dense(256, activation='relu'),
#     layers.Dense(2, activation='softmax'),
# ])

# print("MODEL SIGMOID")
# model_sigmoid.summary()

# model_sigmoid.compile(optimizer=Adam(learning_rate=0.000001),  # SGD=stochastic gradient decent
#                       loss='binary_crossentropy',
#                       metrics=['accuracy'])
#
# # early_stopping = EarlyStopping(monitor='val_loss', patience=3)
# model_sigmoid.fit(datagen.flow(np.array([x[0] for _, x in enumerate(sigmoid_xtrain)]),
#                                np.array([y[1] for _, y in enumerate(sigmoid_xtrain)])), batch_size=64,
#                   epochs=40, validation_data=(
#     np.array([x[0] for _, x in enumerate(sigmoid_xtest)]), np.array([y[1] for _, y in enumerate(sigmoid_xtest)])),
#                   shuffle=True, verbose=1,callbacks=[csv_logger_sigmoid])
# # model_sigmoid.evaluate(np.array([x[0] for _,x in enumerate(sigmoid_xtest)]),np.array([y[1] for _ ,y in enumerate(sigmoid_xtest)]),verbose=1)
#
# model_sigmoid.save('model-anti-spoofing-sigmoid.h5')

print("MODEL SOFTMAX:")
print(f'BS/EP/LR:{BS},{EP},{LR}')
model_softmax.summary()

model_softmax.compile(optimizer=Adam(learning_rate=LR,beta_1=0.9,beta_2=0.999,epsilon=1e-07),
                      loss='binary_crossentropy',
                      metrics=['accuracy'])

early_stopping = EarlyStopping(monitor='val_loss', patience=2)
model_softmax.fit(datagen.flow(np.array([x[0] for _, x in enumerate(softmax_xtrain)]),
                               np.array([y[1] for _, y in enumerate(softmax_xtrain)])),batch_size=BS,
                  epochs=EP, validation_data=(
    np.array([x[0] for _, x in enumerate(softmax_xtest)]), np.array([y[1] for _, y in enumerate(softmax_xtest)])),
                  shuffle=True, verbose=1,callbacks=[csv_logger_softmax])

model_softmax.save('model-anti-spoofing-softmax.h5')
