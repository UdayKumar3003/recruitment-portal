# app/models.py
from . import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    skills = db.Column(db.String(200))
    experience = db.Column(db.String(50))
    openings = db.Column(db.Integer)
    budget = db.Column(db.String(50))

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    resume = db.Column(db.String(200))
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))