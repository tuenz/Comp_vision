import numpy as np
import cv2

def get_corners(image):
    # конвертирихображение в оттенки серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # находим углы с помощью метода goodFeaturesToTrack
    corners = cv2.goodFeaturesToTrack(gray, 60, 0.05, 40, useHarrisDetector=True)
    # преообразуем массив с плавающейточкой в целочисленный 
    corners = np.int0(corners)
    for corner in corners:
        # ravel - возврат непрерывного сведенного массива
        x, y = corner.ravel()  # считываем координаты
        cv2.circle(image, (x, y), 8, (255, 0, 0), -1)
    return image, len(corners) 

original = cv2.imread('danilova71.jpg')
cv2.namedWindow('Original', cv2.WINDOW_AUTOSIZE)
cv2.imshow('Original', original)
result, corners = get_corners(original)

# находим контур объекта
original_0 = cv2.imread('danilova71.jpg', 0)
contours, hierarchy = cv2.findContours(original_0, 1, 2)
cnt = contours[0]
# находим моменты изображения
M = cv2.moments(cnt)
# находим центр масс
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])
cv2.circle(result, (cx, cy), 10, (0, 0, 0), -1)

# SIFT
gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
sift = cv2.SIFT_create()
sift_s = sift.detect(gray,None)
result = cv2.drawKeypoints(result,sift_s,result)

cv2.namedWindow('Result', cv2.WINDOW_AUTOSIZE)
cv2.imshow('Result', result)
cv2.imwrite('danilova72.jpg', result)
cv2.waitKey(0)
