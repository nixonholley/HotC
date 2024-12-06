import cv2
import numpy as np

from utils import get_random_image_file, edge_detection




def main():
    im_file = get_random_image_file()
    im = cv2.imread(im_file)

    edge_detection(im)
    # apply dilation

    # apply erosion

    #find all countours
    pass

if __name__ == '__main__':
    main()
