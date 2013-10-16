from json_error import make_json_app
from flask import Flask, Response, request, jsonify
from event import Event
from user import User

from database import db_session, init_db
import multiprocessing
import engine

from users import Users
from events import Events

users = Users(db_session)
events = Events(db_session)

app = make_json_app(__name__.split('.')[0])

"""
Service methods
"""
@app.route('/users', methods = ['GET'])
def users_index():
  _users = users.users()
  print "Listing users... ({users})".format(users=len(_users))
  return jsonify(users=[x.serialize for x in _users])

@app.route('/users/<user_id>', methods = ['GET'])
def user_show(user_id):
  user = users.user(user_id)
  
  if (user == None):
    return jsonify()
    
  print "User {user} was shown...".format(user=user.id)

  return jsonify(user=user.serialize)

@app.route('/status', methods = ['GET'])
def status():
  _events = events.events()
  print "Listing events... ({events})".format(events=len(_events))
  return jsonify(events=[x.serialize for x in _events])

@app.route('/status/<strain>', methods = ['GET'])
def status_show(strain):
  _events = events.events(strain=strain)
  print "Listing events with strain: {strain} ({size})".format(strain=strain, size=len(_events))
  return jsonify(events=[x.serialize for x in _events])

@app.route('/status/<event_id>', methods = ['PUT'])
def event_update(event_id):
  _event = events.put(event_id)
  print "Consumed event {event} from strain {strain}.".format(event=event_id, strain=_event.strain)
  return jsonify({"message":"Consumed event"})

"""
Request methods
"""
@app.route('/users', methods = ['POST'])
def user_request():
  name = request.json.get('name')
  email = request.json.get('email') 

  user = {'name':name, 'email':email}
  events.push("request_user", user)

  print "User '{user}' was requested...".format(user=user['email'])
  return jsonify({"message":"User creation requested"})

@app.route('/users/<user_id>', methods = ['PUT'])
def user_update(user_id=None):
  name = request.json.get('name')
  email = request.json.get('email') 

  user = {'id':user_id, 'name':name, 'email':email}
  events.put("update_user", user)

  print "Update for user id '{user}' was requested...".format(user=user['id'])
  return jsonify({"message":"User update requested"})

@app.route('/users/<user_id>', methods = ['DELETE'])
def user_destroy(user_id=None):  
  user = {'id':user_id}
  events.push("destroy_user", user)
  print "Destruction of '{user}' requested...".format(user=user)
  return jsonify({"message":"User deletion requested"})


if __name__ == "__main__":
  print ""
  print "-*-*-*-*-"
  print "UserService open for business..."
  print "-*-*-*-*-"
  print ""

  init_db()

  jobs = []

  engines = 2
  for strain in ["request_user", "destroy_user", "update_user"]:
    for i in xrange(engines):
      p = multiprocessing.Process(target=engine.run, args=(db_session, strain))
      p.daemon = True
      p.name = "Strain Engine {no} ({strain})".format(strain=strain, no=i)
      print "Starting {job}...".format(job=p.name)
      jobs.append(p)
      p.start()
  
  app.run(debug=True)

  for job in jobs:
    job.join()
