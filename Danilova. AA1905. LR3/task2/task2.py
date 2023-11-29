from PIL import Image

def get_num(str, max):
    while 1:
      try:
        val = int(input('\nВведите ' + str + ': '))
        if val<=0:
            print('Пожалуйста, вводите только положительные числа.')
        elif val>=max:
            print('Введенный размер должен быть меньше исходного.')
        else:
            return val
      except ValueError:  
        print('Пожалуйста, вводите только целые числа.')


im = Image.open("danilova.jpg")
im.show()
w, h = im.size
print("\nРазмер исходного изображения в пикселях: ", w, "x", h) 
new_w = get_num ('новую ширину для миниатюры', w)
new_h = get_num ('новую высоту для миниатюры', h)

im.thumbnail((new_w, new_h))
print("\nРазмер миниатюр в пикселях: ", im.size)
im.save("danilova_thumbnail.jpg", "JPEG")
im.show()
im_bw = im.convert('L')     
im_bw.save("danilova_thumbnail_bw.jpg", "JPEG")
im_bw.show()