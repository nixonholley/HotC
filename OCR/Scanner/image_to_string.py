import cv2
import pytesseract

def image_to_string(im):
    text = pytesseract.image_to_string(im)
    return text
    