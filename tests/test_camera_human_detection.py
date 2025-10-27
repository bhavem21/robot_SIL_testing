from utils.sensor_simulator import simulate_camera_input
from utils.hardware_inference import evaluate_camera_response
from tests.test_force_control import log_result

def test_stop_on_human_detection():
    detection=simulate_camera_input(object_detected="human", distance=0.3)
    status=evaluate_camera_response(detection)
    result="PASS" if status=="STOPPED" else "FAIL"

    print(f"[Camera] Detected: {detection}")
    print(f"[Robot] Response: {status}")
    print(result)

    log_result("stop on Human Detection", detection, status, result)
    assert status =="STOPPED"

