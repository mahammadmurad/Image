basic commands
from PIL import Image

img = Image.open('./python.png')

print(img)
print(img.format)
print(img.size)
print(img.mode)
print(dir(img))


Blurimage
from PIL import Image, ImageFilter

img = Image.open('./python.png')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", 'png')


ConverttoGrey
from PIL import Image, ImageFilter

img = Image.open('./python.png')
filtered_img = img.convert('L')
filtered_img.save("grey.png", 'png')
filtered_img.show()

Rotate
from PIL import Image, ImageFilter

img = Image.open('./python.png')
filtered_img = img.convert('L')
crooked = filtered_img.rotate(110)
crooked.save("grey.png", 'png')


Resize
from PIL import Image, ImageFilter

img = Image.open('./python.png')
filtered_img = img.convert('L')
resize  = filtered_img.resize((300,400))
resize.save("grey.png", 'png')

