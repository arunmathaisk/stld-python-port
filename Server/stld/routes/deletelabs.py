from flask import Flask, render_template, redirect, request, session
from stld import app
from stld.modals.dbschema import db, Lab
#import json


@app.get('/deletelabs')
def deletelabs():
    if 'auth' in session:
        labs = Lab.query.all()
        return render_template('deletelabs.html',labs=labs)
    else:
        return redirect('/login')


@app.post('/deletelab/<int:id>')
@app.get('/deletelab/<int:id>')
def deletelab_get_post(id):
    lab = Lab.query.get(id)
    db.session.delete(lab)
    db.session.commit()
    return redirect('/deletelabs')



