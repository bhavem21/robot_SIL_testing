Overview
The PITT (Programmable Intelligent Test Toolkit) automated test suite is designed to validate robotic control systems in a Hardware-in-the-Loop (HIL) environment. It simulates sensor inputs, infers hardware responses, and logs structured test data for analysis in Power BI.

Key Features:
1. Sensor Simulation: Emulates force sensors and camera inputs to test robot behavior under controlled conditions.

2. Hardware Inference: Evaluates expected robot responses (e.g., STOPPED, MOVING, REROUTING) based on input logic.

3. Automated Logging: Captures test metadata and sensor values in a structured CSV format.

4. Power BI Integration: Enables real-time analytics and visualization of test outcomes, sensor trends, and failure diagnostics.

Test Workflow
1. Input Generation
    Simulated force: {"x": 0, "y": 0, "z": 45}
    Simulated camera: {"object": "human", "distance": 0.4}

2. Behavior Evaluation:
    Logic determines robot status:
        Human too close → STOPPED
        Box within 1m → REROUTING
        Clear path → MOVING
3. Result Logging
        Each test logs:
        Timestamp
        Test name
        Sensor inputs (x, y, z, object, distance)
        Robot status
        Pass/Fail result

CSV Output
File: logs/test_results.csv

