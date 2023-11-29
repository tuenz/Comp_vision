import cv2
from matplotlib import pyplot as plt
# чтение изображения
img = cv2.imread('danilova31.jpg')
# гауссово размытие
blur_img = cv2.GaussianBlur(img, (35,35),0,0)
# сохранение изображения
cv2.imwrite('danilova32.jpg', blur_img)
# вычитание изображений
res = img*3.5 - blur_img*2.5
cv2.imwrite('danilova33.jpg', res)

# перевод изображения в оттенки серого
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('danilova34.jpg', gray_img)
# гауссово размытие
blur_gray_img = cv2.GaussianBlur(gray_img, (35,35),0,0)
cv2.imwrite('danilova35.jpg', blur_gray_img)
# вычитание изображений
res2= gray_img - blur_gray_img
cv2.imwrite('danilova36.jpg', res2)

# отображение результатов
plt.figure(figsize=(9, 3))
plt.subplot(1,3,1)
plt.title('Исходное изображение')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(1,3,2)
plt.title('Размытое изображение')
plt.imshow(cv2.cvtColor(blur_img, cv2.COLOR_BGR2RGB))
plt.subplot(1,3,3)
plt.title('Результат')
ress=cv2.imread('danilova33.jpg')
plt.imshow(cv2.cvtColor(ress, cv2.COLOR_BGR2RGB))
plt.savefig('danilova37.jpg')

plt.figure(figsize=(9, 3))
plt.gray()
plt.subplot(1,3,1)
plt.title('Исходное полутоновое')
plt.imshow(gray_img)
plt.subplot(1,3,2)
plt.title('Размытое полутоновое')
plt.imshow(blur_gray_img)
plt.subplot(1,3,3)
plt.title('Результат')
plt.imshow(res2)
plt.savefig('danilova38.jpg')
plt.show()
    


