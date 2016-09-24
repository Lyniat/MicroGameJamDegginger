using UnityEngine;
using System.Collections;

public class SceneTransitionTrigger : MonoBehaviour
{
    public SceneEnum SwitchToScene;

    public void OnTriggerEnter(Collider other)
	{
        Debug.Log("Scene transition triggered");
        LevelManager.Current.CurrentScene = SwitchToScene;
    }
}