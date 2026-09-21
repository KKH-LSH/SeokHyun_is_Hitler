import pymysql
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def init_mysql_db():
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='q1w2e3',
            charset='utf8mb4'
        )
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS study DEFAULT CHARACTER SET utf8mb4;")
        conn.commit()
        cursor.close()
        conn.close()
    except Exception:
        pass

init_mysql_db()

class TodoDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='q1w2e3', db='study')
        self.cur = self.db.cursor()
        self.cur.execute("""
            create table IF NOT EXISTS todos (
            todo_index int auto_increment PRIMARY KEY,
            task varchar(100) not null,
            completed varchar(30) default 'false' not null)
                         """)

    def get(self):
        sql = "select * from todos"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def add(self, title):
        sql = "insert into todos(task) values('{0}')".format(title)
        self.cur.execute(sql)
        self.db.commit()

    def completed(self, todo_index):
        sql = f"update todos set completed='true' where todo_index={todo_index}"
        self.cur.execute(sql)
        self.db.commit()

    def remove(self, todo_index):
        sql = f"delete from todos where todo_index={todo_index}"
        self.cur.execute(sql)
        self.db.commit()

todo_db = TodoDB()

@app.route('/')
def index():
    tasks = todo_db.get()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form.get('title', '').strip()
    if title:
        todo_db.add(title)
    return redirect(url_for('index'))

@app.route('/complete/<int:todo_index>', methods=['PATCH'])
def complete_todo(todo_index):
    todo_db.completed(todo_index)
    return jsonify({'message': 'ok'})

@app.route('/delete/<int:todo_index>', methods=['DELETE'])
def delete_todo(todo_index):
    todo_db.remove(todo_index)
    return jsonify({'message': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
