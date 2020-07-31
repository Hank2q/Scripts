import pytesseract
from PIL import Image, ImageEnhance
import PIL.ImageOps
import numpy
img = Image.open('c:/users/hassanin/Desktop/cap.jfif')
rgb = img.convert('RGB')
eng = PIL.ImageOps.invert(rgb)
enh = ImageEnhance.Brightness(eng)
enh = enh.enhance(10)
imageArray = numpy.array(enh)
print(imageArray)
imageArray = imageArray[:, :, ::-1].copy()
print(imageArray)
t = pytesseract.image_to_string(enh, 'eng')
print(t)
