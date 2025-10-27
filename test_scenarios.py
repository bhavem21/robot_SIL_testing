from utils.sensor_simulator import inject_force, simulate_camera_input
from utils.hardware_inference import evaluate_force_response, evaluate_camera_response
from tests.test_force_control import log_result
import random

def run_force_tests():
    for z in range (0,100,10):
        force=inject_force(z=z)
        status=evaluate_force_response(force)
        result="PASS" if (z>=50 and status=="STOPPED") or (z<50 and status =="MOVING") else "FAIL"
        log_result("Force Test", force, status, result)

def run_camera_tests():
    objects=["none", "human", "box"]
    for _ in range (30):
        obj =random.choice(objects)
        distace=round(random.uniform(0.2,2.0),2)
        detection=simulate_camera_input(object_detected=obj, distance=distace)
        status=evaluate_camera_response(detection)

        if obj=="human" and distace < 0.5:
            expected="STOPPED"

        elif obj=="box" and distace <1.0:
            expected="REROUTING"
        
        elif obj !="none":
            expected="MOVING"
        else:
            expected="MOVING"

        result ="PASS" if status==expected else "FAIL"
        log_result("Camera Test", detection, status, result)

