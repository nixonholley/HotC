import cv2
import random

"""
Returns cropped image based on parameters
:param x,y: top-left corner coordinates
:param w,h: width and height of the crop
:return: cropped image
"""
def crop(image, x, y, w, h):
    cropped_image = image[y:y+h, x:x+w]
    return cropped_image

"""
Converts image to grayscale
:param image: image to be converted
:return: grayscale image
"""
def convert_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

"""
Uses adaptive thresholding on image
ADJUST USING SLIDERS FROM VIDEO
"""
def adaptive_threshold_image(gray_image):
    return cv2.adaptiveThreshold(gray_image, 200, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 2)

"""
Thresholds image
"""
def threshold_image(gray_image):
    _, thresh = cv2.threshold(gray_image, 150, 200, cv2.THRESH_BINARY_INV)
    return thresh


"""
Finds the largest contour to crop the image from edges
"""
def find_edges(image):
    gray = convert_grayscale(image)
    thresh = threshold_image(gray)

    cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    largest_contour = max(cnts, key=cv2.contourArea)

    x, y, w, h = cv2.boundingRect(largest_contour)
    temp_im = crop(thresh, x, y, w, h)
    cv2.imwrite('temp/boundingbox.jpg', temp_im)

    return crop(image, x, y, w, h)

"""
Removes noise from image
"""
def remove_noise(image):
    kernel = ones((1,1), uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return image

def get_random_image_file():    
    num = random.randint(1, 11)
    im_file = f'CardImages/index{num}.jpg'
    return im_file
