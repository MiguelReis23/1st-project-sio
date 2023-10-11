import os
import sqlite3


from flask import Flask, render_template, url_for, request, redirect, flash, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',title='Home')


if __name__ == '__main__':
    app.run(port=8080)
