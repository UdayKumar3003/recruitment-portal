# app/routes.py
from flask import Blueprint, render_template, request, redirect
from .models import db, Job, Application

main = Blueprint('main', __name__)

@main.route('/')
def index():
    jobs = Job.query.all()
    return render_template('index.html', jobs=jobs)

@main.route('/job/post', methods=['GET', 'POST'])
def post_job():
    if request.method == 'POST':
        job = Job(
            title=request.form['title'],
            skills=request.form['skills'],
            experience=request.form['experience'],
            openings=request.form['openings'],
            budget=request.form['budget']
        )
        db.session.add(job)
        db.session.commit()
        return redirect('/')
    return render_template('job_post.html')

@main.route('/job/<int:job_id>/apply', methods=['GET', 'POST'])
def apply(job_id):
    if request.method == 'POST':
        application = Application(
            name=request.form['name'],
            email=request.form['email'],
            resume=request.form['resume'],
            job_id=job_id
        )
        db.session.add(application)
        db.session.commit()
        return redirect('/')
    return render_template('apply.html', job_id=job_id)

@main.route('/applications')
def view_applications():
    applications = Application.query.all()
    return render_template('applications.html', applications=applications)
