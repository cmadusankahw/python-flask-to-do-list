from app import app
from flask import render_template

import forms

# flask routes : basic example
@app.route('/')
@app.route('/index') # setting multiple routes
def index():
    return render_template('index.html', current_title='ToDo App')

# flask routes : basic example
@app.route('/add', methods=["GET", "POST"])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        print('Submitted title', form.title.data)
    return render_template('add.html', current_title='ToDo App - About',  form = form)