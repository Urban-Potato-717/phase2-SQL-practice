import sqlite3

conn = sqlite3.connect('practice.db')
cursor = conn.cursor()

# 문제 1: 모든 학생의 이름과 점수만 조회
cursor.execute('SELECT name,score FROM students')
print(cursor.fetchall())

# 문제 2: 점수가 90점 이상인 데이터만 조회
cursor.execute('SELECT name,score FROM students WHERE score>=90')
print(cursor.fetchall())

# 문제 3: 과목별 평균 점수
cursor.execute('SELECT subject, AVG(score) FROM students GROUP BY subject')
print(cursor.fetchall())

# 문제 4: 학생별 총점을 구하고, 높은 순 정렬 *숫자 오름차순 및 이름 역순: DESC
cursor.execute('SELECT name, SUM(score) FROM students GROUP BY name ORDER BY SUM(score) DESC')
print(cursor.fetchall())

conn.close()