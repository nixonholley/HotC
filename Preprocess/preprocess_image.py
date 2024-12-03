import cv2
from PIL import Image
from numpy import ones, uint8
import random

def crop(image, x, y, w, h):
    # Define the region of interest (ROI)
    # # x, y: top-left corner coordinates, w, h: width and height of the crop
    # Crop the image
    cropped_image = image[y:y+h, x:x+w]
    return cropped_image

"""
Converts image to grayscale
:param image: image to be converted
:return: grayscale image
"""
def convert_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def adaptive_threshold_image(gray_image):
    return cv2.adaptiveThreshold(gray_image, 200, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 2)

def threshold_image(gray_image):
    _, thresh = cv2.threshold(gray_image, 150, 200, cv2.THRESH_BINARY_INV)
    return thresh

def find_edges(image):
    gray = convert_grayscale(image)
    thresh = threshold_image(gray)

    cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    largest_contour = max(cnts, key=cv2.contourArea)

    # Sort contours by area, largest to smallest
    # sorted_contours = sorted(cnts, key=cv2.contourArea, reverse=True)
    # print(len(sorted_contours))

    # for i, cnt in enumerate(sorted_contours):
    #     x, y, w, h = cv2.boundingRect(cnt)
    #     temp_im = crop(thresh, x, y, w, h)
    #     cv2.imwrite(f'temp/boundingbox{i}.jpg', temp_im)

    x, y, w, h = cv2.boundingRect(largest_contour)
    temp_im = crop(thresh, x, y, w, h)
    cv2.imwrite('temp/boundingbox.jpg', temp_im)

    return crop(image, x, y, w, h)

def remove_noise(image):
    kernel = ones((1,1), uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return image

def preprocess(filename='CardImages/index1.jpg'):
    image_file = filename

    # Read file in
    im = cv2.imread(image_file)

    # Convert to grayscale
    im = convert_grayscale(im)
    cv2.imwrite('temp/gray.jpg', im)

    #oi = find_roi(im)
    cv2.imwrite('temp/roi.jpg', roi)
    # Convert grayscale to b&w
    thresh, im = cv2.threshold(roi, 220, 255, cv2.THRESH_BINARY)

    # Get rid of noise using Guassian
    # im = remove_noise(im)

    return im

if __name__ == '__main__':
    num = random.randint(1, 11)
    im_file = f'CardImages/index{num}.jpg'

    im = cv2.imread(im_file)
    # cv2.imshow('OG Image', im)
    # cv2.waitKey(2000)

    cropped = find_edges(im)

    cv2.imshow('Cropped Image', cropped)
    cv2.waitKey(3000)
