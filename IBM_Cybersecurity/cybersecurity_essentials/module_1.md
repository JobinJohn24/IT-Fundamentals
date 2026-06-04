# Security Concerns

### CIA

- This acryonym stands for the security program that *MUST* contain confidentiality, integrity, and availability.
- exposed data leads to identity theft, compromised accounts, legal concerns, damage to reputation, & etc.
- to understand if the data should be exposed is to understand its:
    - authorized 'users'
    - regulations
    - conditions when the data is accessed
    - the impact of the disclosure
    - value of the data
  
  - integrity
    - two types:
        1. physical data integrity - actions and fail-safes that protect the physical systems that store and process data.
        2. logical data integrity - digital checks and protocols that protect the data from human error and hackers.
- tools for understanding unauthorized information alterations
  - alteration threats:
    - financial records
    - vote totals
    - health records
    - news stories
  - tools
    - file integrity monitoring (audits senstive information, and folders for safeguarding & making sure all activity is authorized.)
    - relational database management system (records the user access and data changes)
  - data integrity
    - prevents unauthorized users
    - prevent unauthorized data changes
    - use error checking and validation

- availability
  - authorized users having immediate, reliabble access ot their data
  - threats against availability:
    - various forms of sabotage to cause harm to the organization
    - e.g. DoS - overwhelming the system with traffic
  - non-threats against availability:
    - hardware failure, unscheduled software downtime, & network bandwidth issues

- regulatory standards:
  - e.g.
    - HIPAA - Regulates the use and disclosure of protecting health information
    - GDPR - regulates digital privacy for all countries in the EU.

- CIA Triad
  - data being protected from unauthorized access, unauthorized changes, and the authorized data access *WHENEVER* you need it.

### Security & Information Privacy

- intellectual property
- how to turn data into information
- the different types of confidental information

*Intellectual Property*
- creations of the mind
- It's protected ny copyright, trademark, and patent law
- e.g. industrial designs, trade secrets, and research discoveries


*Information assets*
  - physical or digital information that deemed valuable to a company or organization.
  - information is a summary of raw data
- Digital Products
  - e.g. software, e-books, or web elements
  - company must protect it's products from piracy & reverse-engineering
  - DRM *digital rights management*- code that's directly related to the prevention of digital assets from being copied or pirated.
  - DMCA - *Digital milennium copyrights act* - makes it illegal to copy or develop bypassing technology for copy protections


*confidential information*
- `PII` - any information used to identify someone
  - government ID numbers, birthdates, addresses. phone numbers 
- `Company information` - any information used to run a company
  - e.g. IP, designs, procedures, plans, records, and financial data
- `customer information` - customers or partners information that's provideable to companies
  - PII, purchase histories, credit card information
- `PHI`- patient medical record information (diagnosis/treatment)
  - MHR, prescription lists, PII

- PII, often interchangably with PCI & SPI
  - `SPI` - information that doesn't identify but can cause harm if made public
  - `PCI` - customer informaiton the identifies and describes a customer

*Microsoft Windows: Server Lab Env*

- differentiating various windows server editions
- performing taks in temp lab sessions

- ability to config servers for large organization

*Threats & Breaches*

- identify types of security threats
- examples of the threats
- differenitating between worms and trojans

- hardware threats
  - including security policies that lead to physical threats, tampering, and/or theft of hardware.
- data threats
  - inlcuding data leaks, breaches, and dumps
  - dumpster diving, which then requires companies to shread important paperwork to avoid this.
- insider threats
  - including employees, hackers
- software threats
  - that includes theft, exploits, and malwarem

- software threats
  - to avoid it:
    - not opening strange attachments or links
    - back up data
    - using strong antivirus software
    - regularly updating software
    - using strong passwords

- malware threats
  - includes viruses, ransomware, spyware, adware, worms, trojans, and exploits.
    - viruses extend to affect from host to host
      - ability to corrupt files, hijack emails, steal data, record keystrokes, and turn on webcams
      - `program viruses` - code that insert themselves into another program
      - `macro viruses` - affect MS office files via macros used for task automation 
      - `stealth viruses` - replicate themselves to different locations for avoiding antivirus scans
      - `polymorphic` - changing their characteristics to get around cybersecurity defenses.
      - `worms` - viruses that start themselves *AFTER* identifying system weaknesses
      - `trojans` - tricks you into installing legitimate-seeming software that includes harmful malware

- hands-on lab
  - understanding the process and steps on:
    - addressing known vulnerabilities
    - fixing bugs
    - protecting against new attack types
    - adding new features
  - steps for understanding the lab:
    - reviewing and checking for windows updates

- threat types:
  - objectives:
    - understanding how snooping works
    - what botnets are used for 
    - identifying a DoS attack

  - snooping
    - used to intercept data between devices
    - attack types:
      - eavesdroping / packet-sniffing - tool used to intercept data from wireless, wired and phone connections
      - replay - intercepts and retransmits data (needs a access token or security key)
      - man-in-the-middle - it requires victims, receipt point, and an attacker (physical or logical)
    - XXS (cross-site scripting) - attackers attaches code onto a trusted side. Activated based on the usage of the user not the hacker.
      - link with malicious code in a legit URL
      - preventing this:
        - validating inputs
        - sanitizing data (scanning for malicious code)
        - set cookie rules or JS access
        - config a web appl firewall rules for stopping XXS & other scripts
  - SQL injection
    - attackers using code to bypass website's security protections
    - `syntax error` - hacker has access to protection information, able to download website's database or even delete it
    - avoid SQL injection:
      - parameterize queries (i.e. have predefined queries)
      - store provedures
      - using a allowlist
      - escape user input
  - botnets
    - collection of compromised malware-infected computers
    - e.g. cryptomining
  - DoS attacks
    - floods networks with alot of traffic that crashes
    - used to distract from simulataneous attacks
    - e.g. 
      - buffer overflow - more traffic than it can handle
      - ICMP flood - pings sent to every computer on a network to create a crash
      - SYN flood - series of incomplete connection requests floods the website until that server crashes