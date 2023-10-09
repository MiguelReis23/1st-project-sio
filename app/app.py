import os
import sqlite3


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html',title='Test')


if __name__ == '__main__':
    app.run(port=8080)
