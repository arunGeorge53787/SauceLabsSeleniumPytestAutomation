import os
import subprocess
#import pytest
import datetime
from pathlib import Path

# Create reports directory if it doesn't exist
reports_dir = Path("Test_Reports")
if not os.path.exists(reports_dir):
    os.makedirs(reports_dir)

# Generate filename with current date and time
current_datetime = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
report_path = f"{reports_dir}/test_report_{current_datetime}.html"

if __name__ == "__main__":
    venv='sl_env'
    print(f"Running tests and generating report at: {report_path}")
    # Pass arguments as pytest plugins expect them
    subprocess.run(f"source {venv}/bin/activate && pytest --html={report_path} --self-contained-html", shell=True, executable="/bin/bash")
    #subprocess.run(["pytest", f"--html={report_path}", "--self-contained-html"])
    if os.path.exists(report_path):
        print(f"Test report generated: {report_path}")
    else:
        print(f"Test report not generated: {report_path}")