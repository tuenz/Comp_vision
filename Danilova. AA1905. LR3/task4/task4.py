from PIL import Image 
import PIL.ImageOps
from numpy import array
from matplotlib import pyplot as plt

im = Image.open("danilova.jpg")

im_bw = im.convert('L') 
inverted_im = PIL.ImageOps.invert(im_bw)

im_bw_array = array(im_bw)
inverted_im_array = array(inverted_im)

plt.figure(figsize=(10,6))
plt.subplot(2,2,1)
plt.title("Исходное полутоновое изображение")
plt.imshow(im_bw, cmap='gray')
plt.subplot(2,2,2)
plt.title("Инвертированное изображение")
plt.imshow(inverted_im,  cmap='gray')
plt.subplot(2,2,3)
plt.title("Гистограмма 1")
plt.hist(im_bw_array.flatten(),128)
plt.subplot(2,2,4)
plt.title("Гистограмма 2")
plt.hist(inverted_im_array.flatten(),128)
plt.savefig("danilova_hist.jpg")
plt.show()



