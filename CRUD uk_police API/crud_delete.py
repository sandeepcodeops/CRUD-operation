import mysql.connector
import webbrowser

conn = mysql.connector.connect(host="localhost", user='sandeep', passwd='1234', database="uk_police")

select_update_query = "DELETE FROM search_data WHERE date = '2021-06-01'"
conn.cursor().execute(select_update_query)
select_search_query = "SELECT * FROM search_data"
with conn.cursor() as cursor:
    cursor.execute(select_search_query)
    result = cursor.fetchall()
    # for row in result:
    #     print(row)

p = []

tbl = "<tr><td>date</td><td>stop_and_search</td></tr>"
p.append(tbl)

for row in result:
    a = "<tr><td>%s</td>"%row[0]
    p.append(a)
    b = "<td>%s</td>"%row[1]
    p.append(b)


contents = '''
<html>
<head>
<meta content="text/html; charset=ISO-8859-1" http-equiv="content-type">
<title>CURD update</title>
</head>
    <h1> CRUD Operations</h1>
<body>
<table>
%s
</table>
</body>
</html>
''' % p

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
