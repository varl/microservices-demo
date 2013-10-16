from users import Users
from events import Events

from time import sleep

def run(db_session, strain):
  users = Users(db_session)
  events = Events(db_session)
  
  while (1):
    # Very slow poppin' from the DB so 
    # we build a nice queue of events
    event = events.pop(strain)

    if event == None:
      continue

    print "ENGINE: Event Strain: '{strain}'".format(strain=event.strain)
    if event.strain == "request_user":
      user = event.payload_dec
      users.create(user['name'], user['email'])
      events.push("created_user", user)
      print "ENGINE: User '{email}' created.".format(email=user['email'])
    elif event.strain == "destroy_user":
      user = event.payload_dec
      users.destroy(user['id'])
      events.push("destroyed_user", user)
      print "ENGINE: User '{id}' destroyed.".format(id=user['id'])
    elif event.strain == "update_user":
      user = event.payload_dec
      users.update(user)
      events.push("updated_user", user)
      print "ENGINE: User '{email}' updated.".format(email=user['email'])
    
    sleep(5)
