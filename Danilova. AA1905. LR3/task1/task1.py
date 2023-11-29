from PIL import Image
im = Image.open("danilova.jpg")
print("Имя файла или путь к исходному файлу: ", im.filename)
print("\nФормат исходного файла: ", im.format)
print("\nРазмер изображения в пикселях: ", im.size) 
print("\nРежим изображения: ", im.mode)
print("\nТаблица цветовой палитры, если есть: ", im.palette)
print("\ndpi:", im.info['dpi'])



