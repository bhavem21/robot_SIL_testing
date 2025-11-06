Overview

This project implements a Python-based automated testing framework for evaluating the performance of a robot controller against a simulated robot model. It uses a simulation-in-loop (SiL) approach to validate whether the controller-generated joint trajectories result in accurate end-effector (TCP) positions when executed on the robot's physical model.

The framework is designed for function-level evaluation, enabling precise comparison between the controller output and the simulated robot response under various test conditions.

Simulation-in-Loop Workflow
Each test case follows a structured loop:

Test Configuration
    Test cases are defined in `test_config.yaml` and include:
    **Initial joint angles**: Specifies the robot's starting configuration for each test.
    **Target TCP pose**: Defines the desired end-effector position in Cartesian space.
    **Velocity profile**: Controls the speed of trajectory execution (`slow`, `medium`, or `fast`).
    **Workspace coverage**: Test cases are distributed across different regions of the robot's workspace to evaluate controller performance under varied spatial conditions.
    **Deviation threshold**: A configurable limit (in mm) used to determine pass/fail status based on TCP accuracy.

Controller Execution (compute_control)
    Solves inverse kinematics for the target pose
    Generates a joint-space trajectory using jtraj()
    Computes the reference TCP path via forward kinematics

Robot Simulation (simulate_response)

    Uses the same joint trajectory to simulate robot motion
    Adds small deviations to mimic real-world imperfections
    Computes the measured TCP path from simulated joint states

Function Evaluation
    Compares reference and measured TCP paths
    Calculates deviation using Hausdorff distance or RMSE
    Validates against a configurable threshold

Logging and Reporting
    Records test name, reference and measured TCPs, deviation, pass/fail status, and velocity profile


The framework supports automated test execution using pytest:
python run_tests.py

Example Assertion
assert deviation <= threshold_mm, f"{test['name']} failed: deviation={deviation:.2f} mm"


Key Features
    Function-level evaluation of robot controller output
    Simulation-in-loop testing with realistic deviations
    Python automation for scalable test execution
    Deviation metrics using Hausdorff and RMSE
    Pytest integration for clean reporting and CI compatibility