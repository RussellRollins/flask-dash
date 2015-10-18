from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import *

@app.route('/')
def flask_dash():
  #Get the latest DishwasherState by PK
  latestState = DishwasherState.query.order_by(DishwasherState.id.desc()).first_or_404()

  #If that state is clean
  if latestState.is_clean:
    return 'The dishes are clean'

  #If that state is  dirty
  else:
    return 'The dishes are dirty'

@app.route('/clean')
def new_clean():
  clean = DishwasherState(True)
  db.session.add(clean)
  db.session.commit()

  return 'Dishes have been marked clean'

@app.route('/dirty')
def new_dirty():
  dirty = DishwasherState(False)
  db.session.add(dirty)
  db.session.commit()

  return 'Dishes have been marked dirty'

@app.route('/toggle', methods=['POST'])
def toggle_state():
  if request.method == 'POST':
    #Get the latest DishwasherState by PK
    latestState = DishwasherState.query.order_by(DishwasherState.id.desc()).first_or_404()

    #Save the inverse of the current state
    flipState = not latestState.is_clean
    new = DishwasherState(flipState)
    db.session.add(new)
    db.session.commit()

    return 'Dishwasher State has been toggled'
  else:
    abort(404)

if __name__ == '__main__':
  app.run()

