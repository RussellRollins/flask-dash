from flask import Flask, request, abort, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy
import os
import cleanliness

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import *

@app.route('/')
def flask_dash():
  #Get the latest DishwasherState by PK
  latestState = DishwasherState.query.order_by(DishwasherState.id.desc()).first_or_404()   

  return render_template('home.html',
                         message=cleanliness.message(latestState.is_clean),
                         bg_color='bg-success' if latestState.is_clean else 'bg-danger') 

#@app.route('/clean')
#def new_clean():
#  clean = DishwasherState(True)
#  db.session.add(clean)
#  db.session.commit()
#
#  return 'Dishes have been marked clean'

#@app.route('/dirty')
#def new_dirty():
#  dirty = DishwasherState(False)
#  db.session.add(dirty)
#  db.session.commit()

#  return 'Dishes have been marked dirty'

@app.route('/toggle', methods=['POST'])
def toggle_state():
  if request.method == 'POST':
    #Some semplance of security
    if request.form['key'] == os.environ['ACCESS_KEY']:
      #Get the latest DishwasherState by PK
      latestState = DishwasherState.query.order_by(DishwasherState.id.desc()).first_or_404()

      #Save the inverse of the current state
      flipState = not latestState.is_clean
      new = DishwasherState(flipState)
      db.session.add(new)
      db.session.commit()

      return 'Dishwasher State has been toggled'
    else:
      abort(403)
  else:
    abort(404)

if __name__ == '__main__':
  app.run()

