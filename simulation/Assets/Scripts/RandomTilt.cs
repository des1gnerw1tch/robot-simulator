using UnityEngine;

// On start, rotates this object to a random angle around the X and Z axes.
public class RandomTilt : MonoBehaviour
{
    [Tooltip("Maximum tilt in degrees, applied in either direction on each axis.")]
    [Range(0f, 180f)]
    public float maxAngle = 15f;

    void Start()
    {
        float x = Random.Range(-maxAngle, maxAngle);
        float z = Random.Range(-maxAngle, maxAngle);
        transform.rotation = Quaternion.Euler(x, transform.eulerAngles.y, z);
    }
}
