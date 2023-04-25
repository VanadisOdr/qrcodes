import csv
import numpy as np
import cv2

from pylibdmtx import pylibdmtx
from csv import DictWriter

image = cv2.imread('order-01.png', cv2.IMREAD_UNCHANGED);

d = []

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

msg = pylibdmtx.decode(thresh)

zkanks = [

]

for barcode in msg:
    print(barcode.data.decode('utf-8'))
    d.append(barcode.data.decode('utf-8'))

with open('chestnii.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(
        ('znak')
    )

