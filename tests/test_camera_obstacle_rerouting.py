from utils.sensor_simulator import simulate_camera_input
from utils.hardware_inference import evaluate_camera_response
from tests.test_force_control import log_result

def test_reroute_on_obstacle():
    detection=simulate_camera_input(object_detected="box", distance=0.3)
    status=evaluate_camera_response(detection)
    result="PASS" if status=="REROUTING" else "FAIL"

    print(f"[Camera] Detected:{detection}")
    print(f"[Robot] Response:{status}")
    print(result)

    log_result("Reroute on Obstacle Detection", detection, status, result)
    assert status=="REROUTING"