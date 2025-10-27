from utils.sensor_simulator import simulate_camera_input
from utils.hardware_inference import evaluate_camera_response
from tests.test_force_control import log_result

def test_continue_on_clear_path():
    detection=simulate_camera_input(object_detected="none", distance=1.5)
    status=evaluate_camera_response(detection)
    result="PASS" if status=="MOVING" else "FAIL"

    print(f"[Camera] Detected :{detection}")
    print(f"[Robot] Response: {status}")
    print(result)

    log_result("Continue on clear Path", detection, status, result)
    assert status=="MOVING"