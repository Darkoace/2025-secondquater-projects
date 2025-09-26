from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        item = request.form['item']
        conn = sqlite3.connect('productsdatabase.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM PRODUCTS WHERE productName LIKE ?", ('%' + item + '%',))
        results = cursor.fetchall()
        conn.close()
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
