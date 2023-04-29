import csv
import cv2
import os.path
from pylibdmtx import pylibdmtx
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from platform import python_version
from dotenv import load_dotenv

load_dotenv()
#answer = input('Желаете ли вы удалить старый файл?:')

#def delete_old(answer):
    #Удаление старого файла
    #os.remove('chestnii2.csv')

#if answer == 'да' or 'Да' or 'ДА':
    #delete_old(answer.replace(' ', ''))

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

#Отправка письма на почту
server = 'smtp.mail.ru'
user = 'olegsendtest@mail.ru'
password = os.getenv('PASSWORD')

subject = 'sendmailtest'

filepath = "chestnii2.csv"
basename = os.path.basename(filepath)
filesize = os.path.getsize(filepath)

msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = os.getenv('MAIL2')
msg['To'] = os.getenv('MAIL')
msg['Reply-To'] = os.getenv('MAIL2')
msg['Return-Path'] = os.getenv('MAIL2')


part_file = MIMEBase('application', 'octet-stream; name="{}"'.format(basename))
part_file.set_payload(open(filepath, "rb").read())
part_file.add_header('Content-Description', basename)
part_file.add_header('Content-Disposition', 'attachment; filename="{}"; size={}'.format(basename, filesize))
encoders.encode_base64(part_file)

msg.attach(part_file)

mail = smtplib.SMTP_SSL(server)
mail.login(user, password)
mail.sendmail(os.getenv('MAIL2'), os.getenv('MAIL'), msg.as_string())
mail.quit()
