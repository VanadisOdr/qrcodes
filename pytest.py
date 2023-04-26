import csv
import numpy as np
import cv2
import copy
import pandas as pd
import os
import tempfile

from pdf2image import convert_from_path
from pylibdmtx import pylibdmtx
from csv import DictWriter

#Выбираем картинку
image = cv2.imread('outputpng/order2-1.png', cv2.IMREAD_UNCHANGED);

#3 списка
d = []
dd = []
ddd = []

#надо
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#надо
ret,thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#сканер ЧЗ
msg = pylibdmtx.decode(thresh)


#Перебор найденных ЧЗ и генерация нужного формата для csv [[1],[2]]
for barcode in msg:
    d.append(barcode.data.decode('utf-8'))
#print(d)
for z in d:
    #print(z)
    # Генератор списков с ЧЗ
    dd = [z for i in range(1)]
    ddd.append(dd)
#print(ddd)


#Создаём заглавние
with open('chestnii.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(
        ['znak']
    )
#Заполняем ячейки расшифровкой ЧЗ
for znakss in ddd:
    with open('chestnii.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(
            znakss
        )

#Создаём новый csv и убираем пропуски
with open('chestnii.csv', 'r') as file:
    reader = csv.reader(file)
    rows = [row for row in reader if any(field.strip() for field in row)]

with open('chestnii2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

#Удаляем старый csv
os.remove('chestnii.csv')


