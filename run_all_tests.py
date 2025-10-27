from test_scenarios import run_force_tests, run_camera_tests

import csv

# Clear the log file and write headers
with open("logs/test_results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Test Name", "x", "y", "z", "object", "distance", "Status", "Result"])


    
if __name__=="__main__":
    run_force_tests()
    run_camera_tests()
    print("All Tests Cmpleted. ")