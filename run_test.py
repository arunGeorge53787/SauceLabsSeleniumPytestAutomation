import os
import subprocess
import datetime
from pathlib import Path

# Create reports directory if it doesn't exist
reports_dir = Path("Test_reports")  # Ensure consistency with GitHub Actions
reports_dir.mkdir(exist_ok=True)  # Equivalent to os.makedirs(reports_dir, exist_ok=True)

# Generate filename with current date and time
current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
report_path = reports_dir / f"test_report_{current_datetime}.html"

if __name__ == "__main__":
    print(f"Running tests and generating report at: {report_path}")

    # Run pytest directly without activating a virtual environment
    result = subprocess.run(
        ["pytest", f"--html={report_path}", "--self-contained-html"],
        capture_output=True,
        text=True
    )

    # Print stdout and stderr for debugging
    print(result.stdout)
    print(result.stderr)

    # Verify if the test report is generated
    if report_path.exists():
        print(f"✅ Test report generated: {report_path}")
    else:
        print(f"❌ Test report NOT generated: {report_path}")
