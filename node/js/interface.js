var App = App || {};
App.Interface = function (m) {
    var that = {},
        main;

    function init(){
        main = m;
        addListeners();
    }

    function addListeners(){
        $('#button-left')[0].addEventListener("mousedown", buttonLeftDown);
        $('#button-action')[0].addEventListener("mousedown", buttonActionDown);
        $('#button-right')[0].addEventListener("mousedown", buttonRightDown);

        $('#button-left')[0].addEventListener("mouseup", buttonLeftUp);
        $('#button-action')[0].addEventListener("mouseup", buttonActionUp);
        $('#button-right')[0].addEventListener("mouseup", buttonRightUp);
    }

    function buttonLeftDown(){
        main.sendInput(Input.LEFT,Input.DOWN);
    }

    function buttonActionDown(){
        main.sendInput(Input.ACTION,Input.DOWN);
    }

    function buttonRightDown(){
        main.sendInput(Input.RIGHT,Input.DOWN);
    }

    function buttonLeftUp(){
        main.sendInput(Input.LEFT,Input.UP);
    }

    function buttonActionUp(){
        main.sendInput(Input.ACTION,Input.UP);
    }

    function buttonRightUp(){
        main.sendInput(Input.RIGHT,Input.UP);
    }


init(m);
    return that;
};