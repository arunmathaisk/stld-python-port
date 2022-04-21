from flask import Flask, render_template, redirect, request, session
from stld import app
from stld.modals.dbschema import db, Lab



@app.get('/controlboard')
def controlboard():
    if 'auth' in session:
        labs = Lab.query.all()
        return render_template('controlboard.html',labs=labs)
    else:
        return redirect('/login')