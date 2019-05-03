import os
from threading import Thread
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
  name = StringField('What is your name?', validators=[DataRequired()])
  submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
  form = NameForm()
  if form.validate_on_submit():
    # old_name = session.get('name')
    user = User.query.filter_by(username=form.name.data).first()
    if user is None:
      user = User(username=form.name.data)
      db.session.add(user)
      #db.session.commit()
      session['known'] = False
      if app.config['FLASKY_ADMIN']:
        send_email(app.config['FLASKY_ADMIN'], 'New User', 'mail/new_user', user=user)
    else:
      session['known'] = True
    session['name'] = form.name.data
    form.name.data = ''
    return redirect(url_for('index'))
  return render_template('index.html', 
    form=form,
    name=session.get('name'),
    known=session.get('known', False)
  )


@app.route('/user/<name>')
def user(name):
  return render_template('user.html', name=name)