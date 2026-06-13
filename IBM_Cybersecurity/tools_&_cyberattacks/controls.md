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
  - `ingress filtering`
    - packet filtering where traffic is inspected at the entry point all the way to the network
    - allow legit traffic, and block potentially harmful traffic
    - it inspect the source IP headers
  - `egress filtering`
    - inspects the outgoing IP packets and authenticates source headers

### DDoS Attacks

- an attack on the availability of the system
- classes of DDoS attacks:
  - `ninja` 
    - when a system is 
  - `1k cuts`
    - using a SYN flood
    - send a SYN packet to a system that would normally return a SYN acknowledge, but sends to a different location
    - the system starts a timer, and requiring a response back 
    - the bad actor will continuously send SYN packets
      - this will reserve fake connection attempts, spend useless handling requests, exhaust the system
  - `Distributed DDoS` - `1k cuts * n` - (n representing the amount of users involved in the attack)
    - using a number of 'bots' to carry out a distributed amount of attacks to a certain amount of users that would exhaust the systems

- Prevention techniques
  - infinite capacity 
  - redundancy 
    - rule of thirds
  - pacing
    - limiting the amount of traffic the system can hold in a specific interval of time
  - filtering
    - filtering traffic from specific locations or IP addresses and knowing to turn it off when under attack
    - hardening
      - removing the unecessary actions or knowledgeables
      - removing default settings and passwords
    - patching
      - constantly updating the software to remove vulnerability
    - monitoring - SIEM/XDR
      - understanding the difference between successful monitor and bad actors
    - IR/SOAR
      - dynamic playbooks for understanding the process of what to do i.e. incident repsonse

### Injection Attacks
- understanding the SQL injection
- consequences of SQL injection
- cross-site scripting and types

- injeting malicious code within a SQL structure that can manipulate data through remote commands
- prevelant for older systems
- flaws:
  - SQL injection attacks
    - the ability to talk to databases and manage information
    - the attack is bascially deceptive instructions for database misinterpretation (e.g. leaks, and grant access)
    - will generate falisfied username and passwords
  - XXS attacks
    - embedding harmful scripts excuted on the client's side, which will execute malicious scripts which helps capture; cookies, session identifiers, and critical data & alterations of the website
      - Types of XXS attacks: 
        - server-side XXS
          - when user data is incorporated into the HTTP response which originated in the source
        - client XXS
          - web applications procecesses unauthorized data from users and updated with risky JS functions which will create insecure data sources


- consequences for SQL injection attacks:
  - confidentiality breach
  - authentication compromise
  - authorization loss
  - integrity violation

### Security controls
- types of security controls
- safety initiatives: admin, physical, and technical controls
- functions of security controls

- security controls:
  - actively operate:
    - preventing, detecting and managing risks

- control types
  - admin controls
    - guidelines and methodologies
    - ensuring it's implementation
  - physical controls
    - protecting the hardware, env, and infrstructure
    - serves as the first line of defense
  - technical controls
    - protecting information
    - using hardware, software, and firmware
    - ensuring only authorized personnel are allowed

- integrating controls
  - admin controls
    - access policy
    - regular training programs
  - physical controls
    - biometric security controls
    - alarm systems
  - technical controls
    - firewalls
      - IDS

- security measure functions
  - deterrent
    - discourage deviations
    - decrease intentional attacks
    - discourage against unintentional methods
  - preventive
    - stops security incidents
    - obstructing unauthorized actions
    - addressing potential attacks
  - detective
    - identifing unauthorized actions
    - discover and responding to breaches
  - corrective
    - measures implemented to repair security violations
    - incorporating strategies
    - preventing incident recurrence

