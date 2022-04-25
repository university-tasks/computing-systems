from pathlib import Path
import os
import argparse

parser = argparse.ArgumentParser(description="overlay face with a mask")
parser.add_argument("-p", "--path", type=str, help="absolute path to the folder with groups of images")
parser.add_argument("-o", "--output", type=str, help="absolute path to the output folder")
args = parser.parse_args()

print(f"PATH TO THE DATA {args.path}")

for group in Path(args.path).iterdir():
    for image in group.iterdir():
        os.system(f"python3 overlay_face_mask.py -p {str(image.absolute())} -o {str(args.output)}")
