def inject_force(x=0, y=0, z=0):
    """Simulate a force sensor input."""
    force_vector = {"x": x, "y": y, "z": z}
    print(f"[Sensor] Injected force: {force_vector}")
    return force_vector

def simulate_camera_input(object_detected="none", distance=1.0):
    """Simulate a camera detecting an object (e.g., human or box)."""
    detection = {"object": object_detected, "distance": distance}
    print(f"[Camera] Detected: {detection}")
    return detection