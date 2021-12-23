from flask import *
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'flash message'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'sandeep'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'uk_police'

mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM uk_police.search_data")
    data = cur.fetchall()
    cur.close()
    return render_template('index2.html', search_data=data)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        date = request.form['date']
        stop_and_search = request.form['stop_and_search']
        cur = mysql.connection.cursor()
        try:
            cur.execute("INSERT INTO search_data (date, stop_and_search) VALUES (%s, %s)", (date, stop_and_search))
            mysql.connection.commit()
            flash("Data Inserted Successfully")
            return redirect(url_for('index'))
        except Exception:
            flash('Enter a unique values')
            return redirect(url_for('index'))


@app.route('/delete/<string:id_data>', methods=['GET', 'POST'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM search_data WHERE date=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('index'))


@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        date = request.form['date']
        stop_and_search = request.form['stop_and_search']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE search_data 
               SET stop_and_search=%s
               WHERE date=%s
            """, (stop_and_search, date))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
