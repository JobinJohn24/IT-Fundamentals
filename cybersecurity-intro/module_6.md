# Network Security

### objectives
 
- protecting the underlying communication networks and computers from attacks.
- configuring a firewall for computers to use.

### Firewall

- blocks network communications by understanding the addressing & protocol information in the data packet's header.
  - data packet arrives at the firewall.
  - addressing (IP) and protocol information (TCP/UDP) is compared to rules that of the firewall.
    - firewall rules are created by the firewall manufacturer, admin, or user.

*Personal Firewall*

- operating systems have firewalls pre-installed as a part of the operating system.
- any firewall that limited to protecting just the computer that it's installed on. 

*Checking personal computer for firewall safeguards*

- using the following website link will indicate if a personal computer is compromised.
- designed to probe the computer to understand what's accessed and what's blocked.
[Computer Probing Experiment](https://www.grc.com/shieldsup)
- The following is a list of probes that's *MEANT* to be kept out:
  - instant UpnP exposure test probe
  - file sharing probe

### VPN

*Basics*

- VPN purposes:
  - securely connecting isolated LANs across the internet.
  - allowing mobile users remote access to a corporate network using the internet.
  - controlling access within a intranet environment. (*intranet environment = private, isolated network accessible to only authorized individuals*)

*VPNs for Corporate*
- VPNs are built using network devices & software.
- Software includes:
  - `VPN client`: connecting users to the VPN responsible for communication for senders and recievers.
  - `VPN server`: performs the authentication of users and routes traffic to the corporate network.

*VPNs for Open Network*

- the most vulnerable places of the internet are public / open networks like cafes, hotels, or/and airports. 
- a VPN provider offers users to connect your VPN client to a VPN service.

*Securing 'tunnels' for VPN path*

- VPN relies on encryption for data safety, and authenticity.
- Methods of ensuring authenticity:
  - hashes
  - digital signatures
  - message authentication codes (appened to messages & act as an authenticator)

*Protocols for VPNs:*
*Legacy 'playbook':*

- `Point-to-Point Tunneling:` the mathematical overhead was minimal.
  - contained structural flaws in the authentication protocols.
  - basic laptops with automated packing-sniffing & cracking software are able to intercept a PPTP encryption key.
  - modern OS have removed PPTP to protect users from configuring an insecure tunnel.
- `Layer 2 Tunnelling Protocol:` fixes the PPTP problem.
  - offers 0 encryption
  - binds with IPsec/ to handle the data encryption.
  - uses specific network communication ports (easier for firewalls & network ACLs to detect and block.)
- `Internet Protocol Security:` widely known and used by IBM, Intel, HP/Compaq, Microsoft, & etc.
  - paired with IKEv2 which helps with stablity in switching between Wi-Fi & towers.
  - no need to double-wrap its data packets, and prevents admin delays which accounts for its blazing speed.

*VPN Security Risks*

- Major infrastructure and security vulnerabilities:
  1. vulnerable remote device
        - if personal computers connects to a organization's private corporate network, it becomes a backdoor for hackers.
        - corporations must enforce strict device compliances.
  2. Implementation defects (flawed code & poor configs)
        - human programming & bad settings can lead to breaking the protocol's security.
        - the use of modern, and audited protocols as well as config audits must be enforced.
  3. compatatibility issues
        - mixing different software, firewalls, and routers from different providers causes glitches & hidden security gaps.
        - a single technology provider for a organization is enforced.
  4.  unreliable performance
        - since VPNs rely on the internet for communication, there's no guarantees about the reliability, or delivery of information.

*Browser*

*TOR Browser*

- used for enchanced security measures
- uses 3 random TOR routers to relay communcation.

### Intrusion Detection System (IDS)

- it's a dedicated device or software that's divided into two types:
  1. network intrusion detection system
        - responsible for monitoring data passing over a network.
  2. host intrusion detection system 
        - responsible for monitoring data to & from a computer.

- used for scanning traffic passing through a firewall for potential attacks using NIDS.

*Weaknesses:*
  - sensitivity to certain types of attacks
  - don't generate enough traffic
  - false reporting

*IDS Detection Techniques:*

- `anomaly detection`
  - will detect anomalies based on how different it looks behaviorally comparitive to everyday routine operations.
- `misuse detection`
  - system admin provides a database of pre-programmed attack patterns (*signatures*) that can be compared to network activity.

*Honeypots*

- studying attacks as network admins.
  - by deflecting attackers towards isolated computer or network (*which appears to be legit*) which is closely monitored.
  - it's recorded and analyzed without risking important data.
  - e.g. used by anti-spam organizations to identify the location & identities of spam email senders.