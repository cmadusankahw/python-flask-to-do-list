from app import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from models import Task
from datetime import datetime
import forms

# flask routes : index page
@app.route('/')
@app.route('/index') # setting multiple routes
def index():
    tasks = Task.query.all()
    return render_template('index.html', current_title='ToDo App', tasks=tasks)

# flask routes : add tasks page
@app.route('/add', methods=["GET", "POST"])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        # create a new Task with for data
        t = Task(title=form.title.data, date=datetime.utcnow())

        # adding task to db
        db.session.add(t)
        db.session.commit()

        # showind alert
        flash('Task added successfully!')

        # redirecting to index (give a REST function name as param for url_for)
        return redirect(url_for('index'))

    return render_template('add.html', current_title='ToDo App - Add Tasks',  form = form)


# flask routes : edit a task (passing task_id:int as a param)
@app.route('/edit/<int:task_id>', methods=["GET", "POST"])
def edit(task_id):
    # query required task to edit
    task = Task.query.get(task_id)

    # creating form to edit task
    form = forms.AddTaskForm()

    if task:
        # edit task form's submit call
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.utcnow()
            db.session.commit()
            flash('Task updated successfully!')
            return redirect(url_for('index'))
        # if not form submitted 
        form.title.data = task.title
        return render_template('edit.html', form=form, task_id=task_id)
    else:
        flash('Task not found!')

    # redirecting to index (give a REST function name as param for url_for)
    return redirect(url_for('index'))


# flask routes : delete a task (passing task_id:int as a param)
@app.route('/delete/<int:task_id>', methods=["GET", "POST"])
def delete(task_id):
    # query required task to edit
    task = Task.query.get(task_id)

    # creating form to edit task
    form = forms.DeleteTaskForm()

    if task:
        # edit task form's submit call
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash('Task has been deleted!')
            return redirect(url_for('index'))
        # if not form submitted 
        return render_template('delete.html', form=form, task_id=task_id, title=task.title)
    else:
        flash('Task not found!')

    # redirecting to index (give a REST function name as param for url_for)
    return redirect(url_for('index'))

