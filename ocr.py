import pytesseract as tess

tess.pytesseract.tesseract_cmd = r'C:\Users\Johnson Minz\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image

im = Image.open("right.jpg")

text = tess.image_to_string(im)

i = 0
last = i
for x in text:
    if x == ')':
        last = i
    i = i + 1

newtext = text[:last].split(')')
newtext2 = []
temp = []

for x in newtext:
    temp.clear()
    # print(x)
    x.replace('\n\n', ' ')
    asd = x.split(' ', 1)
    # print(asd)
    temp.append(asd[0])
    temp.append(asd[1].split('('))
    print(temp)
    newtext2.append(temp)

print(newtext2)
