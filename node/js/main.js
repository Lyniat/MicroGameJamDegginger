var App = App || {};
App.Main = function () {
    var that = {},
        interface,
        socket;

    function init() {
        interface = new App.Interface(that);
        socket = new App.Socket(that);
    }
    
    function sendInput(key,state) {
        console.log(key,state);
        socket.sendInput(key,state);
    }

    function setPosition(position){
        interface.setPosition(position);
    }

    init();
    that.setPosition = setPosition;
    that.sendInput = sendInput;
    return that;
};

var Input = {};
Input.LEFT = 'left';
Input.RIGHT = 'right';
Input.ACTION = 'action';
Input.DOWN = 'down';
Input.UP = 'up';