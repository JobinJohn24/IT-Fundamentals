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