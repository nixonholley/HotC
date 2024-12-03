import cv2
import Preprocess.preprocess_image as preprocess_image
import random

# image = cv2.imread('CardImages/index2.jpg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(gray, (7,7), 0)
# thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,13))
# dilate = cv2.dilate(thresh, kernel, iterations=1)
# cv2.imwrite('temp/blurrrrr.jpg', dilate)

num = random.randint(1, 11)
im_file = f'CardImages/index{num}.jpg'
im = preprocess_image.preprocess(im_file)
cv2.imshow("image", im)
cv2.waitKey(0)

# cnts = cv2.findContours(im, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# if len(cnts) == 2:
#     cnts = cnts[0]
# else:
#     cnts = cnts[1]

# for c in cnts:
#     x,y,w,h = cv2.boundingRect(c)
#     cv2.rectangle(im, (x,y), (x+w, y+h), (36, 255, 12), 2)
# cv2.imwrite('temp/bbox.png', im)