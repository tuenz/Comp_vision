from PIL import Image
from scipy.ndimage import gaussian_filter
from numpy import array, uint8
from matplotlib import pyplot as plt

im = Image.open("danilova8.jpg")
im_bw = im.convert('L') 
#исходное полутоновое изображение
im_array = array(im_bw)

# размытие изображения по Гауссу 
# с коэф-ом размытия 10
im1 = gaussian_filter(im_array, 10)
pim1 = Image.fromarray(uint8(im1))
# размытие изображения по Гауссу 
# с коэф-ом размытия 20
im2 = gaussian_filter(im_array, 20)
pim2 = Image.fromarray(uint8(im2))

# отображение изолиний и изображений
plt.figure(figsize=(14,7))
plt.subplot(3,2,1)
plt.title("Исходное изображение", fontsize=10)
plt.imshow(im_bw, cmap='gray')

plt.subplot(3,2,2)
plt.title("Изолинии исходного изображения", fontsize=10)
plt.contour(im_array, origin='image', cmap='gray')

plt.subplot(3,2,3)
plt.title("Изображение с размытием 10", fontsize=10)
plt.imshow(pim1, cmap='gray')

plt.subplot(3,2,4)
plt.title("Изолинии изображения с размытием 10", fontsize=10)
plt.contour(im1, origin='image', cmap='gray')

plt.subplot(3,2,5)
plt.title("Изображение с размытием 20", fontsize=10)
plt.imshow(pim2, cmap='gray')

plt.subplot(3,2,6)
plt.title("Изолинии изображения с размытием 20", fontsize=10)
plt.contour(im2, origin='image', cmap='gray')

plt.subplots_adjust(left=0.1, bottom=0.1,right=0.9,
                    top=0.9, wspace=0.3, hspace=0.3)
plt.savefig("danilova_hist_task8.jpg")
plt.show()
