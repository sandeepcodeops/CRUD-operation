import mysql.connector

conn = mysql.connector.connect(host='localhost', user='sandeep', passwd='1234')
cursor = conn.cursor()

sql = "SELECT * FROM employee.employee_data"
cursor.execute(sql)
result = cursor.fetchall()
for i in result:
    print(i)
