import cv2

from utils import get_random_image_file, select_roi
from edge_detection import edge_detection
from image_to_string import image_to_string

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" # how to add tesseract to docker

def main():
    # gets random image file from CardImages library
    im_file = get_random_image_file() # will replace with camera 
    im = cv2.imread(im_file)

    # finds edges of card and creates new image
    im = edge_detection(im)

    # OCR
    text = image_to_string(im)
    print(text)
    
if __name__ == '__main__':
    main()