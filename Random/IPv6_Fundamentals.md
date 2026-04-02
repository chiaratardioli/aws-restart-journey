# IPv6 Fundamentals Summary

## History of IP

IPv4, introduced in the 1980s, uses **32-bit addresses** (about 4 billion total). An example is **52.3.5.6/24**, where part identifies the network and part identifies the host. Due to rapid internet growth, IPv4 addresses ran out despite solutions like **NAT** and **private IPs (e.g., 192.168.1.1)**. By **2015**, all public IPv4 addresses were allocated.

## Introduction to IPv6

IPv6 was created to solve this problem by using **128-bit addresses**, allowing a massive number of unique IPs. An example is **2001:db8:1234:1a00:1:2:3:4/64**, where the first 64 bits represent the network and the last 64 bits represent the host. IPv4 and IPv6 cannot communicate directly, so methods like **dual-stack** are used.

## Main Features of IPv6

IPv6 provides a **much larger address space**, **automatic configuration**, and **better routing efficiency**. It also improves performance by using **multicast instead of broadcast** and includes **built-in security features** like encryption. For example, a device can automatically generate its own IPv6 address without needing a DHCP server.

## IPv6 Addressing

### IPv6 Anatomy and Functionality

IPv6 uses a simplified main header (40 bytes) along with optional extension headers for additional features. It introduces a flow label, which helps identify and manage packets belonging to the same data flow.
Addresses can be assigned automatically using SLAAC or dynamically with DHCPv6. IPv6 removes the need for a header checksum to improve efficiency and replaces ARP with the Neighbor Discovery Protocol (NDP) for communication within a network.

### IPv6 Address Notation

IPv6 addresses are written in hexadecimal format and consist of 128 bits (32 hexadecimal digits).

- Full example: 2001:0db8:0000:0000:0000:0000:0000:0001
- Shortened example: 2001:db8::1

Leading zeros can be removed, and one sequence of consecutive zeros can be replaced with “::”. A prefix (e.g., /64) indicates the network portion of the address.

## TCP/IP Stack

The TCP/IP stack has **four layers**: Application (e.g., HTTP, DNS), Transport (TCP, UDP), Network (IP, ICMP), and Link (Ethernet). Data moves through these layers in a process called **encapsulation**. For example, when loading a website, HTTP sends a request, TCP ensures delivery, IP provides addressing, and Ethernet sends the data physically.

## Conclusion

IPv6 is the modern replacement for IPv4, offering **more addresses, better performance, and improved security**, making it essential for the future of the internet.
