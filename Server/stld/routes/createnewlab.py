from flask import Flask, render_template, redirect, request, session
from stld import app
from stld.modals.dbschema import db, Lab
#import json


@app.get('/createnewlab')
def createnewlab():
    if 'auth' in session:
        return render_template('createnewlab.html')
    else:
        return redirect('/login')

@app.post('/createnewlab')
def createnewlab_post():
    lab_number = int(request.form['lab_number'])
    lab_name = request.form['lab_name']
    lab = Lab(number=lab_number,name=lab_name,status="awake")
    db.session.add(lab)
    db.session.commit()
    return redirect('/createnewlab')