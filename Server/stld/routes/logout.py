from flask import Flask, render_template, redirect, request, session
from stld import app
#from jedi.modals.dbschema import db, User
#import json


@app.get('/logout')
def logout():
    if 'auth' in session:
       session.pop('auth', None)
    return redirect('/')

@app.post('/logout')
def logout_post():
    if 'auth' in session:
       session.pop('auth', None)
    return redirect('/')


    
   




