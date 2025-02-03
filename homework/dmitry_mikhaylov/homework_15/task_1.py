import mysql.connector as mysql
import random

student_name = 'Luke'
student_second_name = 'Skywalker'

books = ['Lightsaber extended manual',
         'Laser weapons extended manual',
         'Space fighter control extended manual']

group_name = 'Jedy group'
group_start = 'jan 2025'
group_end = 'jan 2026'

lessons = {
    'Lightsaber lesson': 2,
    'Laser weapons lesson': 2,
    'Space fighter control lesson': 2
}

courses = {
    'Lightsaber extended course':
        {'lesson_name': 'Lightsaber lesson', 'lesson_number': 2},
    'Laser weapons extended course':
        {'lesson_name': 'Laser weapons lesson', 'lesson_number': 2},
    'Space fighter control extended course':
        {'lesson_name': 'Space fighter control lesson', 'lesson_number': 2},
}

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

query = "INSERT INTO students (name, second_name) VALUES (%s, %s);"
cursor.execute(query, (student_name, student_second_name))
student_id = cursor.lastrowid

query = "INSERT INTO books (title) VALUES (%s);"
book_ids = []
for book in books:
    cursor.execute(query, [book])
    book_ids.append(cursor.lastrowid)

query = "UPDATE books SET taken_by_student_id = %s WHERE id = %s;"
cursor.executemany(query, list([(student_id, book_id) for book_id in book_ids]))

query = '''
INSERT INTO `groups` (title, start_date, end_date)
VALUES (%s, %s, %s);'''
cursor.execute(query, (group_name, group_start, group_end))
group_id = cursor.lastrowid

query = '''
UPDATE students
SET group_id = %s
WHERE id = %s;
'''
cursor.execute(query, (group_id, student_id))

query = "INSERT INTO subjets (title) VALUES (%s);"
for subject in courses.keys():
    cursor.execute(query, [subject])
    courses[subject]['id'] = cursor.lastrowid

query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s);"
for subject, info in courses.items():
    courses[subject]['lesson_ids'] = []
    for count in range(info['lesson_number']):
        cursor.execute(
            query,
            (info['lesson_name'] + ' ' + str(count + 1), info['id'])
        )
        courses[subject]['lesson_ids'].append(cursor.lastrowid)

query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s);"
for subject, info in courses.items():
    values = list([
        (random.randint(3, 5),
         lesson_id,
         student_id) for lesson_id in info['lesson_ids']])
    cursor.executemany(query, values)

db.commit()

query = '''
SELECT `value`
FROM marks
WHERE student_id = %s;'''
cursor.execute(query, (student_id,))
marks = cursor.fetchall()
print(marks)

query = '''
SELECT title
FROM `books`
WHERE taken_by_student_id = %s;'''
cursor.execute(query, (student_id,))
taken_books = cursor.fetchall()
print(taken_books)

query = '''
SELECT s.name, s.second_name, g.title AS `group`,
b.title AS book, sj.title AS subject, l.title AS lesson, m.value AS mark
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON b.taken_by_student_id = s.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjets sj ON sj.id = l.subject_id
WHERE s.id = %s;'''
cursor.execute(query, (student_id,))
student_info = cursor.fetchall()
print(student_info)

db.close()
