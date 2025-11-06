import pytest
import numpy as np
from model_interface import (
    load_test_cases,
    compute_control,
    simulate_response,
    compute_hausdorff
)

# Load test cases from YAML
test_config = load_test_cases()
threshold_mm = test_config.get("deviation_threshold_mm", 10)
test_cases = test_config["tests"]

@pytest.mark.parametrize("test", test_cases)
def test_robot_tcp_deviation(test):
    velocity = test.get("velocity_profile", "medium")

    # Run control and simulation
    ref_tcp, joint_traj = compute_control(test["joint_angles"], test["target_pose"], velocity)
    measured_tcp, motor_pos = simulate_response(joint_traj, deviation_mm=1.0)

    # Compute deviation
    deviation = compute_hausdorff(ref_tcp, measured_tcp)

    # Assert deviation is within threshold
    assert deviation <= threshold_mm, f"{test['name']} failed: deviation={deviation:.2f} mm"
