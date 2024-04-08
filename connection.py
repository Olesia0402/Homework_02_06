from contextlib import contextmanager

import psycopg2


""" create a database connection to a PostgreSQL database """
@contextmanager
def create_connection():
    try:
        """ create a database connection to database """
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="123456789")
        yield conn
        conn.close()
    except psycopg2.OperationalError as err:
        raise RuntimeError(f"Failed to create database connection {err}")