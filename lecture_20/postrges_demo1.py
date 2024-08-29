import psycopg2


dbname = 'demo_hillel'
user = 'p14s'
password = 'aswdertf'
host = 'localhost'
port = '5432'

try:
    connection = None
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print('Connected to the database established successfully!')

    cursor = connection.cursor()
    cursor.execute("select * from users;")
    records = cursor.fetchall()
    for rec in records:
        print("Record:", rec)
except (Exception, psycopg2.Error) as error:
    print('Error while connecting to the DB', error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("DB connection is closed!")
