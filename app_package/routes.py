from app_package import app, db
from flask import render_template, redirect, url_for, flash

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')