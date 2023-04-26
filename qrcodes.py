import csv
import numpy as np
import cv2
import copy
import pandas as pd
import os
import os.path
from pylibdmtx import pylibdmtx
from csv import DictWriter
     #Первым делом нужно запускать converver.py в папке pdf#
#Название вводить без расширения
my_fold = input('Введите название pdf файла:')
#Путь к созданном папке в converter.py
papka = f'pdf/{my_fold}'
print(papka)

#Создаём заглавние
with open('chestnii.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(
        ['znak']
    )

#Подсчёт количества страниц для скана ЧЗ
def fcount(path):
    " Сумма файлов в директории "
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1

    return count



pages = fcount(papka)
#Автоперебор страниц
for i in range(1,pages+1):
    # Выбираем картинку
    image = cv2.imread(f'pdf/{my_fold}/{my_fold +"-"+ str(i)}.png', cv2.IMREAD_UNCHANGED);
    print(my_fold +"-"+ str(i))



    d = []
    dd = []
    ddd = []


    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

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

##Удаляем старый csv
os.remove('chestnii.csv')
#Удаляем png файлы
os.remove(papka)


