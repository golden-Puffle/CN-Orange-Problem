import subprocess
import re

def measure_rtt():
    result = subprocess.run(
        ["ping", "-c", "5", "10.0.0.2"],
        capture_output=True,
        text=True
    )

    output = result.stdout
    print(output)

    match = re.search(r"rtt min/avg/max/mdev = (.*) ms", output)
    if match:
        values = match.group(1).split("/")
        print("\nRTT Values:")
        print(f"Min: {values[0]} ms")
        print(f"Avg: {values[1]} ms")
        print(f"Max: {values[2]} ms")

measure_rtt()
