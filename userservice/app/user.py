from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text
from database import Base
from datetime import datetime
import jsonpickle

import json

class User(Base):
  __tablename__ = 'user'
  id = Column(Integer, primary_key=True)
  name = Column(String)
  email = Column(String)
  creation_date = Column(DateTime)

  def __init__(self, name, email):
    self.creation_date = datetime.utcnow()
    self.name = name
    self.email = email

  @property
  def serialize(self):
    return {
          'id':self.id,
          'name':self.name,
          'email':self.email,
          'created':self.creation_date
        }
