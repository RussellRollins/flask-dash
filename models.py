from app import db

class DishwasherState(db.Model):
  __tablename__ = 'dishwasher_state'

  id = db.Column(db.Integer, primary_key=True)
  is_clean = db.Column(db.Boolean)

  def __init__(self, is_clean):
    self.is_clean = is_clean

  def __repr__(self):
    return '<id {}>'.format(self.id) 
