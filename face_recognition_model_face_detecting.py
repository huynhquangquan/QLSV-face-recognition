import cv2
import face_recognition
import pickle
import os

folderPath = 'images'
pathList = os.listdir(folderPath)

imgList = []
student = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    student.append(os.path.splitext(path)[0])

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img)
        if len(encodings) > 0:
            encode = encodings[0]
            encodeList.append(encode)
        else:
            print("No face detected in the image.")
    return encodeList


encodeListKnown = findEncodings(imgList)
encodeListKnownIds = (encodeListKnown, student)

file = open('model-student.p', 'wb')
pickle.dump(encodeListKnownIds, file)
file.close()
print(encodeListKnownIds)
print("File saved")
