# IP Routing

### Objectives

1. how routers works.
2. how routers are configured.
3. understanding the best path for the router.
4. concepts behind the AWS infastructure.
5. understanding and practicing with e AWS private cloud or virutal data center.
6. how to create subnets, route tables, configure routing inside a VPC.
7. connect VPC/or virtual data center.
8. how to laund applications, websites or etc.
9. difference between public and private subnet from AWS.
10. how to implement public and private IPs to the VPCs and/or virutal data centers on AWS.
11. How NAT functions
12. IP packet headers

### How does IP Routing work?

- devices on the same network talk directly to each other using a connected `switch.`

- a router is used if the devices would like to communicate outside the switches capabilities which would enable the user to access the internet through WLAN. & DC switch(es)

- `routers` can forward traffic between networks.

- `VLANs` that's connected from the hypothetical red and blue `VLANs` can only communicate with each other using a router or multi-layer switch (intelligent switch)

### Routing

- Process of selecting paths inside a network to forward traffic between hosts.

- Which means it's establishing a the best path for the best communication.

- Routers using routing tables *forwarding databases* & algorithms to determine the best possible path for forwarding traffic.

### Routing Tables

- routing table is likea router's map or GPS.

- every individual router will build a routing table (database) of known destinations & how to reach them.

- The router will recieve a IP packet:
  - If the destination is known, then send the forward it.
  - If the destination isn't known, then the packet is dropped.

- Routing tables can be configured statically (manually) *static IP routing*
  - This is known for smaller level companies.

- Routing tables can be be configured dynamically *dynamic IP routing*

- Rather than configuring static routes on every router, the network can use a dynamic routing protocol, which enables routers to automatically share reachable networks with each other (e.g. OSPF & BGP)

- The router will be provided by a manufacturer, placed in your infastructure & be able to configure it based 

### Default Route

- A special route table entry used as a last resort to forward a packet. *IF* there's no specific entry to be used.

  - If the destination is known, then send the forward it.
  - If the destination isn't known, then the question becomes if there's a default route, if yes then forward the packet, if not: drop the packet.

### Use Case for routing tables
## routing tables - practice

- e.g. ![alt text](<Screenshot 2026-05-18 at 4.42.55 PM.png>)
*Router B has a direct WAN connection with router A, while router B is connected to the internet.*

- Routing tables for each router
- ![alt text](<Screenshot 2026-05-18 at 5.23.34 PM.png>)
*Default routing tables for each router.*

*This displays a Local Area Network to a Data Center via a point-to-point Wide Area Network with a internet connection.*

*Router B reads incoming packages, hands it off to the DC switch and then routes it to the correct department floor.*

*Router B will have a backdoor that leads to the public internet.*

*The route to find data from the main archive of the company versus information from a public website is ENTIRELY different* 

### IP Packet

- The message in IP networks are called a packet.
- It's like a sealed envelope that carrying digital mail from one computer to another.
- IP Packet contains the following:
  1. IP address (from)
  2. The sender for who sent the IP packet. (to)

### IP Packet Headers

- Payload - to deliver the acutal content or message.
- Headers - to guide the packet through security checkpoints.

### AWS Global Infrastructure

- AWS Cloud - consists of geographic regions, which are a group of data centers that's in one country.

- Each region has 3+ availability zones *which has data centers packed together with high speed lengths*
- In each availability zones contain AWS data centers with high-speed links.
- When VMs are created, they're distributed among the AWS data center within the availablity zones.

### AWS VPC Overview

- Creating a virtual machine that's used from cloud computing via AWS cloud.
- *virtual private cloud* isolated from other VPCs by default.
- AWS clients have *full control* over their VPCs.
- a VPC will always span one region, never stretching beyond a single AWS region.
- a *default VPC* is created in each AWS region when a AWS account is created.
- having VPCs in each availability zones within a region to increase the availability of the applications, or workload of the VPC.

### VPC Components

- CIDR block
- 1+ subnets
- implied router (automatically created)
- route tables
- internet gateway (IGW)
- security groups
- network access control lists (Network ACLs)

### Components

- CIDR blocks

• each VPC has a CIDR block. *All communication is done using an IP address*
• the VPC subnets are created from the CIDR block.
• the CIDR block ranges from /28 - /16.

- Subnets & Route Tables
- AWS VPC

• Configuring *multiple* subnets per VPC.
• *implied router:* used for communication between subnets within the same VPC. Communication between availability zones.

- Internet Gateway
• how VPC can communicate with the internet.
• *ONLY ONE* internet gateway can be attached to a VPC at a time.
• communcating with the internet requires a subnet's route table.

### Creating a custom AWS VPC - Demo
- 4 subnets, routing tables, and internet gateway.
- ![alt text](<Screenshot 2026-05-21 at 10.25.15 AM.png>)
*Overview of custom AWS VPC architecture and system design*

1. `custom vpc` in `us-east-2`
2. Create 4 subnets in the designated availability zones.
3. associating route table with the given subnets.
   • `RT_1` = subnet1
   • `RT_2` = subnet2
   • `RT_34` = subnets 3 & 4
4. 3 availability zones assigned to the subnets.
   • us-east-2a
   • us-east-2b
   • us-east-2c

![alt text](<Screenshot 2026-05-21 at 10.31.43 AM.png>)
*Overview of end result of custom AWS VPC*

### Difference between public and private subnets in AWS VPCs

- Subnet is considered a public subnet *IF* it satisfies two conditions:
  1. subnet that has a IGW.
  2. route table must have a default route entry pointing to IGW.

- a configuration must be made in order to create traffic to the Internet.

### Network Address Transmission (NAT)

- IP packet - NAT
• masking a private IP address into a public IP address through a process called NAT-ing.
• private IP -> LAN -> router (where NAT conversion occurs)-> internet

### AWS Linux VM in public subnet & access to/from the internet

1. create VM.
2. edit IP route table to  connect to the IGW.
3. accessing the internet from the VM.

*Walkthrough* - Demo

1. adjusting subnet_1 to become a public subnet
2. create VM in a public subnet
   a. VM must have public IP assigned
   b. adjusting the security group to allow all traffic
   c. connect to machine
   d. access something on the internet
   e. ping from internet to the instance

a. `ping IPv4` performs packets send and recieves for understanding if the VM is in a public or private subnet.
  1. if confirmed, 0% packet loss
  2. `request timeout for icmp_seq #` - represents that the VM is in a private subnet. The route table isn't communicating with the IGW.

b. accessibilty from the internet in AWS:
  1. VM
  2. instance with a public IP address
  3. *sits* on a public subnet.
  4. has a security group that communication in and out the the VM.

### Command to verify the IP addresses

- `ip address` - confirms the IP addresses that's 'registered' under the VM.
- `curl ifconfig.me` - verifies the public IP address.