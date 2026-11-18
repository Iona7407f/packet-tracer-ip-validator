import ipaddress

devices = [
    {
        "name": "PC0",
        "ip": "168.20.0.10",
        "network": "168.20.0.0/16"
    },
    {
        "name": "PC1",
        "ip": "168.20.0.11",
        "network": "168.20.0.0/16"
    },
    {
        "name": "PC2",
        "ip": "192.50.50.12",
        "network": "192.50.50.0/24"
    },
    {
        "name": "PC3",
        "ip": "192.50.50.13",
        "network": "192.50.50.0/24"
    },
    {
        "name": "PC4",
        "ip": "168.20.0.14",
        "network": "168.20.0.0/16"
    }
]


def check_devices(device_list):
    seen_ips = {}
    failed_devices = 0

    for device in device_list:
        name = device["name"]
        errors = []

        try:
            ip_address = ipaddress.IPv4Address(device["ip"])
            subnet = ipaddress.IPv4Network(device["network"])
        except ValueError:
            print(f"{name}: ERROR - invalid IPv4 address or subnet")
            failed_devices += 1
            continue

        if ip_address not in subnet:
            errors.append(f"IP address {ip_address} is outside subnet {subnet}")

        if ip_address in seen_ips:
            previous_device = seen_ips[ip_address]
            errors.append(
                f"IP address {ip_address} is already used by {previous_device}"
            )
        else:
            seen_ips[ip_address] = name

        if errors:
            failed_devices += 1
            print(f"{name}: ERROR")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"{name}: OK - IP address {ip_address} is in subnet {subnet}")

    print()
    print(f"Devices checked: {len(device_list)}")
    print(f"Devices with errors: {failed_devices}")
    return failed_devices


if __name__ == "__main__":
    check_devices(devices)

