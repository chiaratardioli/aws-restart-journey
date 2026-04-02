# IPv6 Fundamentals Summary

## History of IP
IPv4, introduced in the 1980s, uses **32-bit addresses** (about 4 billion total). An example is **52.3.5.6/24**, where part identifies the network and part identifies the host. Due to rapid internet growth, IPv4 addresses ran out despite solutions like **NAT** and **private IPs (e.g., 192.168.1.1)**. By **2015**, all public IPv4 addresses were allocated, making a new protocol necessary.  

## Introduction to IPv6
IPv6 was created to solve this limitation by using **128-bit addresses**, allowing an extremely large number of unique IPs. An example is **2001:db8:1234:1a00:1:2:3:4/64**, where the first 64 bits represent the network and the last 64 bits represent the host. IPv4 and IPv6 cannot communicate directly, so techniques like **dual-stack** are used to allow both to operate together.  

## Main Features of IPv6
IPv6 provides a **much larger address space**, **automatic configuration**, and **efficient routing** through hierarchical addressing. It improves performance by using **multicast instead of broadcast** and includes **built-in security features** such as encryption. For example, a device can automatically generate its own IPv6 address using SLAAC without needing a DHCP server.  

## IPv6 Addressing

### IPv6 Anatomy and Functionality
IPv6 uses a **simplified 40-byte header** along with optional **extension headers** for additional functionality. It introduces a **flow label** to identify and manage traffic flows. Address assignment can be done automatically using **SLAAC** or dynamically with **DHCPv6**. IPv6 removes the header checksum to improve efficiency and replaces ARP with the **Neighbor Discovery Protocol (NDP)** for communication within a network.  

### IPv6 Address Notation
IPv6 addresses are written in **hexadecimal format** and consist of 128 bits (32 hexadecimal digits).  
- Full example: **2001:0db8:0000:0000:0000:0000:0000:0001**  
- Shortened example: **2001:db8::1**  

Leading zeros can be removed, and one sequence of consecutive zeros can be replaced with **“::”**. A prefix (e.g., **/64**) defines the network portion of the address.  

### Types of IPv6 Addresses

| Address Type            | Purpose                            | Example          | CIDR Range   |
|-------------------------|-----------------------------------|-----------------|--------------|
| Global Unicast (GUA)    | Public, internet-routable         | 2001::/3        | /3           |
| Unique Local (ULA)       | Private network use               | fc00::/7        | /7           |
| Link-Local              | Local subnet communication only   | fe80::/10       | /10          |
| Multicast               | One-to-many communication          | ff00::/8        | /8           |

## TCP/IP Stack
The TCP/IP stack consists of **four layers**: Application (HTTP, DNS), Transport (TCP, UDP), Network (IP, ICMP), and Link (Ethernet). Data moves through these layers using **encapsulation**. For example, when loading a website, HTTP sends a request, TCP ensures reliable delivery, IP handles addressing, and Ethernet transmits the data.  

## IPv6 Address Management on AWS
Designing an IPv6 addressing plan on AWS focuses on **scalability and structure**, rather than conserving addresses as in IPv4. IPv6 is typically deployed alongside IPv4 in a **dual-stack environment**.

AWS assigns IPv6 addresses from the **Global Unicast Address (GUA)** range, and **ULA is not supported**. Each VPC can have multiple IPv6 CIDR blocks (commonly **/56**), while subnets are typically **/64**.  

There are several ways to allocate IPv6 addresses in AWS:  
- **AWS-provided CIDR blocks** (randomly assigned)  
- **Contiguous blocks via Amazon VPC IPAM** (for better route summarization)  
- **Bring Your Own IPv6 (BYOIPv6)** for full control over address ranges  

IPv6 configuration is flexible—CIDR blocks can be added during or after VPC creation, and IPv4/IPv6 operate independently. Subnets can be **IPv4-only, IPv6-only, or dual-stack**, but IPv6 must be explicitly enabled for resources.  

Even though IPv6 addresses are globally routable, actual internet access depends on **routing, gateways, and security settings** (such as security groups and ACLs), not just the address itself.  

## Conclusion
IPv6 is not only a replacement for IPv4 but also a **modern networking foundation**. It solves address exhaustion while improving **efficiency, scalability, and network design**. With structured addressing, automation features, and integration into platforms like AWS, IPv6 enables more flexible and future-proof network architectures.
