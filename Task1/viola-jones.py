import cv2 as cv
from os import path
import matplotlib.pyplot as plt
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description="overlay face with a mask")
parser.add_argument("-i", "--image", type=str)

args = parser.parse_args()

image = cv.imread(args.image)
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')


detected_faces = face_cascade.detectMultiScale(image)
for (column, row, width, height) in detected_faces:
    cv.rectangle(image,(column, row),(column + width, row + height),(255, 0,0 ),3)    

plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
plt.axis("off")
plt.show()