# Sample folder và ma trận model img cho face_recognition
# import sys
# sys.path.append('/path/to/your/module/directory')
#
# import your_module
import numpy as np
import cv2
import os
from PIL import Image

TRAIN_DATA = 'datasets/traindata'
TEST_DATA = 'datasets/testdata'

xtrain = [] # Ma trận
ytrain = [] # Nhãn
dict = {'elonmusk': [1,0,0,0,0], 'hoailinh': [0,1,0,0,0], 'obama': [0,0,1,0,0], 'quan': [0,0,0,1,0], 'sontung': [0,0,0,0,1]}

for i in os.listdir(TRAIN_DATA):
    i_path = os.path.join(TRAIN_DATA,i)
    list_filename_path = []
    for filename in os.listdir(i_path):
        filename_path = os.path.join(i_path, filename) # Path cuối cùng dẫn đến thư viện IMG cần thiết (images/posName)
        label = filename_path.split('\\')[1] # Name nhận diện
        img = np.array(Image.open(filename_path)) # Dàn ma trận của Img
        list_filename_path.append((img, dict[label])) #để in ra tên folder chứa images

    xtrain.extend(list_filename_path) # Tổng các ma trận của các Imgs trong file Images

print(list_filename_path)

#TRAIN_DATA: images, i_path: images/posName, filename_path: images/posName/images_{}.jpg
