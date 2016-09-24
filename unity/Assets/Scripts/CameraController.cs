using UnityEngine;
using System.Collections;

public class CameraController : MonoBehaviour
{
	public void Start()
	{
		player = LevelManager.Current.Player.gameObject.transform;
	}

    public void Update()
	{
        // Lerp rotation
        var pos = player.position - transform.position;
		var newRot = Quaternion.LookRotation(pos);
		transform.rotation = Quaternion.Lerp(transform.rotation, newRot, Time.deltaTime * 5f);

		// Set targetPosition
		switch (LevelManager.Current.CurrentScene)
		{
			case SceneEnum.North:
                targetPosition = new Vector3(player.position.x, player.position.y, player.position.z - 10f);
                break;
			case SceneEnum.East:
                targetPosition = new Vector3(player.position.x - 10f, player.position.y, player.position.z);
                break;
			case SceneEnum.South:
                targetPosition = new Vector3(player.position.x, player.position.y, player.position.z + 10f);
                break;
			case SceneEnum.West:
                targetPosition = new Vector3(player.position.x + 10f, player.position.y, player.position.z);
                break;
        }

        // Lerp position
        transform.position = Vector3.Lerp(transform.position, targetPosition, Time.deltaTime * 5f);
    }

	private Vector3 targetPosition;
    private Transform player;
}