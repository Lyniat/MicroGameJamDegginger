var App = App || {};
App.Socket = function(){
  var that = {},
      IP = 'http://localhost:3000',
      socket;

  function init(){
      socket = io.connect(IP, {reconnect: true});

      socket.on('connect', function (socket) {
          console.log('Connected!');
      });
  }

  function sendInput(key,direction) {
      var content = {key:key,direction:direction};
      console.log(content);
      socket.emit('input',content);
  }

  init();
  that.sendInput = sendInput;
  return that;
};
