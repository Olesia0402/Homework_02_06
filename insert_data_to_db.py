import logging

from faker import Faker
import random
from psycopg2 import DatabaseError


from connection import create_connection


fake_data = Faker(locale="uk-UA")


def insert_data_for_groups(conn):
    # Додавання груп
    cursor = conn.cursor()
    for _ in range(3):
        cursor.execute("INSERT INTO groups (group_name) VALUES (%s)", (fake_data.word(), ))
    try:
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()

def insert_data_for_teachers(conn):
    # Додавання викладачів
    cursor = conn.cursor()
    for _ in range(5):
        cursor.execute("INSERT INTO teachers (teacher_name) VALUES (%s)", (fake_data.name(), ))
    try:
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()

def insert_data_for_subjects(conn):
    # Додавання предметів із вказівкою викладача
    cursor = conn.cursor()
    for teacher_id in range(1, 6):
        for _ in range(2):
            cursor.execute("INSERT INTO subjects (subject_name, teacher_id) VALUES (%s, %s)", (fake_data.word(), teacher_id))
    try:
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()

def insert_data_for_students(conn):
    # Додавання студентів
    cursor = conn.cursor()
    for group_id in range(1, 4):
        for _ in range(15):
            cursor.execute("INSERT INTO students (student_name, group_id) VALUES (%s, %s) RETURNING student_id", (fake_data.name(), group_id))
    try:
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
        
def insert_data_for_grades(conn):
    cursor = conn.cursor()
    existing_students_ids = []
    cursor.execute('''SELECT student_id FROM students;''')
    for row in cursor.fetchall():
        existing_students_ids.append(row[0])
    existing_subjects_ids = []
    cursor.execute('''SELECT subject_id FROM subjects;''')
    for row in cursor.fetchall():
        existing_subjects_ids.append(row[0])
    for student_id in existing_students_ids:
        for subject_id in existing_subjects_ids:
            for _ in range(5):
                cursor.execute("INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (%s, %s, %s, %s)",
                                (student_id, subject_id, random.randint(0, 100), fake_data.date_this_decade()))
    try:
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()


if __name__ == '__main__':
    with create_connection() as conn:
        insert_data_for_groups(conn)
        insert_data_for_teachers(conn)
        insert_data_for_students(conn)
        insert_data_for_subjects(conn)
        insert_data_for_grades(conn)

