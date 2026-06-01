# DNS, monitoring, alerting, logging, databases

## objectives

- monitoring in place for the infastructure.
- notification alterting based on breaches or data leaks
- log for understanding every event, infastructure, application, network changes.
- DNS introduction (converting text to IP address & vice versa)
- introduction to databases
- drawing professional architecture

## domain name system/services

- websites and destinations on the internet use IP addresses.
- DNS help translate a website text into IP addresses.
- DNS are databases on the internet mapping domain names on their IP address(es).
- devices connected to the internet has a DNS server in its TCP/IP configuration.

- Process: User wants to visit `dolfined.com`
1. user submits a request for `dolfined.com`
2. creates a DNS query of the subdomain.
3. DNS will check it's database for corresponding query based on the IP address.
4. If found, it would provide a DNS response with the IP address.
5. the server will form a IP packet to `www.dolfined.com` & get a response back

### commands related to DNS configuration

- commands related to finding the DNS server details on your machine (dependent on the OS you're using.)
- linux - `cat/etc/resolv/config` = shows configured DNS servers
- linux - `systemd-resolve --status` = for systemd-based systems
- linux - `nmcli dev show | grep DNS` = for network manager - managed interfaces

*DNS Configuration - Demo*

DNS testing - AWS linux EC2 instance
1. creating a EC2 AWS linux instance in a public subnet
   1. ensuring instance has a public IP
   2. associate a security group that allows all traffic, inbound, and outbound
2. SSH into the instance from the console.

*testing DNS - Demo*

- creating key pair 
- all made in the custom_vpc
- enable the subnet to be a public subnet
- enable auto=assign
- enable SGA security group
- label as `testing-dns`
-  `EC2 instance connect` rather than `SSH client`
-  commands for linux:
   -  `sudo su` - elevate the permissions to root
   -  `cat /etc/resolv.conf` OR `systemd-resolve --status`- provides the DNS server with it's corresponding IP address. Confirms that the DNS is active and usable.
   - `nslookup `example website `www.google.com` - returns the IPv4 & IPv6 addresses.
   - `nano /etc/hosts` - the ability to define hosts.
   - `172.31.0.55 www.google.com` defines the given into the localhost
   - control + x - confirming the changes
   - when `ping www.google.com` the ping is established from the definition that was confirmed with `nano /etc/hosts` was defined.

*Route 53*

- Scalable DNS & domain name registration.
- used for big coporate for hosting their domains

### Monitoring, Alerting & Logging

*monitoring*
- monitoring is watching the metrics in real-time for performance and security.
- e.g. network in & our traffic, CPU storage, disc space
- `activity monitor` for macOS.

*alerting*

- notifing when some pre-identified events happen or threshold are crossed (performance, health, or security related)
- budget alarm, email notifications for an alert threshold and the usage amount.

*logging*

- documentation history of events, or errors.
- great in auditing & troubleshooting for finding root cause of a system.
- `cloudtrail` - built-in for AWS console
- `cloudwatch` - built-in monitoring resources & applications for AWS console

*Importance*

- security
- troubleshooting - fixing things faster when something goes wrong.
- performance - spoting slowness before users complain 
- compliance
- e.g:
  a. CPU usage goes down 80%.
  b. someone tries to SSH into an EC2 numerous times.
  c. code (service) fails to run.
  d. website response time is slow.
  e. web server runs out of disk space.
- e.g. tools
  a. windows task manager
  b. MacOS activity monitor 
  c. AWS cloudwatch (monitoring & altering(alarm) + logging)
  d. AWS cloudtrail - logging

### Databases

- organized collection of data that's stored, searched, updated, and retrieved by software.
- files can't be used because it's harder to search, update or scale as the data grows bigger.
- applications need databases:
  - applications use user data 
  - e-commerce sites store products, orders
- database - write operation
  - the application(s) writes, queries (reads data) the DB

*Types of databases:*

- ![alt text](<Screenshot 2026-05-23 at 9.17.36 PM.png>)
*displays the types of databases*


*relational databases - structured query language (SQL)*

- allows application to 'talk' to databases (read/write) using simple queries.

### Drawing network & infrastructure architectures

- professionally drawing architectures of infrastructure of e.g. a:
  1. AWS architecture that's placed in AWS region - useast2, with two availability zones with a private and public subnet in each of the availablity zones. The private subnet containing the database, and the public subnet containing the webserver.
  2. all subnets connected to the router and the router connected to the IGW 

- `app.diagram.net` - online drawing tool.


