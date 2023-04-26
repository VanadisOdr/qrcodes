#import tempfile

#from pdf2image import convert_from_path

#with tempfile.TemporaryDirectory() as path:
	#images = convert_from_path('pdf/order2.pdf', 500, fmt="png", poppler_path=r'C:\Users\GnedovOO\PycharmProjects\qrcodes\poppler-23.01.0\Library\bin', output_folder=r'C:\Users\GnedovOO\PycharmProjects\qrcodes\outputpng')
from pdf2image import convert_from_path
import os

print('Обнаружение вложенных PDF файлов ...')
print()
for file in os.listdir():  # цикл поиска файлов
	if file.endswith(".PDF") or file.endswith(".pdf"):  # определение файлов пдф
		print('Конвертирование', file, 'в png')
		print()
		name = os.path.join(file)  # вывод имен найденых пдфов
		index = name.index('.')  # отсекаем все после точки
		name = name[:index]  # получаем имя без расширения
		put = os.path.abspath(file)  # получаем путь
		# print('Путь: ', put)
		print()
		pages = convert_from_path(put, 500, poppler_path=r'C:\Users\GnedovOO\PycharmProjects\qrcodes\poppler-23.01.0\Library\bin')
		if not os.path.isdir(name):
			os.mkdir(name)
		for i, page in enumerate(pages):
			page.save(name + f'/{name}-{i+1}.png')

