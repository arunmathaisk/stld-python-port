from flask import Flask, render_template, redirect, request, session
from stld import app
from stld.modals.dbschema import db, Lab


@app.get('/status/<int:lab_number>')
def status(lab_number):
    lab = Lab.query.filter_by(number=lab_number).first()
    return lab.status
