from flask import Flask, render_template, redirect, request, session
from stld import app
from stld.modals.dbschema import db, Lab
#import json


@app.post('/shutdown/<int:id>')
@app.get('/shutdown/<int:id>')
def shutdown(id):
    lab = Lab.query.get(id)
    lab.status="shutdown"
    db.session.commit()
    return redirect('/controlboard')



