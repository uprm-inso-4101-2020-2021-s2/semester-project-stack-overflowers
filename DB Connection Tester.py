from getpass import getpass
from psycopg2 import connect, Error

try:
    with connect(
            host="backlog-handler-db.cobkfpis7wr9.us-east-2.rds.amazonaws.com",
            user='psqlMaster',
            password='psqlmasterpassword',
            port='5000',
            database='testing_db'
    ) as connection:
        print(connection)

        with connection.cursor() as cursor:
             cursor.execute("CREATE SCHEMA test")

        

except Error as e:
    print(e)
