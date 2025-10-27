from utils.sensor_simulator import inject_force
from utils.hardware_inference import evaluate_force_response
import pandas as pd
from datetime import datetime
import os

def log_result(test_name, input_data, status, result):
    """log test result to csv. """

    # Extract known fields from input_data
    x = input_data.get("x", "")
    y = input_data.get("y", "")
    z = input_data.get("z", "")
    obj = input_data.get("object", "")
    distance = input_data.get("distance", "")

    log_entry={
        "timestamp": datetime.now(),
        "test_name": test_name,
        "x":x,
        "y":y,
        "z":z,
        "object":obj,
        "distance":distance, 
        "status": status,
        "result": result
    }
    log_path="logs/test_results.csv"
    df= pd.DataFrame([log_entry])

    # Add header only if file doesnt exist
    write_header=not os.path.exists(log_path)
    df.to_csv(log_path, mode='a', header=write_header, index=False)


def test_emergency_stop_on_contact():
    "simulate a force spike"
    force = inject_force(z=60)

    #evaluate robot response
    status=evaluate_force_response(force)

    #determine oass/fail
    result="PASS" if status=="STOPPED" else "Fail"

    print(f"[Sensor] Injected force: {force}")
    print(f"[Robot] Emergency stop triggered by force.")
    print(result)

    #log the result
    log_result("emergency Stop on Force", force, status, result)

    "Assert for test automation"
    assert status=="STOPPED"
