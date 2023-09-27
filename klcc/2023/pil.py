from PIL import Image
import numpy as np

img = Image.open(r'C:\Users\aditc\dev\competitive-programming-practise\klcc\2023\question_grayscale_image.png')
data = np.asarray(img.getdata())

for word in data:
    for part in data:
        print(chr(part))