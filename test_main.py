from main import check_devices, devices

assert check_devices(devices) == 0

assert check_devices([
    {
        "name": "PC2",
        "ip": "192.50.60.12",
        "network": "192.50.50.0/24"
    }
]) == 1

assert check_devices([
    {
        "name": "PC2",
        "ip": "hello",
        "network": "192.50.50.0/24"
    }
]) == 1

assert check_devices([
    {
        "name": "PC0",
        "ip": "168.20.0.10",
        "network": "168.20.0.0/16"
    },
    {
        "name": "PC1",
        "ip": "168.20.0.10",
        "network": "168.20.0.0/16"
    }
]) == 1

print("All 4 tests passed")