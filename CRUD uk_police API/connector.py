"""
This file represents the connection of MySQL and Python

"""

import mysql.connector
"""
Established the connection and created the database
"""
conn = mysql.connector.connect(host='localhost', user='sandeep', passwd='1234')

cursor = conn.cursor()
cursor.execute("CREATE DATABASE uk_police")
print("Database is created")

"""
The query for checking present databases 
"""
show_db_query = "SHOW DATABASES"
with conn.cursor() as cursor:
    cursor.execute(show_db_query)
    for db in cursor:
        print(db)
