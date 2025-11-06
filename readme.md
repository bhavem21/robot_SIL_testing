Robot Controller Testing Framework

Overview:

This project implements a Python-based automated testing framework for evaluating the performance of a robot controller against a simulated robot model. It uses a simulation-in-loop (SiL) approach to validate whether the controller-generated joint trajectories result in accurate end-effector (TCP) positions when executed on the robot's physical model. The framework is designed for function-level evaluation, enabling precise comparison between the controller output and the simulated robot response under various test conditions.

Simulation-in-Loop Workflow
Each test case follows a structured loop that begins with loading configuration data from a YAML file. The configuration includes the robot's initial joint angles, the target TCP pose in Cartesian space, and a velocity profile that controls the speed of trajectory execution. Test cases are distributed across different regions of the robot's workspace to ensure broad spatial coverage and to evaluate controller performance under varied conditions. A deviation threshold, defined in millimeters, is used to determine whether the measured TCP path is acceptably close to the reference path.

The controller execution phase uses the compute_control function to solve inverse kinematics for the target pose and generate a joint-space trajectory using jtraj(). This trajectory is then used to compute the reference TCP path via forward kinematics.

In the simulation phase, the same joint trajectory is passed to the simulate_response function, which simulates robot motion and introduces small deviations to mimic real-world imperfections. The measured TCP path is computed from the simulated joint states.

Function evaluation compares the reference and measured TCP paths using metrics such as Hausdorff distance or root mean square error (RMSE). These metrics are validated against the configured threshold to determine pass or fail status.

Finally, the framework logs the results of each test case, including the test name, reference and measured TCP paths, deviation value, pass/fail status, and velocity profile.

Test Execution
The framework supports automated test execution using pytest. You can run all test cases by executing:
python run_tests.py

Each test includes an assertion to verify that the deviation remains within the acceptable threshold. For example:
assert deviation <= threshold_mm, f"{test['name']} failed: deviation={deviation:.2f} mm"

Key Features
This framework provides function-level evaluation of robot controller output using a simulation-in-loop methodology. It supports realistic deviation modeling, scalable test execution through Python automation, and robust deviation analysis using Hausdorff distance and RMSE. Integration with pytest ensures clean reporting and compatibility with continuous integration workflows.
