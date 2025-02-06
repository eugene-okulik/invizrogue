import os
import csv
import dotenv
import mysql.connector as mysql

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)
cursor = db.cursor(dictionary=True)

homework_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path = os.path.join(
    homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv'
)

query = '''
SELECT COUNT(*) as count
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON b.taken_by_student_id = s.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjets sj ON sj.id = l.subject_id
WHERE s.name = %s AND s.second_name = %s
AND g.title = %s AND b.title = %s
AND sj.title = %s AND l.title = %s AND m.value = %s;'''

with open(file_path, newline='') as csv_file:
    for row in csv.reader(csv_file):
        cursor.execute(query, tuple(row))
        result = cursor.fetchone()
        if result['count'] == 0:
            print('В БД не найден набор данных:', row)

# Для проверки использовал файл, в который включил свой набор данных
# with open('test.csv', newline='') as csv_file:
#     for row in csv.reader(csv_file):
#         cursor.execute(query, tuple(row))
#         result = cursor.fetchone()
#         if result['count'] == 0:
#             print('В БД не найден набор данных:', row)

db.close()
