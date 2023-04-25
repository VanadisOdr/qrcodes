import csv
import numpy as np
import cv2
import copy

from pylibdmtx import pylibdmtx
from csv import DictWriter

image = cv2.imread('test2.png', cv2.IMREAD_UNCHANGED);

d = []
dd = []


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

msg = pylibdmtx.decode(thresh)



for barcode in msg:
    d.append(barcode.data.decode('utf-8'))

for i in range(len(d)):
    dd.insert()
#Генератор списков
dd = [[] for i in range(len(d))]

n = 2
m = 1
a = [[0] * m for i in range(n)]
print(a)



with open('chestnii.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(
        ['znak']
    )

for znakss in dd:
    with open('chestnii.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(
            znakss
        )




