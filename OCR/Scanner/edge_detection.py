import cv2
import numpy as np

def init_trackbars():
    def on_change(value):
        pass

    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 360, 240)
    cv2.createTrackbar("Threshold1", "Trackbars", 100, 255, on_change)
    cv2.createTrackbar("Threshold2", "Trackbars", 89, 255, on_change)

def valTrackbars():
    threshold1 = cv2.getTrackbarPos("Threshold1", "Trackbars")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Trackbars")
    return (threshold1, threshold2)

def reorder_points(points):
    points = points.reshape((4,2))
    new_points = np.zeros((4, 1, 2), dtype=np.int32)

    _sum = points.sum(1)
    new_points[0] = points[np.argmin(_sum)]
    new_points[3] = points[np.argmax(_sum)]

    diff = np.diff(points, axis=1)
    new_points[1] = points[np.argmin(diff)]
    new_points[2] = points[np.argmax(diff)]

    return new_points

def warp_image(im, roi, im_width, im_height):
    pts1 = np.float32(roi)
    pts2 = np.float32([[0,0], [im_width, 0], [0, im_height], [im_width, im_height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    return cv2.warpPerspective(im, matrix, (im_width, im_height))

def get_largest_contour(contours):
    largest = np.array([])
    max_area = 0
    for c in contours:
        area = cv2.contourArea(c)
        if area > 5000:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            if area > max_area and len(approx) == 4:
                largest = approx
                max_area = area
    return largest

def edge_detection(im, im_width = 480, im_height = 640, edit=False):
    init_trackbars()

    # resize image
    im = cv2.resize(im, (im_width, im_height))

    # convert to grayscale
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # add gaussian blur
    im_blur = cv2.GaussianBlur(im_gray, (5,5), 1)

    # loop to adjust Trackbar values
    while True:
        # get track bar values
        thresh = valTrackbars()

        # apply canny blur
        im_threshold = cv2.Canny(im_blur, thresh[0], thresh[1])

        kernel = np.ones((5,5))
        # apply dilation
        im_dial = cv2.dilate(im_threshold, kernel, iterations=2)
        im_erode = cv2.erode(im_dial, kernel, iterations=1)

        # find contours
        contours, hierarchy = cv2.findContours(im_erode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        roi = get_largest_contour(contours)
        roi = reorder_points(roi)
        new_im = warp_image(im, roi, im_width, im_height)
        new_im = new_im[20:new_im.shape[0]-20, 20:new_im.shape[1]-20] 
        cv2.imshow('Image', new_im)
        
        # press q to break loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    return new_im