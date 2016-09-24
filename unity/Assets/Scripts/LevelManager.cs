using UnityEngine;
using System.Collections;

public class LevelManager : MonoBehaviour
{
	public static LevelManager Current
	{
		get
		{
			if (current == null)
			{
                var go = GameObject.Find("LevelManager");
                current = go.GetComponent<LevelManager>();
            }

            return current;
        }
	}
    private static LevelManager current;

	[HideInInspector]
	public SceneEnum CurrentScene = SceneEnum.North;

    public SocketInput Input;
    public PlayerController Player;
}