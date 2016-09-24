var App = App || {};
App.Main = function () {
    var that = {},
        interface,
        socket;

    function init() {
        interface = new App.Interface(that);
        socket = new App.Socket();
    }
    
    function sendInput(key,direction) {
        console.log(key,direction);
        socket.sendInput(key,direction);
    }

    init();
    that.sendInput = sendInput;
    return that;
};

var Input = {};
Input.LEFT = 'left';
Input.RIGHT = 'right';
Input.ACTION = 'action';
Input.DOWN = 'down';
Input.UP = 'up';