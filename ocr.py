import pytesseract as tess
from PIL import Image

im = Image.open("right.jpg")

text = tess.image_to_string(im)

i = 0
last = i
for x in text:
    if x == 'o':
        x = ' '
    if x == ')':
        last = i
    i = i + 1

newtext = text[:last].split(')')
newtext2 = []
temp = []
dic = ()
for x in newtext:
    temp.clear()
    # print(x)
    x = x.replace('\n', '')
    asd = x.split(' ', 1)
    # print(asd)
    temp.append(asd[0])
    temp.append(asd[1].split('('))
    print(temp)
    newtext2.append(temp[:])

print(newtext2)
