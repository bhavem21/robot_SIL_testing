# 🤖 Robot Controller Testing Framework

## Overview

This project implements a **Python-based automated testing framework** for evaluating the performance of a robot controller against a simulated robot model. It uses a **simulation-in-loop (SiL)** approach to validate whether the controller-generated joint trajectories result in accurate end-effector (TCP) positions when executed on the robot's physical model.

The framework is designed for **function-level evaluation**, enabling precise comparison between the controller output and the simulated robot response under various test conditions.

---

##  Simulation-in-Loop Workflow

Each test case follows a structured loop:

1. **Test Configuration**
   - Defined in `test_config.yaml`
   - Includes initial joint angles, target TCP pose, and velocity profile

2. **Controller Execution (`compute_control`)**
   - Solves inverse kinematics for the target pose
   - Generates a joint-space trajectory using `jtraj()`
   - Computes the reference TCP path via forward kinematics

3. **Robot Simulation (`simulate_response`)**
   - Uses the same joint trajectory to simulate robot motion
   - Adds small deviations to mimic real-world imperfections
   - Computes the measured TCP path from simulated joint states

4. **Function Evaluation**
   - Compares reference and measured TCP paths
   - Calculates deviation using Hausdorff distance or RMSE
   - Validates against a configurable threshold

5. **Logging and Reporting**
   - Records test name, reference and measured TCPs, deviation, pass/fail status, and velocity profile

---

##  Test Configuration Format

Test cases are defined in `test_config.yaml`:

```yaml
deviation_threshold_mm: 10
tests:
  - name: "Test 1"
    joint_angles: [0, 0, 0, 0, 0, 0]
    target_pose: [0.3, -0.4, 0.5]
    velocity_profile: "medium"
  - name: "Test 2"
    joint_angles: [0.1, -0.2, 0.3, -0.1, 0.2, -0.3]
    target_pose: [0.25, -0.35, 0.45]
    velocity_profile: "fast"


## Pytest Integration

```bash
pytest run_tests.py


## Example Assertion
assert deviation <= threshold_mm, f"{test['name']} failed: deviation={deviation:.2f} mm"


## Key Features:

Function-level evaluation of robot controller output

Simulation-in-loop testing with realistic deviations

Python automation for scalable test execution

Deviation metrics using Hausdorff and RMSE

Pytest integration for clean reporting and CI compatibility
