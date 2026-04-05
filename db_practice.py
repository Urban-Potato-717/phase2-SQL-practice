import sqlite3

conn = sqlite3.connect('practice.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        subject TEXT NOT NULL,
        score INTEGER NOT NULL
    )
''')

students_data = [
    ('김철수', '수학', 85),
    ('김철수', '영어', 92),
    ('이영희', '수학', 78),
    ('이영희', '영어', 95),
    ('박민수', '수학', 90),
    ('박민수', '영어', 88),
]

cursor.executemany(
    'INSERT INTO students (name, subject, score) VALUES (?, ?, ?)',
    students_data
)

conn.commit()
#저장 명령어

cursor.execute('SELECT * FROM students')
for row in cursor.fetchall():
    print(row)

conn.close()
#작업 종료