from stld import db

class Lab(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False,)
    name = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(15), nullable=False)

