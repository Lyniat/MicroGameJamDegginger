var App = App || {};
App.Socket = function(m){
  var that = {},
      main,
      IP = '127.0.0.1:3000',
      socket,
      time;

  function init(m){
      main = m;

      socket = io.connect(IP, {reconnect: true});

      socket.on('connect', function (s) {
          socket.emit('register','player');
          console.log('Connected!');
          //testPing();
      });

      socket.on('position', function (position) {
          console.log('Received position '+position);
          main.setPosition(position);
      });
  }

  function sendInput(key,state) {
      var content = {key:key,state:state};
      console.log(content);
      socket.emit('input',content);
  }

  function testPing(){
      time = getTime();
      socket.emit('ping-player');
      socket.on('ping', function () {
          var secondTime = getTime();
          var delta = secondTime -time;
          console.log('ping: '+delta);
      });
      setTimeout(function(){
          testPing();
      }, 5000);
  }

  function getTime(){
      var d = new Date();
      var n = d.getTime();
      return n;
  }

  init(m);
  that.sendInput = sendInput;
  return that;
};
