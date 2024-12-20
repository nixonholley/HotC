import random
import cv2

def get_random_image_file():    
    num = random.randint(12, 14)
    im_file = f'./OCR/CardImages/index{num}.jpg'
    return im_file

def select_roi(im, region):
    roi = cv2.selectROI(f"Select {region}", im, showCrosshair=True, fromCenter=False)

    x, y, w, h = map(int, roi)
    cropped_image = im[y:y+h, x:x+w]

    print(f'x: {x}, y: {y}, w: {w}, h: {h}')

    cv2.imwrite('./temp/roi.jpg', cropped_image)

    return cropped_image

def init_trackbars():
    def on_change(value):
        pass

    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 360, 240)
    cv2.createTrackbar("Threshold1", "Trackbars", 167, 255, on_change)
    cv2.createTrackbar("Threshold2", "Trackbars", 121, 255, on_change)

def valTrackbars():
    threshold1 = cv2.getTrackbarPos("Threshold1", "Trackbars")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Trackbars")
    return (threshold1, threshold2)

class Card:
    def __init__(self, id = 'N/A',  name='N/A', text = 'N/A'):
        self.name = name
        self.text = text
        self.id = id

    def __str__(self):
        return f'Card[{self.name}]:[{self.id}]\n-Text:\n{self.text}'
