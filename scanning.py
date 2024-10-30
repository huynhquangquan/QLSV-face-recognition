# FACE SCANNING SAMPLES COMPLETED
import cv2
import os
import time # Thêm dòng này để import thư viện time

def scanning(base_name,choice):
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
    count = 0 #images id
    # # import các images từ folder
    scan_location_for_fr = 'imgs_factory/scanning'
    # imgPathList = os.listdir(imagePath)
    # # print(imgPathList) # Kiểm tra xem trong folder có images nào
    # imgList = []
    # studentIds = []
    #
    # for path in imgPathList:
    #     imgList.append(cv2.imread(os.path.join(imagePath,path)))
    #     studentIds.append(os.path.splitext(path)[0])
    #     # print(path) # In toàn bộ
    # print(studentIds) # elonmusk.jpg, trong đó mảng[0].mảng[1]

    def create_new_directory(base_path, base_name):
        counter = 0
        new_dir_path = os.path.join(base_path, f"{counter}_{base_name}") # Tạo path
        while os.path.exists(new_dir_path): # Xét Path liệu đã tồn tại qua .exists
            # Thêm số vào sau tên thư mục
            counter += 1
            new_dir_path = os.path.join(base_path, f"{counter}_{base_name}")

        os.makedirs(new_dir_path) # Tạo folder mới
        return new_dir_path


    # base_name = (input("Nhập tên sinh viên: ")) # Default name cho folder mới
    new_dir_path = create_new_directory(scan_location_for_fr, base_name) # Tạo folder mới vào Path được chỉ định

    while True:
        success, frame = cap.read()
        if not success:
            print("Frame is empty")
            break
        # gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) # Convert the frame to grayscale
        faces = face_detector.detectMultiScale(frame, 1.3, 5) # Use the grayscale frame for face detection
        for (x, y, w, h) in faces:
            # image_detection = gray[y:y+h, x:x+w] # Extract the face region from the grayscale frame
            # image_detection = cv2.resize(frame[y:y+h, x:x+w], (280,280)) # CNN
            image_detection = cv2.resize(frame[y-0:y+h-0, x-0:x+w-0], (128, 128)) # Corrected
            image_path = os.path.join(new_dir_path, f'{base_name}_{count}.jpg')
            cv2.imwrite(image_path, image_detection)
            cv2.rectangle(frame, (x-0, y-0), (x+w-0, y+h-0), (128,155,0), 3) # Corrected
            count += 1
        cv2.imshow('SAVING_IMGS_FOR_DETECTION', frame)
        if cv2.waitKey(1) & 0xFF == 27:
             break

    cap.release()
    cv2.destroyAllWindows()
