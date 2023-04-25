import csv




with open('chestnii.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(
        ('znak')
    )
da = [
    ['0104603734721249215WgZ&593Irap'],
    ['01046037347212492153KNW193Zu/5']
]
for znaki in da:
    with open('chestnii.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(
            znaki
        )


d = []
dd = []
for barcode in msg:
    d.append(barcode.data.decode('utf-8'))
    dd.append(d)
    d.clear()

with open('chestnii.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(
        ('znak')
    )
