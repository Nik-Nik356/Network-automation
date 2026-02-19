import napalm
from getpass import getpass

username = input("Username: ").strip()
password = getpass("Password: ")

DEVICE_IPS = ["10.101.1.214", "10.101.1.218"]

# Open file in write mode
with open("device_facts.txt", "w") as file:

    for devices in DEVICE_IPS:

        driver = napalm.get_network_driver("ios")

        device = driver(
            hostname=devices,
            username=username,
            password=password,
        )

        try:
            device.open()
            facts = device.get_facts()

            file.write(f"\n===== Device: {devices} =====\n")
            file.write(f"\n===== Device: {devices} =====\n")
            file.write(f"Hostname   : {facts['hostname']}\n")
            file.write(f"Model      : {facts['model']}\n")
            file.write(f"OS Version : {facts['os_version']}\n")
            file.write(f"Uptime     : {facts['uptime']}\n")
            file.write(f"Serial Number : {facts['serial_number']}\n")
            
            print(f"Saved facts for {devices}")

        except Exception as e:
            file.write(f"\nERROR connecting to {devices}: {e}\n")
            print(f"Failed for {devices}")

        finally:
            device.close()

print("All done. Check device_facts.txt")