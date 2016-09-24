using UnityEngine;
using System.Collections;

public class Ball : MonoBehaviour {

	// Use this for initialization
	void Start () {
	    GetComponent<Rigidbody>().velocity = new Vector3(8,8,0);
	}
	
	// Update is called once per frame
	void Update () {
float old = GetComponent<Rigidbody>().velocity.y;
		float vel = GetComponent<Rigidbody>().velocity.x;
		 if(vel < 8 && vel > 0){
			GetComponent<Rigidbody>().velocity = new Vector3(8,0,old);
			}

		if(vel > 0 && vel < -8){
			GetComponent<Rigidbody>().velocity = new Vector3(-8,0,old);
			}
	}
}
