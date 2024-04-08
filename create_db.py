import logging
from psycopg2 import DatabaseError

from connection import create_connection


tables = ['''create table if not exists groups(
group_id smallserial PRIMARY key,
group_name varchar(100) not null);''',
'''create table if not exists students(
student_id smallserial primary key,
student_name varchar(100) not null,
group_id smallint references groups(group_id) on delete cascade);''',
'''create table if not exists teachers(
teacher_id smallserial primary key,
teacher_name varchar(100) not null);''',
'''create table if not exists subjects(
subject_id smallserial primary key,
subject_name varchar(100) not null,
teacher_id smallint references teachers(teacher_id) on delete cascade);''',
'''create table if not exists grades(
id smallserial primary key,
student_id smallint references students(student_id) on delete cascade,
subject_id smallint references subjects(subject_id) on delete cascade,
grade smallint check (grade >= 0 AND grade <= 100),
grade_date date not null);''']


def create_table(conn, sql_expression: str):
    c = conn.cursor()
    try:
        c.execute(sql_expression)
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()


if __name__ == '__main__':
    try:
        with create_connection() as conn:
            if conn is not None:
                for table in tables:
                    create_table(conn, table)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)