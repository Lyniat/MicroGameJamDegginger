using UnityEngine;
using SocketIO;
using System.Collections;

public class SocketInput : MonoBehaviour
{
    public void Start()
    {
        socket = GetComponent<SocketIOComponent>();

        socket.On("connect", OnConnect);
        socket.On("input", OnInput);
        socket.On("position", OnPosition);
    }

    public void OnConnect(SocketIOEvent e)
    {
        socket.Emit("register", new JSONObject("\"game\""));
    }

    public void OnInput(SocketIOEvent e)
    {
        Debug.Log(string.Format("Name: {0}, Data: {1}", e.name, e.data));
    }

    public void OnPosition(SocketIOEvent e)
    {
        Debug.Log("Position received");
    }

    private SocketIOComponent socket;
}