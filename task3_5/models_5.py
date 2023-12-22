from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Regdata(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(20), nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)
    consent_personal = db.Column(db.Boolean, nullable=False)

    def __repr__(self)->str:
        return f'Faculty({self.faculty_name})'

    def __str__(self) ->str:
        return self.faculty_name