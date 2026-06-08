# Cybersecurity Controls

*internet attack*
### Internet Security Threat: Mapping
- features of Nmap
- outline features of wireshark
- advantages of mapping for professionals

- using network mapping to visualize a network's connections
- as an admin:
  - assessing the network's topology by recognizing:
    - nodes
    - services
    - operating system
    - data path

- NMap - enables admins to:
  - identify devices
  - discover open paths
  - detect security risks
  - used for network and security auditing 
  - it utilizes raw IP packets to identify:
    - devices
    - OS
    - services
    - Packet filers
    - firewalls
    - automating networking 

- Wireshark
  - used for comprehensive network mapping and analysis
  - network protocol analyzer
  - features:
    - dispalys network traffic visibility
    - maps network activity in real-times
    - dissect packets
    - examine protocol-level communications

- advantages for professionals:
  - easier to troubleshoot issues
  - manage the network's complexity
  - detects anomalies
  - proactive network management

- advantages for hackers:
  - ability to identify unguarded entry points
  - vulnerable systems
  - a way for them to navigate the network

### Packet Sniffing
- packet sniffing
- the use cases
- types of packet sniffing techniques used by attackers
- protection strategies

- packet sniffing
  - unauthorized access to transmitted information
  - units of data transmited over networksa
    - it utilizes a header and payload (i.e. IP address: to/from, and the content of the packet: message)
  - scenario:
    - organization network is experiencing slowdowns
    - the company utilizes packet sniffing to analyze the data packers and collects points by intercepting traffic
    - it places the NIC, in a state of capture mode for all traffic

- use cases
  - used for network diagnostics
    - examines data packets looking for suspicious activity
  - performance monitoring
  - web activity monitoring

- sniffing attack
  - using software to intercept unencrypted packets
  - examines personal data
  - using AARP tampering
  - DNS falsification
  - SQL injection 

- Types of packet sniffing 
  - passive sniffing
    - involves multiple connecting networks
    - monitors LANs or Wi-Fi data
    - e.g. intercepting data at a public Wi-Fi
  - active sniffing
    - targets switched networks with additional traffic
    - e.g. generating extra network activity which causes switching to broadcast data widely

- protection against it:
  - maintain systems
  - security login measures
    - MFA
    - strong passwords
  - exercise caution with emails
  - using a VPN 
  - prioritize HTTPS websites

### IP Spoofing
- distributed denial-of-service (DDoS)
- attacks through masking botnet devices
- man-in-the-middle attacks 
- prevention techniques

- network communciation
  - manipulating packet headers to conceal senders address
  - exchange of IP packets
  - the backbone of communication between networks

- DDoS attacks
  - distributing the services of a target or network
    - to flood a target with excess target
  - alters the source IP address
  - e.g. target = github
    - experienced a DDoS attack
    - it 

- botnets
  - interconnected computers that are centralled controlled with a compromised computer that runs a specialized bot program
  - with the motive to perform malicious attacks
  - individuals may use IP Spoofing to masks the botnets' activities and assign fictitious IP addresses

- Man-in-the-middle attacks
  - intercepting a packet, modifying it, and forward the packet undetected
  - with the motive to collect to private information

- prevention techniques
  - ingress filtering
    - packet filtering where traffic is inspected at the entry point all the way to the network
    - allow legit traffic, and block potentially harmful traffic
    - it inspect the source IP headers
  - egress filtering
    - inspects the outgoing IP packets and authenticates source headers

### DDoS Attacks