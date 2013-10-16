from sqlalchemy import Column, Integer, String, DateTime, Boolean
from database import Base
from datetime import datetime
import jsonpickle

class Event(Base):
  __tablename__ = 'event'
  id = Column(Integer, primary_key=True)
  strain = Column(String)
  payload = Column(String)
  creation_date = Column(DateTime)
  consumed = Column(Boolean)

  def __init__(self, strain, payload):
    self.creation_date = datetime.utcnow()
    self.strain = strain
    self.payload = unicode(jsonpickle.encode(payload))
    self.consumed = False

  @property
  def payload_dec(self): 
    return jsonpickle.decode(self.payload)  
    
  @property
  def serialize(self):
    return {
          'id':self.id,
          'strain':self.strain,
          'payload':self.payload,
          'consumed':self.consumed,
          'created':self.creation_date.strftime("%Y-%m-%d %H:%M:%S"),
        }

