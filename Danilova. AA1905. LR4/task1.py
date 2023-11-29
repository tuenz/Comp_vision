from PIL import Image
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
# размеры изображений
w_foreground, h_foreground = foreground_copy.size
w_background, h_background = background_copy.size

# рассчитываем координаты центра
center = (round((w_background-w_foreground)/2),round((h_background-h_foreground)/2))
# задаем произвольные координаты
rand = (100,100)
# накладываем изображение в центр
background_copy.paste(foreground_copy, center)
# отображаем результат
background_copy.show()
# сохраняем результат
background_copy.save('danilova11.jpg')

# накладываем изображение в произвольную координату
background_copy = background.copy()
background_copy.paste(foreground_copy, rand)
background_copy.show()
background_copy.save('danilova12.jpg')

