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
