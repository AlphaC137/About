# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)

# Models
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20))
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime)
    tasks = db.relationship('Task', backref='project', lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20))
    priority = db.Column(db.String(20))
    due_date = db.Column(db.DateTime)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

# Routes
@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

@app.route('/project/new', methods=['GET', 'POST'])
def new_project():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        status = request.form['status']
        due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d') if request.form['due_date'] else None
        
        project = Project(title=title, description=description, status=status, due_date=due_date)
        db.session.add(project)
        db.session.commit()
        flash('Project created successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('new_project.html')

@app.route('/project/<int:id>')
def view_project(id):
    project = Project.query.get_or_404(id)
    return render_template('view_project.html', project=project)

@app.route('/project/<int:id>/task/new', methods=['GET', 'POST'])
def new_task(id):
    project = Project.query.get_or_404(id)
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        status = request.form['status']
        priority = request.form['priority']
        due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d') if request.form['due_date'] else None
        
        task = Task(
            title=title,
            description=description,
            status=status,
            priority=priority,
            due_date=due_date,
            project_id=project.id
        )
        db.session.add(task)
        db.session.commit()
        flash('Task added successfully!', 'success')
        return redirect(url_for('view_project', id=project.id))
    
    return render_template('new_task.html', project=project)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)