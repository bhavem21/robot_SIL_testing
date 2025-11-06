#Runs tests and compares outputs 

# model_interface.py

import yaml
import numpy as np
from controller.controller import compute_control
from sim.sim_robot_model import simulate_response
from utils.logger import log_result
from scipy.spatial.distance import directed_hausdorff

def load_test_cases(path="test_config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def compute_deviation(ref_tcp, measured_tcp):
    return np.linalg.norm(np.array(ref_tcp[-1]) - np.array(measured_tcp[-1])) * 1000

def compute_hausdorff(ref_tcp, measured_tcp):
    ref = np.array(ref_tcp)
    meas = np.array(measured_tcp)
    d1 = directed_hausdorff(ref, meas)[0]
    d2 = directed_hausdorff(meas, ref)[0]
    return max(d1, d2) * 1000  # in mm

def compute_rmse(ref_tcp, measured_tcp):
    ref = np.array(ref_tcp)
    meas = np.array(measured_tcp)
    min_len = min(len(ref), len(meas))
    return np.sqrt(np.mean(np.sum((ref[:min_len] - meas[:min_len])**2, axis=1))) * 1000

def run_test_case(test, threshold_mm):
    velocity = test.get("velocity_profile", "medium")
    ref_tcp = compute_control(test["joint_angles"], test["target_pose"], velocity)
    ref_tcp, joint_traj = compute_control(test["joint_angles"], test["target_pose"], velocity)
    measured_tcp, motor_pos = simulate_response(joint_traj, deviation_mm=1.0)
    deviation = compute_hausdorff(ref_tcp, measured_tcp)
    pass_status = deviation <= threshold_mm
    log_result(test["name"], ref_tcp, measured_tcp, deviation, pass_status, velocity)

def run_all_tests():
    config = load_test_cases()
    threshold_mm = config.get("deviation_threshold_mm", 10)
    for test in config["tests"]:
        run_test_case(test, threshold_mm)

if __name__ == "__main__":
    run_all_tests()
