# Internet Protocol Troubleshooting Commands

In this lab, I will act as a new network administrator who is troubleshooting customer issues, 
I will explore troubleshooting techniques by following the OSI model. I will focus specifically on Layers 3, 4, and 7, and 
I will correlate each layer with commonly used troubleshooting commands. Through practical examples and customer-based scenarios, I will 
apply these commands to identify and resolve networking issues. While this lab will not cover an exhaustive list of troubleshooting tools, 
I will use some of the most common and effective commands to diagnose typical networking problems.

Some layers have commands related to them to help with troubleshooting. The following is an example of how the troubleshooting commands flow 
with the Open Systems Interconnection (OSI) model.

![OSI model and Troubleshooting: a comparison](NS05-OSItroubleshooting.png)
Figure: This is an example of how troubleshooting commands have similarities to the OSI model.

## Layer 3 (network): The ping and traceroute commands

1. **ping**

One can use the ping command for several purposes, but the most common is to test connectivity to a server. The ping command sends ICMP echo
requests from a machine to a target server (for example, amazon.com). The server then responds with an echo reply, including the round-trip time.
It is primarily used to troubleshoot connectivity issues and verify reachability to a specific target. Additionally, it can be used to maintain
continuous traffic flow in a network if needed, and it also supports sending continuous pings.

The *ping* command accepts an IP address or URL followed by options; the *-c* option specifies the count, indicating how many echo requests will be sent.
```bash
ping 8.8.8.8 -c 5
```
In the example above, ping sends five ICMP echo requests to the public DNS server operated by Google to test connectivity and measure response time.

3. **traceroute**

The traceroute command reports on the path and latency that the packet takes to get from your machine to the destination (8.8.8.8). Each server is 
called a hop. There can be packet loss, seen as percentages, at each loss, which is usually due to the user's local area network (LAN) or ISP; however, 
if the packet loss occurs toward the end of the route, then the issue is more than likely the server connection. You can pinpoint an issue or error when 
hostnames and IP addresses on either side of a failed jump, which looks like three asterisks (***).

The *traceroute** command accepts an IP address or URL followed by options.
```bash
traceroute 8.8.8.8
```
The traceroute command shows the path taken to the web server operated by Google and the latency taken to it.

Packet loss, seen as percentages, can occur at each hop, and this loss usually occurs because of an issue with the user's local area network (LAN) or ISP

You can pinpoint an issue or error when the hostnames and IP addresses on either side of a jump have failed. Three asterisks (***) indicate a failed hop.

## Conclusion
- I practiced troubleshooting commands
- I identified how to use these commands in customer scenarios

## Additional resources
- [ping](https://docs.aws.amazon.com/vpn/latest/s2svpn/HowToTestEndToEnd_Linux.html)
- [telnet](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-windows-unable-connect-port/)
- [traceroute](https://aws.amazon.com/premiumsupport/knowledge-center/network-issue-vpc-onprem-ig/)
