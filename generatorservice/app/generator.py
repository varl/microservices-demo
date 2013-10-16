import requests
import json


list = {}

for i in xrange(10000):
  list['viva_'+str(i)] = 'viva_'+str(i)+'@foo.tld'
        
for name, email in list.iteritems():
  body = json.dumps({u'name':name, 'email':email})
  headers = {'content-type': 'application/json'}
  r = requests.post(url=u"http://localhost:5000/users", data=body, headers=headers)
  print 'Generated ' +name + ', ' + email

