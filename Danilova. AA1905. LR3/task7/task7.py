from numpy import array
from PIL import Image
import cv2
from matplotlib import pyplot as plt
from skimage.util import random_noise

im = cv2.imread('danilova_cat.jpg', 1)
#загрузка изображения
im_array = array(im)
sigma = 0.5
n = random_noise(im_array, mode='gaussian', seed=None, var=sigma*sigma)
#Функция добавления случайных шумов различных типов к изображению
#Если значение seed равно None, используется синглтон numpy.random.Generator
#var Дисперсия случайного распределения
#возвращает значения [0,1]

cv2.imwrite('danilova_task7.jpg', 255*n)
#сохранение изображения

#построение гистограмм
pim1 = Image.open('danilova_cat.jpg')
im1 = array(pim1)
pim2 = Image.open('danilova_task7.jpg')
im2 = array(pim2)

plt.figure(figsize=(14,7))
plt.subplot(2,2,1)
plt.title("Исходное изображение")
plt.imshow(pim1)

plt.subplot(2,2,2)
plt.title("Модифицированное изображение")
plt.imshow(pim2)

plt.subplot(2,2,3)
plt.title("Гистограмма 1")
plt.hist(im1.flatten(),128)

plt.subplot(2,2,4)
plt.title("Гистограмма 2")
plt.hist(im2.flatten(),128)
plt.savefig("danilova_hist_task7.jpg")
plt.show()
