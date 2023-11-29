from PIL import Image, ImageDraw
# чтение изображений
foreground = Image.open('gram.jpg') #передний план
background = Image.open('desk.jpg') #фон
# отображение изображений
foreground.show()
background.show()

# создание миниатюры из переднего плана с сохранением пропорций
foreground_copy = foreground.copy()
foreground_copy.thumbnail((200,200))
# созданий копии изображения-фона
background_copy = background.copy()

#создание маски - окружности
mask1 = Image.new("L", foreground_copy.size, 0)
draw = ImageDraw.Draw(mask1)
draw.ellipse((0, 0, 200, 200), fill=125)
mask1.show()
mask1.save('mask1.jpg')
#создание маски из картинки кота
mask2 = Image.open('cat.jpg').resize(foreground_copy.size).convert('L')
mask2.show()
mask2.save('mask2.jpg')

# размеры изображений
w_foreground, h_foreground = foreground_copy.size
w_background, h_background = background_copy.size
# рассчитываем координаты центра
center = (round((w_background-w_foreground)/2),round((h_background-h_foreground)/2))

# накладываем изображение в центр с маской
background_copy.paste(foreground_copy, center, mask1)
# отображаем и сохраняем результат
background_copy.show()
background_copy.save('danilova21.jpg')

background_copy = background.copy()
background_copy.paste(foreground_copy, center, mask2)
background_copy.show()
background_copy.save('danilova22.jpg')
