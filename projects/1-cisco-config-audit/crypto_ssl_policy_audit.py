from netmiko import ConnectHandler
from getpass import getpass

# Ask credentials securely
username = input("Username: ").strip()
password = getpass("Password: ")

DEVICE_IPS = ["10.101.1.217", "10.101.1.218"]

for ip in DEVICE_IPS:

    print(f"Connecting to {ip}...")

    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": username,
        "password": password,
    }

    connection = ConnectHandler(**device)

    output = connection.send_command(
        "show running-config | section crypto ssl policy"
    )

    connection.disconnect()

    filename = f"{ip}.txt"

    with open(filename, "w") as f:
        f.write(f"Device: {ip}\n")
        f.write("Command: show running-config | section crypto ssl policy\n")
        f.write("=" * 60 + "\n\n")
        if output.strip() == "":
           f.write("No crypto ssl policy configuration found.\n")
        else:
           f.write(output)
        

    print(f"Saved {filename}")

