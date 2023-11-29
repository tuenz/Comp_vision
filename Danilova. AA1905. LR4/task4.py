from PIL import Image
from scipy.ndimage import sobel, gaussian_filter
import matplotlib.pyplot as plt
from numpy import array, zeros, sqrt

# стандартное отклонение
sigma = 5
# чтение изображения
im = Image.open('danilova41.jpg')
im.show()
m_im = array(im.convert('L'))
# массивы для расчета производных
m_imx = zeros(m_im.shape)
m_imy = zeros(m_im.shape)
# оператор собеля
# Производная по х
sobel(m_im, 1, m_imx)
# Производная по у
sobel(m_im, 0, m_imy)
# Величина градиента
m = sqrt(m_imx*m_imx + m_imy*m_imy)
# результаты на графиках
plt.figure(figsize=(9, 5))
plt.gray()
plt.subplots_adjust(wspace=0.3, hspace=0.4)
plt.subplot(2,2,1)
plt.title('Собель. Произв. по х')
plt.imshow(m_imx)
plt.subplot(2,2,2)
plt.title('Собель. Произв. по у')
plt.imshow(m_imy)
plt.subplot(2,2,3)
plt.title('Собель. Границы')
plt.imshow(m)
plt.subplot(2,2,4)
plt.title('Собель. Гистограмма')
plt.hist(m.flatten(),128)
plt.savefig('danilova42.jpg')
plt.show()

# оператор гаусса
m_imx = zeros(m_im.shape)
m_imy = zeros(m_im.shape)
gaussian_filter(m_im, (sigma, sigma), (0, 1), m_imx)
gaussian_filter(m_im, (sigma, sigma), (1, 0), m_imy)
m = sqrt(m_imx * m_imx + m_imy * m_imy)

plt.figure(figsize=(9, 5))
plt.gray()
plt.subplots_adjust(wspace=0.3, hspace=0.4)
plt.subplot(2,2,1)
plt.title('Гаусс. Произв. по х')
plt.imshow(m_imx)
plt.subplot(2,2,2)
plt.title('Гаусс. Произв. по у')
plt.imshow(m_imy)
plt.subplot(2,2,3)
plt.title('Гаусс. Границы')
plt.imshow(m)
plt.subplot(2,2,4)
plt.title('Гаусс. Гистограмма')
plt.hist(m.flatten(),128)
plt.savefig('danilova43.jpg')
plt.show()