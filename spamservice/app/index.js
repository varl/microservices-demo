request = require('request-json');
var client = request.newClient('http://localhost:5000/');


setInterval(function() {
  console.log("Polling user service for created users...");
  client.get('status/created_user', function email_fulfilment(err, res, body) {
    if (err) {
      console.log("Couldn't poll user service, retrying...");
      return
    }
    var i = 0;
    for (;i<body.events.length;++i) {
      var event = body.events[i];
      var user = JSON.parse(event.payload);
      client.put('status/'+event.id, {}, function(err, res, body) {
      });
      console.log("Sending registration e-mails to ... " + user.email);
    }
    var smile = body.events.length ? '>:)' : ':(';
    console.log('Sent out ' +body.events.length+ ' spam-mails. '+ smile);
  });
}, 5000);


