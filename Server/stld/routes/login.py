from flask import Flask, render_template, redirect, request, session
from stld import app
#from jedi.modals.dbschema import db, User
#import json

@app.get('/')
@app.get('/login')
def login():
    if 'auth' in session:
        return redirect('/controlboard')
    else:
        return render_template('login.html')

@app.post('/login')
def login_post():
    password = request.form['password']
    if password == 'royal_stag':
        session['auth'] = 1
        return redirect('/controlboard')
    else:
        return redirect('/login')


    
   




