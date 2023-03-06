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



