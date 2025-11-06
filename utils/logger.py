#logs result to csv
# utils/logger.py

import os
import csv

def log_result(name, ref_tcp, measured_tcp, deviation, status, velocity):
    file_path = "log_results/model_results.csv"
    file_exists = os.path.isfile(file_path)

    # ✅ Fix: specify encoding='utf-8'
    with open(file_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow([
                "test_case", "ReferenceTCP", "MeasuredTCP",
                "VelocityProfile", "Deviation_mm", "Pass"
            ])
        writer.writerow([
            name, ref_tcp, measured_tcp, velocity, deviation, status
        ])
