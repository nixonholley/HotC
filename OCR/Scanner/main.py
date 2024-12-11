import cv2

from utils import get_random_image_file
from edge_detection import edge_detection
from image_to_string import image_to_string

import pytesseract

def main():
    # gets random image file from CardImages library
    im_file = get_random_image_file() # will replace with camera 
    im = cv2.imread(im_file)

    # finds edges of card and creates new image
    im = edge_detection(im)
    
    cv2.imwrite('./temp/image_to_string.jpg', im) #tempS
    
if __name__ == '__main__':
    main()