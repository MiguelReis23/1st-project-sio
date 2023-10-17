import os
import sqlite3


from flask import Flask, render_template, url_for, request, redirect, flash, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html',title='Test')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html',title='Checkout')

if __name__ == '__main__':
    app.run(port=8080)
