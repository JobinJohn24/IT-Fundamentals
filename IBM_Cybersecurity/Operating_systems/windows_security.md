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

- bitlocker
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

### Antimalware Tools and Firewall configs
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