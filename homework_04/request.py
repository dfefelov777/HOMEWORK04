import psycopg2
from psycopg2 import OperationalError

def create_connection():
    try:
        connection = psycopg2.connect(
            dbname="postgress",
            user="user",
            password="password",
            host="localhost",
            port="5432"
        )
        print("Connection to PoseteSQL DB successful")
        return connection
    except OperationalError as t:
        print(f"The error '{t}' occured")

connection = create_connection()