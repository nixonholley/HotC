import cv2
import numpy as np

from utils import get_random_image_file, edge_detection




def main():
    im_file = get_random_image_file()
    im = cv2.imread(im_file)

    # finds edges of card and creates new image
    im = edge_detection(im)

if __name__ == '__main__':
    main()
