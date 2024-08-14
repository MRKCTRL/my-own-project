import os
import psycopg2
from flask import Flask, render_template
from flask import Flask, render_template, request, url_for, redirect 


@app.route('/')
def home():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', books=books)