from user import User
from sqlalchemy import distinct 
from sqlalchemy.exc import IntegrityError, InterfaceError

class Users:
  def __init__(self, session=None):
    self.session = session

  def users(self):
    return User.query.all() 

  def user(self, user_no):
    return User.query.filter(User.id == user_no).scalar()

  def destroy(self, user_id):
    user = User.query.filter(User.id == user_id).scalar()
    if user != None:
      self.session.delete(user)
      self.commit()
    return

  def create(self, name, email):
    user = User(name, email)
    self.session.add(user)
    self.commit() 
    return

  def update(self, user):
    _user = User.query.filter(User.id == user['id']).one()
    if user['name']:
      _user.name = user['name']
    if user['email']:      
      _user.email = user['email']
    return self.commit()

  def commit(self):
    try:
      self.session.commit()
      return "OK"
    except IntegrityError:
      return "Panic at the disco"

