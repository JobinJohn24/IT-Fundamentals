# Windows security

### active directory accounts and security considerations
- purpose of active directory in a windows server
- roles of domain admin account in AD management
- types of user accounts in a Windows Server env
- key functions

- directory
  - catalog or listing

- AD
    - organizational tools that manages data
    - catalogs every device, user and data elements
  - role of AD:
    - central authority
    - establishment of access and access rules
    - managing identities and relationships
  - AD Domain:
    - organization of network resources
    - single entry point
    - streamlines network admins

- roles of domain admin:
  - creating and managing accounts
  - security policies
  - installing/upgrading software
- user accounts
  - identifies for system access
  - govern access and monitory activity
  - types:
    - admin account
      - full control over domain controllers
      - tasks:
        - establishing policies
        - overseeing computers
        - managing accounts
    - guest account
      - restricted
    - KRBTGT - kerberos ticket generating ticket account
      - used internally by domain accounts
      - responsible for issuing tickets
    - help assistant account
      - used by IT support and technical teams
      - temporarily for access to a user's system
      - ensures support activites are securely done
- key functions
  - authentication
  - authorization
    - determining access rights
  - monitoring activities

### Authentication Methods
- discussing RADIUS, TACACS, Kerberos, & SSO

- methods
  - `radius` - enables remote access servers to communicate for user authentication
  - stores user credentials
  - commonly used in dial-up & VPN connections
    - helps ensure remote access to network resources
  - `TACACS` - helps separate authentication, permission, and accounting processes
  - `SSO` - using single set of log-on credentials to access applications and platforms
  - `Kerberos + Active Directory` - user account management simplified, consistent security policies, and SSO capabilities

### Windows Security Settings
- UAC
- Bitlocker & BitLocker to Go
- EFC in windows security

- UAC 
  - enhancing security and protects against unauthorized changes and malware
  - ensure users of risky behaviors
  - prompts
    - `consent prompt` - users to verify an action
    - `credential prompt` - request for admin credentials

- Bitlocker
  - using encryption techniques to convert data into unreadable cipher text
  - supporting authentication methods:
    - passwords
    - PINs
    - Smart Cards
    - TPM trusted platform module
  - can be integrated into active directory

- BitLocker to Go
  - extends the functionality to removable storage devices

- EFS
  - encrypts files and folders on NTFS volumes
  - applied to files stored locally and in shared folders
  - control access to encrypted data

### User Management and Permissions
- functions and features of security settings
- admin vs standard user differences
- NTFS & shared permissions differences

- group management
  - permission management
  - mangement of permission determinant on:
    - roles
    - departments
    - access requirements

- auditing and accountability
  - helps with identifying security breaches

- standard and admin accounts
  - standard accounts is the default account
  - admin account has privileges:
    - instally software 
    - changing system settings

- login options
  - local
  - microsoft
  - domain
    - managed by a windows server domain controller
    - used in a network env
    - access to:
      - printers and other services
      - shared files
      - network resources
    - two sets of permissions:
      - share permissions
        - used for files and folders
        - permissions access to:
          - read
          - write
          - change
      - NTFS
        - access to shared folders over the network
        - 3 levels
          - read
          - full control
          - change

### Anti-Malware Tools and Firewall configs
- WinRe risks and considerations
- defender antivirus role for protection against software threats
- antivirus and antimalware software importance

- Microsoft Defender Antivirus
  - built-in antivirus solution
  - helps prevent attacks against:
    - software threats
    - malware
    - spyware
    - viruses
  - defender protection:
    - active system tracking
    - automatic security updates
    - scan files, downloads and processes
    - uses cloud-based technology
    - security configs:
      - firewall settings
      - device security
      - parental controls

- Antivirus and Antimalware Software importance 
  - avoid to install *multiple* antivirus software simultaneously
  - antimalware advanced techniques:
    - detects malicious behavior patterns
    - system changes
    - unauthorized access attempts
    - suspicious network communications

- Software Firewall
  - tracking and controlling network communications
  - built-in feature for Windows OS
  - tracks *incoming & outgoing* network communications
  - analyzes network traffic
  - changes to notification settings
    - keeps the user informed about potential attack attempts
  - exceptions includes:
    - application
    - port numbers
    - predefined exemptions

### Windows Defender Firewall - Lab
- configuring WDF using basic user interface
- types of network profiles
- enabling and disabling each network profile
- managing incoming connections, which improves the system's security

### Firewall Rule in Microsoft Windows Defender - Lab
-


### Patching
- importance of patching & updates
- frequency of applying patching & updates
- best practices for patching management

- scenario:
  - alice, a freelance graphic designer postpones updates
  - the software crashes while finalizing projects and attempts to recover the work, which failed
  - the ignored security patch caused the data loss, which indicated a setback of several days work

- Patches and updates
  - patches improve the security software applications post-release
  - updates offer features or enhancements

- importance
  - crucial for software maintenance
  - addresses security gaps
  - for businesses, it help secure sensitive days, and ensures that it's compatible with emerging technologies

- frequency
  - having a scheduled critical update 
  - include a incremental update

- Patch management
  - systematic approach
  - includes identification, acquisition, installation, and verification
  - monitors new patches

- best practices for patch management
  - develop management policy
  - prioritize and apply critical patches
  - testing patches to prevent conflicts
  - preparing a contingency plan
  - consistent schedule for applying updates
  - employing patch management software
  - automating patch deployment across the software platforms
  - new feature incorporation
  - prioritizing patches based on importance

### Kerberos
- components
- fundamental steps for protocol's flow
- domain-based authentication systems benefits

- secure service requests over insecure networks
- utilizes cryptographic techniques and third-party mediator
- KDC (Kerberos Distribution Center) key roles
  - user authentication
  - ticket issuance
  - temporary credentials

- Protocol
- elements:
  - client with service request
  - hosting server
    - provides the requested service
  - authentication server
    - authentication and issues TGT upon client
  - TGT - Ticket Granting Server
    - issues tickets for service access
  - KDC
    - combines AS & TGS

- Protocol's Workflow:
  - client/user hash
  - TGS secret key
  - service server secret key
- Authentication Flow
  - ![alt text](<Screenshot 2026-06-22 at 2.08.49 PM.png>)
- ticket creation for the SS
  - ![alt text](<Screenshot 2026-06-22 at 2.09.53 PM.png>)
- authentication using service ticket
  - ![alt text](<Screenshot 2026-06-22 at 2.10.28 PM.png>)
- Decrpytion & Authentication
  - ![alt text](<Screenshot 2026-06-22 at 2.10.49 PM.png>)

- Benefits
  - delegates authentication
  - enables SSO
  - offers interoperability
    - standards set by IETF
  - uses renewable session tickets

### Windows Auditing
- basic audit policies
- security auditing & purpose
- creating audit policies

- introduction
  - structured audit strategy
  - regular security checks, which:
  - identifies potential threats from cyberattacks
  - tracks systems activitys
  - records the security events

- Audit Policies
  - account log-on events
    - tracks the users login details
  - account management
  - directory service
  - logon events
  - object access
  - policy change
  - privilege use
  - process tracking
  - system events

- Creating policies
  - understanding the organizational requirements
  - policy creation implementation:
    - identifying critical assets
      - sensitive data
    - actions and events
      - user access
      - potential threats
    - strucutred audit policy
      - outlining events to monitor
      - helping to manage and review the audit logs
    - implementation of the policy
      - config the network security settings
      - ensure security
    - reviewing the policy
      - updates to the audit documents

