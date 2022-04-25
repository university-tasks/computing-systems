import cv2
import dlib
import numpy as np
import os
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="overlay face with a mask")
parser.add_argument("-p", "--path", type=str, help="absolute path to an image")
parser.add_argument("-o", "--output", type=str, help="absolute path to the output folder")

args = parser.parse_args()
print(f"PATH TO AN IMAGE {args.path}")
print(f"OUTPUT FOLDER: {args.output}")

color_black = (0, 0, 0)

# Loading the image and resizing, converting it to grayscale
img = cv2.imread(args.path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Initialize dlib's face detector
detector = dlib.get_frontal_face_detector()

faces = detector(gray, 1)

# printing the coordinates of the bounding rectangles
print(faces)
print("Number of faces detected: ", len(faces))

predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

for face in faces:
    landmarks = predictor(gray, face)

    points = []
    for i in range(1, 16):
        point = [landmarks.part(i).x, landmarks.part(i).y]
        points.append(point)

    mask = [((landmarks.part(29).x), (landmarks.part(29).y))]

    fmask = points + mask
    fmask = np.array(fmask, dtype=np.int32)

    img2 = cv2.polylines(img, [fmask], True, color_black, thickness=2, lineType=cv2.LINE_8)

    # Using Python OpenCV – cv2.fillPoly() method to fill mask
    # change parameter [mask_type] and color_type for various combination
    img3 = cv2.fillPoly(img2, [fmask], color_black, lineType=cv2.LINE_AA)
    img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

# cv2.imshow("image with mask", img3)
# cv2.waitKey(0)

parentDir = Path(args.path).parent.name
imagename = Path(args.path).name
outputPath = str(Path(os.path.join(args.output, parentDir, imagename)).absolute())

if not os.path.exists(Path(os.path.join(args.output, parentDir)).absolute()):
    os.mkdir(str(Path(os.path.join(args.output, parentDir)).absolute()))

print("Saving output image to", outputPath)
cv2.imwrite(outputPath, img3)


# cv2.waitKey(0)
# cv2.destroyAllWindows()
