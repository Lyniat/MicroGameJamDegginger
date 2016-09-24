using UnityEngine;
using System.Collections;
using SocketIO;

public class Interface : MonoBehaviour {

    public Rigidbody player_0;
    public Rigidbody player_1;

	public void Start()
    {
        socket = GetComponent<SocketIOComponent>();

        socket.On("connect", OnConnect);
        socket.On("ping", OnPing);
        socket.On("input", OnInput);
    }

    public void OnConnect(SocketIOEvent e)
    {
        socket.Emit("register", new JSONObject("\"game\""));

        Debug.Log("Connected to input server");
    }

    public void OnPing(SocketIOEvent e)
    {
        socket.Emit("ping");

        Debug.Log("Ping received");
    }

    public void OnInput(SocketIOEvent e)
    {
        var user = e.data["user"];
        var key = e.data["key"];
        var state = e.data["state"];

        switch (key.str)
        {
            case "left":
                left = state.str.Equals("down");
                break;
            case "right":
                right = state.str.Equals("down");
                break;
            case "action":
                action = state.str.Equals("down");
                break;
        }

        Debug.Log(string.Format("Input received: {0}", e.data));
    }

    public bool Left { get { return left; } }
    private bool left;

    public bool Action { get { return action; } }
    private bool action;

    public bool Right { get { return right; } }
    private bool right;

    private SocketIOComponent socket;

	public void Update(){
		if(left){
			player_0.velocity = new Vector3(0,20,0);
		}
		if(right){
			player_1.velocity = new Vector3(0,20,0);
		}
	}

}
