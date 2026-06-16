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
