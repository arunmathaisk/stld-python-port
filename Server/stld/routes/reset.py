from flask import Flask, render_template, redirect, request, session
from stld import app
from stld.modals.dbschema import db, Lab
#import json


@app.post('/reset/<int:id>')
@app.get('/reset/<int:id>')
def reset(id):
    lab = Lab.query.get(id)
    lab.status="awake"
    db.session.commit()
    return redirect('/controlboard')



