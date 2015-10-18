import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///flask-dash'
db = SQLAlchemy(app)

class DishwasherState(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  is_clean = db.Column(db.Boolean)

  def __init__(self, is_clean):
    self.is_clean = is_clean

  def __repr__(self):
    return '<DishwasherState %r>' % self.id

@app.route('/')
def flask_dash():
  #Get the latest DishwasherState by PK 
  latestState = DishwasherState.query.order_by(DishwasherState.id).first_or_404()

  #If that state is clean
  if latestState.is_clean:
    return 'The dishes are clean'

  #If that state is  dirty
  else:
    return 'The dishes are dirty'

@app.route('/clean')
def new_clean():
  clean = DishwasherState(True)
  #db.session.add(clean)
  #db.session.commit()

  return 'Dishes have been marked clean'

@app.route('/dirty')
def new_dirty():
  dirty = DishwasherState(False)
  #db.session.add(dirty)
  #db.session.commit()

  return 'Dishes have been marked dirty'

@app.route('/toggle')
def toggle_state():
  #Get the latest DishwasherState by PK
  latestState = DishwasherState(True)

  #Save the inverse of the current state
  flipState = not latestState.is_clean
  return flipState
  #new = DishwasherState(flipState)
  #db.session.add(new)
  #db.session.commit()

  return 'Dishwasher State has been toggled'
