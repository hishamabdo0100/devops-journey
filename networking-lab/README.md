# Networking Fundamentals Lab 1

## Objective

Practice basic Linux networking commands on an Ubuntu Server virtual machine and understand IP addressing, routing, connectivity, and DNS resolution.

## Environment

* Operating System: Ubuntu Server 26.04.1 LTS
* Virtualization: VirtualBox (NAT networking)
* Network Interface: `enp0s3`

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
* Subnet: `10.0.2.0/24`

## 2. Inspect the Routing Table

**Command:**

```bash
ip route
```

**What it does:** Displays routes Linux uses to decide where to send network traffic.

**Key observations:**

* Default gateway: `10.0.2.2`
* Connected subnet: `10.0.2.0/24`
* Network interface used: `enp0s3`
* VirtualBox NAT provides the VM's network connectivity.

## 3. Test Connectivity Using an IP Address

**Command:**

```bash
ping -c 4 8.8.8.8
```

**What it does:** Sends four ICMP Echo Requests to test connectivity to the destination IP address.

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

**What it does:** Resolves the domain name to an IP address and then tests connectivity using ICMP.

**Result:**

* `google.com` resolved to `142.251.208.238` during this test.
* 4 packets transmitted
* 4 packets received
* 0% packet loss
* Average round-trip time: approximately 45.9 ms

*Note: DNS responses and latency may vary between runs.*

## Key Takeaways

* `ip addr` displays network interfaces and their IP addresses.
* `ip route` displays the routing table and default gateway.
* `ping` tests IP connectivity using ICMP.
* DNS translates domain names into IP addresses.
* Successful ping tests confirm connectivity for these destinations at the time of testing, but do not guarantee that every network service is reachable.

## Status

* [x] Inspect network interfaces
* [x] Inspect routing table
* [x] Test connectivity to an IP address
* [x] Test DNS resolution and domain connectivity
