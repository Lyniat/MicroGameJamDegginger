var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

var users = [];
var game;

io.on('connection', function(socket){
    console.log('a user connected');
    var user = {};
    user.socket = socket;
    users.push(user);

    user.socket.on('input', function(msg){
        console.log('socket '+getUserID(user)+' sent: ' + msg.key +' '+msg.direction +' to game.');
        sendInput(user,msg);
    });

    user.socket.on('register', function(){
        console.log('game registered.');
        var g = {};
        g.socket = socket;
        game = g;
        removeUser(users,user);
    });
});

http.listen(3000, function(){
    console.log('listening on *:3000');
});

function removeUser(user){
    function remove(array, user) {
        for(var i = array.length; i--;) {
            if(array[i] === user) {
                array.splice(i, 1);
                console.log('removed user '+i);
                return;
            }
        }
        console.log('user to remove not found!');
    }
}

function getUserID(user){
    for(var i = 0; i < users.length; i++){
        if(users[i] === user) {
            return i;
        }
    }
}

function sendInput(user,input){
    if(!game){
        console.log("got input but no game registered!");
        return;
    }
    var id = getUserID(user);
    var string = 'user '+id+' '+input;
    var object = {user:id, key:input.key, direction:input.direction};
    console.log(string);
    game.socket.emit('input',object);
}

var Input = {};
Input.LEFT = 'left';
Input.RIGHT = 'right';
Input.ACTION = 'action';
Input.DOWN = 'down';
Input.UP = 'up';