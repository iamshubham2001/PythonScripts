import subprocess

service_name = "nginx"  # Change this to the name of the service you want to monitor

# check service status
status = subprocess.run(
    ["systemctl", "is-active", service_name],
    capture_output=True,
    text=True
)

if status.stdout.strip() == "active":
    print(f"{service_name} is running.")
else:
    print(f"{service_name} is not running.")
    print("Restarting the service...")

    # Attempt to restart the service123456
    restart = subprocess.run(
        ["sudo", "systemctl", "restart", service_name],
    )

    # Check if the restart command was successful
    new_status = subprocess.run(
        ["systemctl", "is-active", service_name],
        capture_output=True,
        text=True
    )
    
    if restart.returncode == 0:
        print(f"{service_name} has been restarted successfully.")
    else:
        print(f"Failed to restart {service_name}. Please check the service status manually.")   