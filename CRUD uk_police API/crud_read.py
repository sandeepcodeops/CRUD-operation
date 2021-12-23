import mysql.connector
import webbrowser

conn = mysql.connector.connect(host="localhost", user='sandeep', passwd='1234', database="uk_police")

select_search_query = "SELECT * FROM search_data"
with conn.cursor() as cursor:
    cursor.execute(select_search_query)
    result = cursor.fetchall()
    # for row in result:
    #     # print(row)

p = []

tbl = "<tr><td>date</td><td>stop_and_search</td></tr>"
p.append(tbl)

for row in result:
    a = "<tr><td>%s</td>"%row[0]
    p.append(a)
    b = "<td>%s</td>"%row[1]
    p.append(b)


contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta content="text/html; charset=ISO-8859-1"
http-equiv="content-type">
<title>CRUD read</title>
</head>
    <h1> CRUD Operations for read</h1>
<body>
<table>
%s
</table>
</body>
</html>
'''%(p)

filename = 'webbrowser.html'


def main(contents, filename):
    output = open(filename, "w")
    output.write(contents)
    output.close()


main(contents, filename)
webbrowser.open(filename)


if conn.is_connected():
    cursor.close()
    conn.close()
    print("MySQL connection is closed.")
