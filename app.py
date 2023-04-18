import random
import sqlite3
from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def main():
    conn = sqlite3.connect("tovary.db")
    cursor = conn.cursor()
    select_query = """SELECT * from Tovary"""
    cursor.execute(select_query)
    records = cursor.fetchall()
    res_list = []
    for s in  records:
        d1 = {"name":s[0], "price":s[2], "image":s[1]}
        res_list.append(d1)        
    return render_template("index.html",res_list=res_list)
app.run("0.0.0.0")