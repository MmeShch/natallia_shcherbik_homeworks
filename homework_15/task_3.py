# 3) Требуется создать csv-файл «rows_300.csv» со следующими столбцами:
# – № - номер по порядку (от 1 до 300);
# – Секунда – текущая секунда на вашем ПК;
# – Микросекунда – текущая миллисекунда на часах.
# На каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.
import csv
import time
import datetime

with open('rows_300.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Number', 'Second', 'Microsecond'])

    for i in range(1, 301):
        now = datetime.datetime.now()
        writer.writerow([i, now.second, now.microsecond])
        time.sleep(0.01)


