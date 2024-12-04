import cv2
from Preprocess.utils import find_edges

def crop_image_borders(image_file : str):

    im = cv2.imread(image_file)
    # cv2.imshow('OG Image', im)
    # cv2.waitKey(2000)
    cropped = find_edges(im)

    cv2.imshow('Cropped Image', cropped)
    cv2.waitKey(3000)

def main():
    crop

if __name__ == '__main__':
    main()
