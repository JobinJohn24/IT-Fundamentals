# Cybersecurity & Network Security Fundamentals

### Objectives

- distinguishing between cybersecurity & network security
- defining both, it's applications
- network devices - firewalls (method of securing & protecting your devices)
- examples from AWS, network ACL
- encryption
- Virtual Private Networks

### Cybersecurity Introduction

- your phone or computer is like your house
- Cybersecurity is about:
  1. locking doors (passwords, firewalls)
  2. closing curtains (encryption)
  3. setting up alarm system (antivirus, monitoring)
  4. checking who's at the door (authentication in networks)

- it's about protecting computers, networks, and data from being stolen, attacked, or damaged.
- Cybersecurity important:
  1. protects personal information
  2. to stop hackers from breaking into systems
  3. keeping companies and services running
  4. preventing data loss/leaks

### Specialization within Cybersecurity

1. `network security` - protecting network devices and data stored or moving through internet or local networks.
2. `Application security` - software & application security (from bugs, backdoors, trojans, etc)
3. `endpoint security` - devices like server, storage, laptops, phones, etc
4. `cloud security` - infastructure and data in the cloud
5. `identity & access` - who's allowed to access what
6. `physical security` - protecting data centers and hardware
7. `policies & rules` - ensuring compliance to policies & rules

### Network Security Introduction

- network security is a branch of cybersecurity
- it's about protecting network devices and data when traveling across the network - keeping the hackers out & keep the data safe.

*Network Devices - Firewalls*
- firewall - security gate for a network & applications.
- configured to allow or deny data inbound or outbound based on the rules you set.
- once, configured, the firewalls monitors traffic inbound and outbound to apply the configured rules.
- firewalls protect at the network level or at the application level.
- advanced / web application / next-generation firewall - understand or interprets up to layer 7.

![alt text](<Screenshot 2026-05-22 at 5.46.24 PM.png>)
*e.g. overview of firewalls and it's implementation for real-world use cases*

### Infrastructure Security - Zoning Architecture

- firewalls divide the network into trusted and untrusted segments.
- e.g. government, hospital, corporate
- they establish zones within their infastructure.
- Zoning architecture designed based on security & criticality (importance of an asset or system) of each component.

*Firewall Examples - AWS VPC Security Groups*

### Understanding Security Groups

- virtual firewall applying at the instance's network interface (AWS Virtual Machine is called a EC2 *Elastic compute cloud*) ~ VNIC = Virutal Network Interface Card
- in a security group, permit rules are configured *no deny rules*
- contains a implicit deny rule at the end.
- changes take effect immediately.
- traffic can flow ingress(inbound) / egress(outbound)
- Stateful - contains firewalls that allow seamless entry & exit.
- stateless - need to allow for the inbound entry.

*Inbound Rules - Source & Port Range*

- Destination's a predefined because of the security groups attached to it.
- ![alt text](<Screenshot 2026-05-23 at 10.45.20 AM.png>)
- every instance *MUST* require a security group.
- destination port is not required because of the preconceived notion that it's already on it's way to the destination from the source port.
- the port range dictates the destination because the port range is based on the instance. 

*Outbound Rules - Destinatino & Port Ranges*

- ![alt text](<Screenshot 2026-05-23 at 10.53.07 AM.png>)
- a table of rules for outbounding from an instance to a source.
- the destination IP's dictates the source IP that comes from the instances.
- security groups are stateful.

*Firewall Example: AWS VPC Security Groups*

- security group walkthrough in AWS console:
  1. default security group based on out/in -bound rules
  2. default VPC's are necessary for understanding the immediate readiness, and the ability to deploy VPCs without technicial difficulties.
  3. the default VPC inbound rules allows access to all ports.
  4. the default VPC outbound rules allows traffic from anywhere (0.0.0.0/0)
  5. if 0 inbound rules are initiated, then all traffic will be dropped & implicitly drop the traffic.
  6. e.g. if the outbound rules allows traffic to flow seamlessly, then the traffic will be allowed since the VPC is stateful, which means they allows for traffic in and outbound when coming outbound.

*Security Group - Practice #1*

- ![alt text](<Screenshot 2026-05-23 at 12.01.50 PM.png>)
- port 80, anyone can access the instance over HTTP
- port 22, only the specific IP can SSH into the server.

- ![alt text](<Screenshot 2026-05-23 at 12.03.16 PM.png>)
- the server can send traffic *ANYWHERE* on any port (e.g. download updates)

- ![alt text](<Screenshot 2026-05-23 at 12.05.00 PM.png>)
- The server can *ONLY* connect to 10.0.2.0/24 on port 5432 (PostgreSQL)
- /24 - usable hosts that I can send the traffic to.

- ![alt text](<Screenshot 2026-05-23 at 12.20.19 PM.png>)
- if the request was sent within the same subnet with the same IP: 10.0.1.0/24
- Only EC2s in 10.0.1.0/24 can connect on port 3306 (MySQL).

*AWS Security Group - VM in AWS*

- hands-on lab that allows user to ping (verify that the IP is connected to IGW)
  1. two security groups (SGA & SGB)
  2. Walkthrough the default inbound & outbound rules.

- Notes of walkthrough:
  1. create two security groups within the same public subnet under `SGA` & `SGB`
  2. create two instances in the public subnet under `instance_A` & `instance_B`
   a. create a key pair for each instance for the key pairs of each instance.
   b. ensuring that the public IP was assigned to each instance.
  3. associate instances with each security group
  4. when trying to ssh from laptop into instances_a or b can be blocked because of no inbound rules established in both security groups.
  5. adding the SSH from 0.0.0.0/0 to the inbound rules of SGA & SGB.

*Firewall Examples: Network Access Control Lists (NACLs)*

- a virtual firewall that applies at the subnet level.
  - decides what goes in and out of a subnet.
  - NACL rules are numbered.
  - lowest numbers are evaluted first.
  - allow/deny rules can be configured.
- if the rule number isn't displayed, then it would be denied.
- NACL functions at the implied router.

![alt text](<Screenshot 2026-05-23 at 2.14.43 PM.png>)
- overview of understanding the position at which NACL can be placed. 

*Use Cases for NACLs:*
- wanting a extra layer of subnet-level of protection.
- need to explicitly DENY traffic because security groups can't deny.
- you want to block IP ranges at the subnet-level (i.e. bad actors, geo-blocking)
- working with a compliance-heavy environment (extra firewalls are required.)

*AWS Network Access Control List - Walkthrough*

- network ACLs are stateless, which means it treats every request as independent that retains no memory of past interactions.
- NACL will have no memory that outbound traffic is just a response to a valid inbound request.

*AWS Network Access Control List - Walkthrough*

- creating two security groups, using the security group names & ensuring they allow all traffic inbound & outbound on all port ~ examining what security groups are capable of doing.

*AWS NACL - Ping between instances in the SAME subnet*
- blocking ICMP ping from any source outbound & inbound = rule 50 
- allow all traffic inbound & outbound = rule 100