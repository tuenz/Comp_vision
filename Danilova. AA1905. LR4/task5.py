import numpy as np
import cv2
import matplotlib.pyplot as plt

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
        # cv2.circle(image, center_coordinates, radius, color, thickness)
        # thickness -1 pxзаполнит форму круга заданным цветом.
        cv2.circle(image, (x, y), 8, (255, 0, 0), -1)
    print('Количество углов:', len(corners))
    return image, len(corners) 


original = cv2.imread('danilova51.jpg')
original, corners = get_corners(original)
plt.title('Количество углов на изображении равно ' + str(corners))
plt.imshow(cv2.cvtColor(original,cv2.COLOR_BGR2RGB))
plt.savefig('danilova52.jpg')
plt.show()