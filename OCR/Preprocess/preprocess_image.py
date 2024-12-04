from utils import find_edges, get_random_image_file
import cv2

def crop_image_borders(image_file : str):

    im = cv2.imread(image_file)
    # cv2.imshow('OG Image', im)
    # cv2.waitKey(2000)
    cropped = find_edges(im)

    cv2.imshow('Cropped Image', cropped)
    cv2.waitKey(3000)

def main():
    im_file = get_random_image_file()
    cropped = crop_image_borders(im_file)

if __name__ == '__main__':
    main()
