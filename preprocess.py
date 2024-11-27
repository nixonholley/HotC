import cv2
from PIL import Image
import pytesseract
from numpy import ones, uint8

"""
Converts image to grayscale
:param image: image to be converted
:return: grayscale image
"""
def convert_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    kernel = ones((1,1), uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return image



image_file = "CardImages/index1.jpg"

#im = Image.open(image_file)
im = cv2.imread(image_file)
#cv2.imshow("Original Image", im)
#cv2.waitKey(1000)

gray_im = convert_grayscale(im)
cv2.imwrite('temp/gray.jpg', gray_im)

thresh, bw_im = cv2.threshold(gray_im, 220, 255, cv2.THRESH_BINARY)
cv2.imwrite('temp/bw.jpg', bw_im)

no_noise_im = remove_noise(bw_im)
cv2.imwrite('temp/no_noise.jpg', no_noise_im)