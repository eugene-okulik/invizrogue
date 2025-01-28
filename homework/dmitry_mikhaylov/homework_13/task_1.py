import os
from datetime import datetime, timedelta


homework_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

with open(file_path, 'r') as data_file:
    for line in data_file.readlines():
        date_str = line.split()[1] + " " + line.split()[2]
        given_date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
        if line.startswith('1'):
            print(given_date + timedelta(weeks=1))
        elif line.startswith('2'):
            print(datetime.strftime(given_date, "%A"))
        elif line.startswith('3'):
            print((datetime.now() - given_date).days)
