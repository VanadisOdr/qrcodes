from pdf2image import convert_from_path

image = convert_from_path('order.pdf',500,poppler_path='C:\Users\GnedovOO\PycharmProjects\qrcodes\venv\Lib\Lib\site-packages\pdf2image\poppler-23.01.0\Library\bin')

for i in range(len(image)):
    image[i].save('page'+ str[i] +'.jpg', 'JPEG')





