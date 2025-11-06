# Simulate robot response
# robot_model.py


import numpy as np

import roboticstoolbox as rtb
from spatialmath import SE3


robot = rtb.models.DH.Puma560()

def simulate_response(joint_traj, deviation_mm=1.0):
    measured_tcp = []
    for q in joint_traj:
        tcp = robot.fkine(q).t
        noise = np.random.normal(loc=0.0, scale=deviation_mm / 1000.0, size=3)  # mm to meters
        tcp_noisy = tcp + noise
        measured_tcp.append(tcp_noisy.tolist())

    motor_positions = joint_traj[-1].tolist()
    return measured_tcp, motor_positions
