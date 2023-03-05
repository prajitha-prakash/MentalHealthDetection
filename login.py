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

attendance_pic_path=r"C:\mental\\"

import cv2

def emotion_finding():
        try:
            import cv2
            print("fir")
            webcam = cv2.VideoCapture(0)
            key = cv2.waitKey(1)

            check, frame = webcam.read()



