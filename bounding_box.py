import cv2

image = cv2.imread('CardImages/index2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7,7), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,13))
dilate = cv2.dilate(thresh, kernel, iterations=1)
cv2.imwrite('temp/blurrrrr.jpg', dilate)