import sys
import numpy as np


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

attendance_pic_path=r"C:\Users\project\mental_health\static\\"

import cv2

def emotion_finding():
        try:
            import cv2
            print("fir")
            webcam = cv2.VideoCapture(0)
            key = cv2.waitKey(1)

            check, frame = webcam.read()

            import time

            filename = "y22.jpg"
            cv2.imwrite(attendence_pic_path + filename, img=frame)
            webcam.release()
            # img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
            # img_new = cv2.imshow("Captured Image", img_new)
            print("kkk")
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            print("Processing image...")

            webcam.release()
            cv2.destroyAllWindows()

            # photo = attendence_pic_path + filename
            print("jjjjjjjjjjjjjj")

            import base64

            # photo="c://2.jpg"

            unknown_image = face_recognition.load_image_file(attendence_pic_path + filename)
            # b_img = face_recognition.load_image_file(img)
            m = len(face_recognition.face_encodings(unknown_image))
            print("printing results")
            for a in range(m):
                ####emotion finding
                import requests

                import cv2
                model = Sequential()

                model.add(
                    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1)))
                model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
                model.add(MaxPooling2D(pool_size=(2, 2)))
                model.add(Dropout(0.25))

                model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
                model.add(MaxPooling2D(pool_size=(2, 2)))
                model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
                model.add(MaxPooling2D(pool_size=(2, 2)))
                model.add(Dropout(0.25))

                model.add(Flatten())
                model.add(Dense(1024, activation='relu'))
                model.add(Dropout(0.5))
                model.add(Dense(7, activation='softmax'))

                model.load_weights(r'C:\Users\project\mental_health\model.h5\\')

                # prevents openCL usage and unnecessary logging messages
                cv2.ocl.setUseOpenCL(False)
                # dictionary which assigns each label an emotion (alphabetical order)
                emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral",
                                5: "Sad",
                                6: "Surprised"}

                frame = cv2.imread(attendence_pic_path + filename)

                facecasc = cv2.CascadeClassifier(
                    r'C:\mental\haarcascade_frontalface_default.xml')
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = facecasc.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y - 50), (x + w, y + h + 10), (255, 0, 0), 2)
                    roi_gray = gray[y:y + h, x:x + w]
                    cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1),
                                                 0)
                    prediction = model.predict(cropped_img)
                    # print(prediction)
                    maxindex = int(np.argmax(prediction))
                    print(emotion_dict[maxindex])
                    res_emo = emotion_dict[maxindex]
                    print("Detected Emotion  :  ", res_emo)
            return "ok"
            except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            # break


while True:
    emotion_finding()



