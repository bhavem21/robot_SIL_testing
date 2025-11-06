import numpy as np
from spatialmath import SE3
import roboticstoolbox as rtb
robot = rtb.models.DH.Puma560()


def compute_control(joint_angles, target_pose, velocity_profile):
    q_start = np.array(joint_angles).reshape(-1)
    T_target = SE3(*target_pose)

    ik_result = robot.ikine_LM(T_target)
    if not ik_result.success:
        raise ValueError(f"IK failed for target pose: {target_pose}")
    q_target = np.array(ik_result.q).reshape(-1)

    steps = {"slow": 100, "medium": 50, "fast": 20}.get(velocity_profile, 50)
    traj = rtb.jtraj(q_start, q_target, steps)

    reference_tcp = [robot.fkine(q).t.tolist() for q in traj.q]
    return reference_tcp, traj.q
