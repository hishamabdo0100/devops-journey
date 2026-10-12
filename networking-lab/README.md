# Networking Fundamentals Labs

## Overview

This directory documents practical networking exercises completed on an Ubuntu Server virtual machine. The labs cover Linux networking commands, IP addressing, routing, connectivity, DNS resolution, and IPv4 subnet calculations.

## Environment

* Operating System: Ubuntu Server 26.04.1 LTS
* Virtualization: VirtualBox
* Network Mode: NAT
* Network Interface: `enp0s3`
* Programming Language: Python 3

---

# Lab 1: Linux Networking Fundamentals

## Objective

Practice basic Linux networking commands and understand IP addressing, routing, connectivity, and DNS resolution.

## 1. Inspect Network Interfaces

**Command:**

```bash
ip addr
```

**What it does:** Displays network interfaces and their assigned IP addresses.

**Key observations:**

* `lo`: Loopback interface, using `127.0.0.1` for local communication.
* `enp0s3`: Main virtual network interface.
* IPv4 address: `10.0.2.15/24`
* MAC address: `08:00:27:6f:6e:47`
* Connected subnet: `10.0.2.0/24`

## 2. Inspect the Routing Table

**Command:**

```bash
ip route
```

**What it does:** Displays routes Linux uses to decide where to send network traffic.

**Key observations:**

* Default gateway: `10.0.2.2`
* Connected subnet: `10.0.2.0/24`
* Network interface: `enp0s3`
* VirtualBox NAT provides the VM's network connectivity.

## 3. Test Connectivity Using an IP Address

**Command:**

```bash
ping -c 4 8.8.8.8
```

**What it does:** Sends four ICMP Echo Requests to test connectivity to a destination IP address.

**Result:**

* 4 packets transmitted
* 4 packets received
* 0% packet loss
* Average round-trip time: approximately 49.5 ms

## 4. Test DNS Resolution and Connectivity

**Command:**

```bash
ping -c 4 google.com
```

**What it does:** Resolves the domain name to an IP address and tests connectivity using ICMP.

**Result:**

* `google.com` resolved to `142.251.208.238` during this test.
* 4 packets transmitted
* 4 packets received
* 0% packet loss
* Average round-trip time: approximately 45.9 ms

*Note: DNS responses and latency may vary between runs.*

## Lab 1 Key Takeaways

* `ip addr` displays network interfaces and their IP addresses.
* `ip route` displays the routing table and default gateway.
* `ping` tests IP connectivity using ICMP.
* DNS translates domain names into IP addresses.
* Successful ping tests confirm connectivity to the tested destinations at the time of testing, but do not guarantee that every network service is reachable.

---

# Lab 2: IPv4 Subnetting with Python

## Objective

Understand IPv4 subnetting concepts and build a Python tool to calculate network information from an IP address and CIDR prefix.

## Concepts Practiced

* IPv4 addresses consist of 32 bits.
* CIDR notation specifies the network prefix length.
* Host bits determine the total number of addresses in a subnet.
* Network Address identifies the subnet.
* Broadcast Address identifies the broadcast destination for a traditional IPv4 subnet.
* Subnet Mask represents the network prefix in dotted-decimal notation.

## Example Input

```text
192.168.1.70/27
```

## Calculation

* CIDR prefix: `/27`
* Network bits: 27
* Host bits: `32 - 27 = 5`
* Total addresses: `2^5 = 32`
* Traditionally usable host addresses: `32 - 2 = 30`

The two excluded addresses are the network address and broadcast address in a conventional IPv4 subnet.

## Python Implementation

**File:** `subnet_calculator.py`

```python
import ipaddress

ip_input = input("Enter IP address with CIDR: ")

network = ipaddress.ip_network(ip_input, strict=False)

print("Network Address:", network.network_address)
print("Broadcast Address:", network.broadcast_address)
print("Subnet Mask:", network.netmask)
print("Total Addresses:", network.num_addresses)

if network.version == 4 and network.prefixlen <= 30:
    print("Usable Hosts:", network.num_addresses - 2)
else:
    print("Usable Hosts: Depends on network type and usage")
```

## How to Run

Run the script on Ubuntu Server:

```bash
python3 subnet_calculator.py
```

Enter an IPv4 address with its CIDR prefix when prompted.

## Example Output

For input `192.168.1.70/27`:

```text
Network Address: 192.168.1.64
Broadcast Address: 192.168.1.95
Subnet Mask: 255.255.255.224
Total Addresses: 32
Usable Hosts: 30
```

## Lab 2 Key Takeaways

* `/27` leaves 5 host bits in an IPv4 address.
* A `/27` subnet contains 32 total addresses.
* A conventional `/27` subnet has 30 usable host addresses.
* `ipaddress.ip_network()` calculates the network address, broadcast address, subnet mask, and address count.
* `strict=False` allows the script to accept a host IP with a CIDR prefix and determine its containing network.
* Python's `ipaddress` module is part of the standard library and does not require installing an external package.

---

# Overall Progress

* [x] Inspect network interfaces.
* [x] Inspect the routing table.
* [x] Test connectivity to an IP address.
* [x] Test DNS resolution and domain connectivity.
* [x] Calculate an IPv4 network address.
* [x] Calculate an IPv4 broadcast address.
* [x] Identify a subnet mask from CIDR notation.
* [x] Calculate total addresses and traditionally usable host addresses.
* [x] Implement and run a Python subnet calculator on Ubuntu Server.

## Notes

Network connectivity results, DNS answers, and latency measurements can change over time. Usable-host calculations above follow conventional IPv4 subnet rules and are not universal for every prefix length or special-purpose network.
