using UnityEngine;
using System.Collections;

public class PlayerController : MonoBehaviour
{
    public void Start()
    {
        input = LevelManager.Current.Input;
    }

    public void Update()
    {
        if (Input.GetKey(KeyCode.A) || input.Left)
        {
            MoveLeft();
        }

        if (Input.GetKey(KeyCode.D) || input.Right)
        {
            MoveRight();
        }

        if (Input.GetKey(KeyCode.S) || input.Action)
        {
            // TODO: Action
        }
    }

    private void MoveLeft()
    {
		switch (LevelManager.Current.CurrentScene)
		{
			case SceneEnum.North:
				transform.position = new Vector3(transform.position.x - 0.1f, transform.position.y, transform.position.z);
                break;
			case SceneEnum.East:
				transform.position = new Vector3(transform.position.x, transform.position.y, transform.position.z + 0.1f);
                break;
			case SceneEnum.South:
				transform.position = new Vector3(transform.position.x + 0.1f, transform.position.y, transform.position.z);
                break;
			case SceneEnum.West:
				transform.position = new Vector3(transform.position.x, transform.position.y, transform.position.z - 0.1f);
                break;
        }
    }

    private void MoveRight()
	{
		switch (LevelManager.Current.CurrentScene)
		{
			case SceneEnum.North:
				transform.position = new Vector3(transform.position.x + 0.1f, transform.position.y, transform.position.z);
                break;
			case SceneEnum.East:
				transform.position = new Vector3(transform.position.x, transform.position.y, transform.position.z - 0.1f);
                break;
			case SceneEnum.South:
				transform.position = new Vector3(transform.position.x - 0.1f, transform.position.y, transform.position.z);
                break;
			case SceneEnum.West:
				transform.position = new Vector3(transform.position.x, transform.position.y, transform.position.z + 0.1f);
                break;
        }
	}

	private SocketInput input;
}