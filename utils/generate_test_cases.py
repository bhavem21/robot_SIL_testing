import random
import yaml
from roboticstoolbox.models.DH import Puma560
from spatialmath import SE3

# Load Puma 560 model
robot = Puma560()

# Define joint limits (in radians) for Puma 560 (6 DOF)
JOINT_LIMITS = {
    "min": [-2.79, -1.57, -2.79, -6.28, -2.79, -6.28],
    "max": [2.79, 1.57, 2.79, 6.28, 2.79, 6.28]
}

# Define workspace bounds for target TCP pose (in meters)
POSE_LIMITS = {
    "min": [0.1, -0.6, 0.0],
    "max": [0.8, 0.6, 0.8]
}

# Velocity profiles
VELOCITY_PROFILES = ["slow", "medium", "fast"]

def sample_joint_angles():
    return [
        round(random.uniform(JOINT_LIMITS["min"][i], JOINT_LIMITS["max"][i]), 2)
        for i in range(6)
    ]

def sample_target_pose():
    return [
        round(random.uniform(POSE_LIMITS["min"][i], POSE_LIMITS["max"][i]), 2)
        for i in range(3)
    ]

def sample_velocity():
    return random.choice(VELOCITY_PROFILES)

def is_reachable(pose):
    target = SE3(*pose)
    ik_result = robot.ikine_LM(target)
    return ik_result.success

def generate_test_cases(n=50, threshold_mm=10):
    test_cases = []
    attempts = 0
    while len(test_cases) < n and attempts < n * 5:
        joint_angles = sample_joint_angles()
        target_pose = sample_target_pose()
        if is_reachable(target_pose):
            test_cases.append({
                "name": f"TC{len(test_cases)+1}",
                "joint_angles": joint_angles,
                "target_pose": target_pose,
                "velocity_profile": sample_velocity()
            })
        attempts += 1

    config = {
        "deviation_threshold_mm": threshold_mm,
        "tests": test_cases
    }

    with open("test_config.yaml", "w") as f:
        yaml.dump(config, f, sort_keys=False)

    print(f"✅ Generated {len(test_cases)} reachable test cases in test_config.yaml")

# Run generator
if __name__ == "__main__":
    generate_test_cases(n=50)
