from PIL import Image, ImageEnhance
from numpy import array
from matplotlib import pyplot as plt

def get_num(str):
    while 1:
      try:
        val = float(input('\nВведите ' + str + ': '))
        if val>4 or val <= 1:
            print('Пожалуйста, вводите только числа в диапазоне (1,4].')
        else:
            return val
      except ValueError:  
        print('Пожалуйста, вводите целые или дробные числа.')

im = Image.open("danilova.jpg")
im_bw = im.convert('L') 
im_bw_array = array(im_bw)

num = get_num('коэффициент изменения яркости в диапазоне (1,4]')
enhancer = ImageEnhance.Brightness(im_bw)
im_bw_bright = enhancer.enhance(num)
im_bw_bright_array = array(im_bw_bright)

plt.figure(figsize=(14,7))
plt.subplot(2,2,1)
plt.title("Исходное полутоновое изображение")
plt.imshow(im_bw, cmap='gray')
plt.subplot(2,2,2)
plt.title("Более яркое изображение")
plt.imshow(im_bw_bright, cmap='gray')
plt.subplot(2,2,3)
plt.title("Гистограмма 1")
plt.hist(im_bw_array.flatten(),128, [0,255])
plt.subplot(2,2,4)
plt.title("Гистограмма 2")
plt.hist(im_bw_bright_array.flatten(),128, [0,255])
plt.savefig("danilova_hist_task5.jpg")
plt.show()


