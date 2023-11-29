from PIL import Image
from numpy import array
from matplotlib import pyplot as plt
import numpy as np
from numpy import uint8

im = Image.open("danilova.jpg")
im_bw = im.convert('L') 
im_bw.save("danilova_l_task6.jpg")
#исходное полутоновое изображение
im_bw_array = array(im_bw)

imh, b = np.histogram(im_bw_array.flatten(), 256, normed = True)
#imh статистический результат каждого интервала = ось y
#b=bins: Массив, хранящий начальную точку каждого статистического интервала. 
cdf = imh.cumsum()
#расчет кумулятивной функции по заданной оси
cdf = 255*cdf/cdf[-1]
#нормировка
im_new = np.interp(im_bw_array.flatten(), b[:-1], cdf)
#интерполяция функции
#1 пар-р - координаты в которых вычисляются интерполированные значения.
#2 пар-р - координаты независимых переменных, по которым вычисл интерп
#3 пар-р - координаты зависимых переменных, по которым вычисл интерп
im_new = im_new.reshape(im_bw_array.shape)
#reshape() изменяет форму массива без изменения его данных

im_task6 = Image.fromarray(uint8(im_new))
im_task6.save("danilova_task6.jpg")
#построение графиков
plt.figure(figsize=(14,7))
plt.subplot(2,2,1)
plt.title("Исходное полутоновое изображение")
plt.imshow(im_bw, cmap='gray')

plt.subplot(2,2,2)
plt.title("Модифицированное изображение")
plt.imshow(im_task6, cmap='gray')

plt.subplot(2,2,3)
plt.title("Гистограмма 1")
plt.hist(im_bw_array.flatten(),128, [0,255])

plt.subplot(2,2,4)
plt.title("Гистограмма 2")
plt.hist(im_new.flatten(), 128, [0,255])
plt.savefig("danilova_hist_task6.jpg")
plt.show()