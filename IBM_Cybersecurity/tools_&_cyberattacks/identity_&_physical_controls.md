# Identity & Physical Controls

### identity and access management (IAM)
- early days

- in the early days of the internet, the internal network was the first line of defense
- the main objective was spliting the internal and external network (internet)
- problems occured:
  - bad actors would possibly on the internal and good actors would be on the external network
- solutions:

- `admin management` ~  identity governance
  - creating accounts, updating, & deleting it
  - provisioning accounts
- `authentication`
  - authenticating your identity
- `authorization`
  - allowed to doing certain tasks
- `audit`
  - correctly validating the first 3 A's

### Authentication
- purposes
- protocols
- servers
- methodologies

- purpose
  - validation of an identity

- protocols
  - digital rules and process systems
  - checks digital credentials
  - e.g. RADIUS - remote authentication dial-in user service
    - client-server used for remote user authentication
    - used for wireless and VPNs
  - e.g. 2 - CHAP - challenge handshake authentication protocol
  - e.g. 3 - EAP - extensible authentication protocol
  - e.g. 4 - kerberos 
    - uses encryption to protect user credentials between client and server
    - relying on 3rd-party servers known as key distribution center `KDC`
      - e.g. windows active directory

- servers
  - manages user credentials
  - verifies identities
  - grants access to protected resources or systems

### Authorization
- purpose
- access control schemes
- various file controls

- purpose
  - determines the granting and deyning of certain tasks

- access control schemes
  - how authenticated users access and use resources in a system
  - set permissions and roles dictating the user's access levels
  - `role-based access controls`
    - assigns system permissions to users based on their roles
  - `attribute-based access control`
    - the attributes that make access decisions for: users, resources, actions, and environmental context
  - `rule-based access control`
    - specific rules or control list to different objects or resources
      - e.g. firewall rules
  - `mandatory access control`
    - enforces access regulations determined by the admin
  - `discretionary access control`
    - assigns ownerships to various objects (files and directories)
    - e.g. file access controls

### Access Controls
- description
- role of identities
- innovative and traditional methods

- security measures that authorized personnel are allowed to view, and make use of the content
- access management:
  - processes and technologies, that controls and monitors users' access

- identities
  - helpful for access management
  - acts as digital representations
  - e.g.
    - username, password, or IP addresses
  - attributes
    - serves as the digital footprint
    - basic details
- methods
  - regulates access for digital and physical resources
  - traditional methods:
    - usernames
    - certificates
    - SSH keys
    - tokens
    - smartcards
  - innovative methods
    - biometric systems
    - behavioral systems
    - MFA
    - SSO
    - geolocation and time-based restrictions

### Multi-factor Authentication
- IAM breakdown

- authentication
  - factors that determine the question, who are you:
    - knowing
      - e.g. passwords or pins
    - having
      - e.g. mobile phone
    - are
      - e.g. your face, biometric

### Single-Sign on
- determining a password manager that utilizes PC sunflowers
- using MFA for the SSO

- problems:
  - introducting a single-point failure

### Passkeys FIDO
- better security and usability without having passwords
- device lost scenarios
- multi devices
- SSH, & PGP
- PW problems & manager

- when there's a device lost, there's account/device recovery
- with multiple devices, the ability to synchorization capabilities
  - e.g. enabling these functions within a cloud