var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

var users = [];
var game;

io.on('connection', function (socket) {
    console.log('a user connected');
    var user = {};
    user.socket = socket;

    user.socket.on('input', function (msg) {
        console.log('socket ' + getUserID(user) + ' sent: ' + msg.key + ' ' + msg.state + ' to game.');
        sendInput(user, msg);
    });

    user.socket.on('register', function (msg) {
        if(msg == 'game') {
            console.log('game registered.');
            var g = {};
            g.socket = socket;
            game = g;
            user = {};
        }else if(msg == 'player'){
            users.push(user);
            sendPosition(user);
        }
    });

    user.socket.on('disconnect', function () {
        console.log('a user disconnected');
        removeUser(user);
    });

    user.socket.on('ping-player', function () {
        console.log("try ping");
        if(game){
            game.socket.emit('ping');
            game.socket.on('ping', function () {
                console.log("got ping");
                user.socket.emit('ping');
            });
        }
    });
});

http.listen(3000, function () {
    console.log('listening on *:3000');
});

function removeUser(user) {
    for (var i = users.length; i--;) {
        if (users[i] === user) {
            users.splice(i, 1);
            console.log('removed user ' + i);
            updateUserPositions();
            return;
        }
    }
    console.log('user to remove not found!');
}

function getUserID(user) {
    for (var i = 0; i < users.length; i++) {
        if (users[i] === user) {
            return i;
        }
    }
}

function sendInput(user, input) {
    if (!game) {
        console.log("got input but no game registered!");
        return;
    }
    var id = getUserID(user);
    var string = 'user ' + id + ' ' + input;
    var object = {user: id, key: input.key, state: input.state};
    console.log(string);
    game.socket.emit('input', object);
}

function sendPosition(user) {
    var id = getUserID(user);
    user.socket.emit('position', id);
}

function updateUserPositions() {
    for (var i = 0; i < users.length; i++) {
        sendPosition(users[i]);
    }
}

var Input = {};
Input.LEFT = 'left';
Input.RIGHT = 'right';
Input.ACTION = 'action';
Input.DOWN = 'down';
Input.UP = 'up';