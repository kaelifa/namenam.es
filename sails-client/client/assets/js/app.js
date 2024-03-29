/**
 * app.js
 *
 * This file contains some conventional defaults for working with Socket.io + Sails.
 * It is designed to get you up and running fast, but is by no means anything special.
 *
 * Feel free to change none, some, or ALL of this file to fit your needs!
 */


(function (io) {

  // as soon as this file is loaded, connect automatically, 
  var socket = io.connect();
  if (typeof console !== 'undefined') {
    log('Connecting to Sails.js...');
  }
  
  function bindForm() {
    $('#addUser button.add').click(
      function() {
        $.post('/Name/create',  {
          label: $('#label').val()
        }, function(data) {
          $('#label').val();
        });
      }
    );
  }
  
  function createName() {
    
  }
  
  function drawNames(data) {
    var $nameList = $('#nameList');
    $nameList.empty();
    var newItem;
    
    for(var i = 0; i < data.length; i++) {
        newItem = $('<li />');
        newItem.text(data[i].label);
        
        $nameList.append(newItem);
    }    
  }

  socket.on('connect', function socketConnected() {
    
    log('requesting data');
    
    bindForm();
    
    socket.request('/Name', {}, function(data) {
      log('request');
      log(data);
      
      drawNames(data);
    });

    // Listen for Comet messages from Sails
    socket.on('message', function messageReceived(message) {

      ///////////////////////////////////////////////////////////
      // Replace the following with your own custom logic
      // to run when a new message arrives from the Sails.js
      // server.
      ///////////////////////////////////////////////////////////
      log('New comet message received :: ', message);
      //////////////////////////////////////////////////////

      if((message.model === 'name') && (message.verb === 'create')) {
        newItem = $('<li />');
        newItem.text(message.data.label);
        
         $('#nameList').append(newItem);
      }
    });


    ///////////////////////////////////////////////////////////
    // Here's where you'll want to add any custom logic for
    // when the browser establishes its socket connection to 
    // the Sails.js server.
    ///////////////////////////////////////////////////////////
    log(
        'Socket is now connected and globally accessible as `socket`.\n' + 
        'e.g. to send a GET request to Sails, try \n' + 
        '`socket.get("/", function (response) ' +
        '{ console.log(response); })`'
    );
    ///////////////////////////////////////////////////////////


  });


  // Expose connected `socket` instance globally so that it's easy
  // to experiment with from the browser console while prototyping.
  window.socket = socket;


  // Simple log function to keep the example simple
  function log () {
    if (typeof console !== 'undefined') {
      console.log.apply(console, arguments);
    }
  }
  

})(

  // In case you're wrapping socket.io to prevent pollution of the global namespace,
  // you can replace `window.io` with your own `io` here:
  window.io

);
