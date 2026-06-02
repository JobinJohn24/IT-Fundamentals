# Servers & Virtualization

### Servers

- poses limitations for scaling, & cost which led to virutal servers.

## Physical servers (bare-metal servers)
- a computer is a physical server with:
  - good-size memory
  - one or more CPU(s)
  - one or more GPU(s)
  - one or more NIC
  - one or more disk drives to store the opearting system and data
- need a operating system to use servers
- servers support 10s, 100s, and 1,000s of users because of the high-specifications.

* e.g - client-server (web) application
![alt text](<Screenshot 2026-05-14 at 8.33.20 PM.png>)
*The following shows a web application that accessible over the public internet*
*client initiaties the request*
*the server processes the request and sends a response*

### Virtualization

## Physical Server - limitations

- underutilization which means they're running at 10-20% capacity.
- isolation and security: to isolate applications, use separate servers. Also need separate environments for testing, development and production.
- scalability & flexibity - harder and more expensive.
- rising costs: more server for scalability and to deploy more applications
- slower deployments/longer lead times: hardware purchase, deployment and config cycles
- backups: slow, hardware dependent, & not easy to restore.

## Introduction to Virtualization

- virtually divide physical servers into multiple virtual servers.
  - introducing portability, scalability, easy backups & flexibility.
 
![alt text](<Screenshot 2026-05-15 at 1.22.45 AM.png>)

*The following shows the comparison between physical servers and virtualization*
*In a virtualization layer, you have hypervisors or multiple virtualizations*
*You're able to have multiple operating systems*
*The hypervisors allows for virtual instances of the hardware to create the VMs*

## Virtual Machine Resources

![alt text](<Screenshot 2026-05-15 at 7.30.59 AM.png>)
- e.g. The hypervisor will act as a emulation layer.
- e.g. when you have 10 TB of disc, you can virtually split the disc into 5 VMs

## Popular Hypervisor Providers

* VMware vSphere - Industry-standard
* Xen
* Microsoft Hyper-V
* Linux KVM
* Oracle VM VirtualBox - your device-compatible 

## Type I & II Hypervisors
- Type I is installed directly on bare metal hardware without needing a host OS
- (e.g.VMware vSphere, Microsoft HyperV)
- Type II hypervisor is installed on the full OS with HV mounted on top of the OS
- (e.g. personal use)

## AWS Account
- Creating AWS account
- creating VMs in AWS

- using *EC2* for Virtual Servers in the cloud.
- using *VPC* for isolated cloud resources

