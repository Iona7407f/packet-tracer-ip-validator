# Small Office Network

An educational project that simulates a small office network in Cisco Packet Tracer. It includes five PCs, two switches, and a router.

Sales and Security are separated into VLANs. A trunk carries both VLANs between the switches, and the router connects their subnets through separate physical interfaces.

A Python script validates the recorded IP address plan, checking address format, subnet membership, and duplicate addresses.

**Tools:** Cisco Packet Tracer & Python 3.12

## Network Topology

![Network topology](screenshots/topology.png)

| VLAN | Department | Subnet | Gateway |
| --- | --- | --- | --- |
| 10 | Sales | 192.50.50.0/24 | 192.50.50.1 |
| 20 | Security | 168.20.0.0/16 | 168.20.0.1 |

# Python Address Validation

The script checks IPv4 format, subnet membership, and duplicate addresses.

**Valid address plan — all five PCs pass**

```bash
PC0: OK - IP address 168.20.0.10 is in subnet 168.20.0.0/16
PC1: OK - IP address 168.20.0.11 is in subnet 168.20.0.0/16
PC2: OK - IP address 192.50.50.12 is in subnet 192.50.50.0/24
PC3: OK - IP address 192.50.50.13 is in subnet 192.50.50.0/24
PC4: OK - IP address 168.20.0.14 is in subnet 168.20.0.0/16

Devices checked: 5
Devices with errors: 0
```

### Automated Checks

**Address outside the expected subnet**

```bash
PC2: ERROR
  - IP address 192.50.60.12 is outside subnet 192.50.50.0/24

Devices checked: 1
Devices with errors: 1
```

**Invalid IPv4 address**

```bash
PC2: ERROR - invalid IPv4 address or subnet

Devices checked: 1
Devices with errors: 1
```

**Duplicate IP address**

```bash
PC0: OK - IP address 168.20.0.10 is in subnet 168.20.0.0/16
PC1: ERROR
  - IP address 168.20.0.10 is already used by PC0

Devices checked: 2
Devices with errors: 1
```

**Test summary**

```bash
All 4 tests passed
```
