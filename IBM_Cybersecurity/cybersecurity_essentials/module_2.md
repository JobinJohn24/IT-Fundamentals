# Security Best Practices

### Password management techniques
- best practices
- identify strong/weak password
- creating password policies

- Cracking passwords:
    - brute force - utilizies as mathematically possible passwords
      - `total combinations = (character set size)^password length`
      - e.g. a 4-digit pin that uses 0-9 numbers will have `10^4 = 10,000` possible combinations
    - dictionary - uses words pulled from newspapers and dictionaries
    - rainbow - words from the original password hash
    - hashing - using a `scrambling` algorithm that transforms from an input string into fixed-input output string
- hackers can guess trillion passwords per second.
- avoiding this:
  - using uni-code, digits, and ascii characters
  - using upper/lower case.
  - avoiding using *leet*
  - 12 character minninum
- password expiration helps employee use less risky behavior

### authentication & SSO
- SFA, 2SFA, MFA
- types of authentication factors
- how MFA decreases risk of breaches

- single-factor
  - e.g. username & password 
  - not safe from:
    - keystroke logging
    - phishing
    - data breach information
- two-factor
  - e.g. security key in a USB
  - best defense against phishing and hijacking
  - modern uses of NFC, where proximity of the security key gives access
- MFA
  - requires more than just a password
  - extra protection:
    - risk of breach reduced
    - no keystroke logging
    - control of factors
    - phishing risk reduced
  - not a 100% fail-proof
- SSO
  - businesses use it for simplification & speed 
  - ability to working without having to multiple passwords
- identification factors
  - security questions
  - OTP code
  - password or pin
  - biometric

### Security Threats: Access Control, Authorization, & Authentication
- authentication factor
- digital accounting
- methods of non-repudiation

- 3 processes for logging into a network or account
    1. access control - access based on user status
    2. authorization - permissions for access to networks, application or account
    3. authentication - proof of identity with password or credentials

- access control 
  - used to restrict:
    - resources that of access
    - functions that's allowed to perform
    - what users can do
    - *Rules-based access control* - uses network groups with different permission levels
- authorization
  - permission to access a location or do an action
  - jobin
- authentication
  - confirming the identity
  - `login information + identity confirmation = authentication`
  - factors:
    - username and passwords
    - something you have (e.g. devices)
    - something you are (e.g. biometrics)
  - methods: 
    - SSO
    - MFA
    - SFA
    - 2FA

- digital accounting
  - used for troubleshooting, security analysis, forensics, and hacking
  - logs:
    - audit logs represent the log file events
    - understands who, and what (actions)
    - system response
  - tracking
    - OS
    - browser
    - resolution
    - activity
    - fonts
  - cookies
    - browsing activity
    - personal information
  - browsing history
    - recent sites
    - commonly visited sites

- non-repudiation
  - acts as a digital signature
  - video
  - biometrics
  - signature
  - receipt

### Hardening Devices
- methods of securing & hardening devices
- device & system vulnerabilites
- best practices for common security threats

- device hardening
- techniques:
  - disabling uneeded features
  - updating firmware
  - using firewalls, VPN, or anti-malware
- Firmware updates:
  - BIOS *basic input output system* 
    - boots up windows & linux PCs
    - starts OS
    - runs hardware checks
  - secure boot
    - unified extensible firmware interface
    - it confirms the manufacturer's digital signature 
      - helps prevent malware from taking control
  - TPM chips:
    - stores & manages encryption keys
  - drive encryption
    - scrambles data to make it unreadable

- encryption
  - converts plain text to cipher text using a algorithm

- features and port
  - using features and ports to steal data and cause damage
  - features:
    - autorun - runs the malware automatically
    - bluetooth
    - NFC - no protections with limited ranges
  - ports:
    - 443 - manages *secure* web traffic (HTTPS)
    - 22 - used for secure shell connections (SSH)
    - 80 - standard web browser traffic (HTTP)

- zero-day attacks
  - no patches or updates because they haven't been created.
  - protection against ZDA:
    - using a VPN
    - general security guidelines
    - using & visiting trusted networks and sites

- firewalls
  - it monitors connections and blocks traffic
  - e.g. school uses firewalls so student can't access social media

### Reading - Firewalls

- Filters
  - responsible for controlling network traffic
  - the inbound and outbound rules determine the traffic whether it's approved or denied based on IP addresses, ports, domain names, etc
  - more rules = longer time for firewall to review traffic
- inbound rules
  - controls incoming network traffic
  - protects the system from unauthorized access
- outbound rules
  - controls outgoing network traffic
  - helps manage data leaving with *ONLY* authorized applications and services

### Lab - windows firewall with advanced security

### Security threats: Validation & Device Usage
- device usage best practices
- reputable driver and firmware sources
- do's & dont's of keeping devices safe

- source code validation
  - updates for device from reputable sources (i.e. vendor stores, authorized reseller, original equipment managers, and software managers)

- OEM vs 3rd party websites
  - drivers & firm updates on websites from original equipment manufacturers
  - e.g. dell, HP, samsung, nikon, nvidia
- Anti-malware & VPN services
  - e.g. norton, mcafee, bitdefender, & free -> microsoft, windows, apple 

### Security Threats: Encryption Concepts
- encryption & common uses
- symmetric and asymmetric encryption use cases
- cryptographic hashing methods & techniques

- 