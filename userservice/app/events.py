from event import Event 
from sqlalchemy import distinct 
from sqlalchemy.exc import IntegrityError, InterfaceError 

class Events:
  def __init__(self, session=None):
    self.session = session

  def events(self, strain=None):
    if strain == None:
      return Event.query.filter(Event.consumed == False).all()
    else:
      return Event.query.filter(Event.consumed == False, Event.strain == strain).all()[:50]

  def push(self, strain, payload):
    event = Event(strain, payload)
    self.session.add(event)
    return self.commit()

  def put(self, event_id):
    event = Event.query.filter(Event.consumed == False, Event.id == event_id).scalar()
    if event != None:
      event.consumed = True
      self.commit()
    return event

  def peek(self, strain):
    return Event.query.filter(Event.consumed == False, Event.strain == strain).first()  

  def pop(self, strain):
    event = Event.query.filter(Event.consumed == False, Event.strain == strain).first()
    if event != None:
      event.consumed = True
      self.commit()
    return event

  def commit(self):
    try:
      self.session.commit()
      return "OK"
    except IntegrityError:
      return "Panic at the disco"

