from flask import Flask, render_template, redirect, url_for
import pymysql

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<num>")
def save_num_get(num):
    conn = pymysql.connect(host='localhost', user='root', password='q1w2e3', db='study')
    cur = conn.cursor()
    cur.execute("insert into numcount(num) values({0})".format(num))
    conn.commit()
    conn.close()

    return redirect(url_for("index"))
if __name__ == "__main__":
    app.run(host="0.0.0.0")
