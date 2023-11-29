from skimage import io, filters, measure
from scipy import ndimage
from matplotlib import pyplot as plt
import cv2

# чтение изображения
im = io.imread('danilova61.jpg', as_gray=True)
imm = cv2.imread('danilova61.jpg')
#подсчет количества объектов
val = filters.threshold_otsu(im)
img = ndimage.binary_fill_holes(im < val)
labels = measure.label(img)
print('Количество объектов: ', labels.max())
# отображение результатов
plt.subplot(1,2,1)
plt.title('Исходное изображение')
plt.imshow(cv2.cvtColor(imm, cv2.COLOR_BGR2RGB))
plt.subplot(1,2,2)
plt.title('Количество объектов: ' + str(labels.max()))
plt.imshow(img, cmap='gray')
plt.savefig('danilova62.jpg')
plt.show()
