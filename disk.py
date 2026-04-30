import subprocess
# subprocess.run(["ls", "-l"])

# Run the "df -h" command to get disk usage information
result = subprocess.run(["df", "-h"], capture_output=True, text=True)
# print(result.stdout) # Print the output of the command

output = result.stdout

alert_count = 0
for line in output.splitlines():
    if line:
        if line.split() == "" or line.startswith("Filesystem"):
            continue # Skip empty lines and the header line

        parts = line.split()

        if len(parts) < 6:
            continue # Skip lines that don't have enough parts
        
        filesystem = parts[0]
        usage = parts[4]

        # extra safety
        if "%" not in usage:
            continue # Skip lines where the usage percentage is not in the expected format
        
        # Remove the percentage sign and convert to an integer
        usage_percent = int(usage.replace("%", "") )

        if usage_percent >= 80:
            print(f"Alert: {filesystem} usage is {usage}")
            alert_count += 1

# Final summary
print(f"Total alerts: {alert_count}")