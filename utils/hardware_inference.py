def evaluate_force_response(force_vector):
    """Determine robot behavior based on force input."""
    threshold = 50  # Newtons
    if abs(force_vector["z"]) >= threshold:
        print("[Robot] Emergency stop triggered by force.")
        return "STOPPED"
    else:
        print("[Robot] Normal operation.")
        return "MOVING"

def evaluate_camera_response(detection):
    """Determine robot behavior based on camera input."""
    obj = detection["object"]
    dist = detection["distance"]

    if obj == "human" and dist < 0.5:
        print("[Robot] Human too close — stopping.")
        return "STOPPED"
    
    elif obj == "box" and dist < 1.0:
        print("[Robot] Box detected within range — rerouting.")
        return "REROUTING"
    
    elif obj != "none":
        print("[Robot] Object detected but safe — continuing.")
        return "MOVING"
    
    else:
        print("[Robot] Path clear.")
        return "MOVING"
