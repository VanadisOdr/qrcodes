import csv
import cv2
import os
import os.path
from pylibdmtx import pylibdmtx

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


    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    msg = pylibdmtx.decode(thresh, shrink=5,max_count=20, threshold=2, min_edge=20, max_edge=60)


    #Заполняем ячейки расшифровкой ЧЗ
    for barcode in msg:
        with open('chestnii.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([barcode.data.decode('utf-8')])

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
#os.remove(papka)

