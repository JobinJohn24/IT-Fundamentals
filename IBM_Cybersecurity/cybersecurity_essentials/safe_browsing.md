# Safe Browsing

# Application Ecosystem Security
- software and application security concerns
- how they're compromised
- types of data that's 'appealing' to hackers

- mobile applications
  - prone to be less secure
- rooting & jailbreaking
  - removing device restrictions and installing non-approved applications
  - add functionality but adds vulnerability
- desktop software
  - used to open files stored locally or in the cloud
  - IT departments will provides patches & updates in software to avoid vulnerabilities
  - steps for secure:
    - strong password
    - physically safe
    - using anti-virus & VPN software
    - only browsing HTTPS sites 
    - enabling automatic updates
- business software
  - automates transactions
  - mines sales data
  - manages information
  - ransomware & cyberattacks are used to steal sensitive data
- corporate network
  - protecting files, systems, and resources are a way for business for avoid cyberattacks & malware
  - they have options:
    - having an internal network sharing on company-owned hardware
    - enterprise-level versions of Box, OneDrive, or Google Drive

### Public Browsing Risks
- security concerns for public browsing
- public browsing risks
- types of data stolen from public network

- open network
  - open networks aren't encrypted
  - often invite eavesdropping from hackers

- session hijacking
  - hackers can take over your phone/device to intercept & hijack your connection
- shoulder surfing
  - strategically sitting to try to see essential information

### Plug-ins, Extensions, and Toolbars
- config a browser foe safe browsing
- identifying secure & insecure websites
- managing plug-ins, extensions, and toolbars

- Browsers
  - e.g. google chrome, firefox, safari, and internet explorer
- security zones
  - providing zones to block or allow website based on a confined zone
  - security zone levels:
    - medium, high, custom = local, internet, and intranet
  
- plug-ins, extensions, & toolbars
  - toolbars - old add-ons are filled with bloatware & malware
  - extensions aren't supported by today's browsers
  - extensions add features and functions

- cookies
  - text files with small pieces of data
  - process:
    1. connect to internet
    2. go to site
    3. web server replies with site & cookies
    4. cookies are saved to browser / hard drive
    5. when the site is revisted, the server IDs the user and records data that can be shared

- Cookie types:
  - session cookies:
    - used for one session
    - uses RAM
    - automatically deleted with session ends
  - presistent cookies
    - remain on computer indefinitely
    - some may have expiration dates
  - authentication cookies
    - saves logins, usernames, and passwords
  - tracking cookies
    - tracks multiples visits to a website
    - e.g. online store use them to send targeted ads
  - 1st party cookies
    - safer
  - 3rd party cookies
    - from sites you're not on
    - tracks across the web
    - ads generate the cookies
  - zombie cookies
    - saved directly to your device 
    - difficult to remove
    - used to remove specific users
    - ablitiy to regenerate after deletion

- Security certificates 
  - secure socket layers authenticate a website's identity and enable encrypted connection (between web server and browser)
  - provides a secure tunnel between the web server and browsers
  - root certificate stores:
    - certificates of authority
    - apple
    - microsoft
    - mozilla
    - google
  - SSL certificates:
    - used to keep user data secure
    - prevent fake sites
    - conveying trust to users
    - verifiying ownership of sites

### Safe browsing techniques
- cache used for
- safe websites
- adware risks

- autofill management
  - used to replace manually filled form fields

- browser cache
  - storage of downloaded web pages that've been visited
  - large cache causes slower performance
  - browser history is store

- private browsing
  - doesn't save browsing history, cookies, site data or form data

- malicious websites
  - URLs use misleading characters
  - poorly designed

- safe websites
  - use 'whois lookup' tool
  - check for trust seal
  - inspect URLs

- adware & popups
  - malware that displays unwanted ads
  - often combined with apps, and it activate on install 
  - it'll track your online activity
  - collects the users data 

- warning signs
  - search engines use algorithms for detecting harmful sites
  - harmful site will contain:
    - adware
    - malware

### Lab: Managing browser security and privacy settings
- performing safety checks
- options for clearing browsing data
- check and clear browsing history
- config settings for privacy & security

### VPNs
- different VPN connection types
- pros & cons of hardware & software VPNs
- network hardware used to create VPNs

- VPNs
  - encrypted tunnel set up between 2+ sites
- site-to-site VPN
  - two sites connect across an existing internet connection with a VPN device
- host-to-site VPN
  - remote user needs to connect securely to a site
- host-to-host VPN
  - when two remote users securely connect to each other

- VPN hardware
  - devices designed to create VPNs
  - Network devices with VPNs functionality
  - routers, firewalls, VPN concentrators (multiple VPNs being connected)
  - its including in:
    - virtual LANs
    - Operating systems and browsers (windows, MacOS)

- IPSec (Internet Protocol Security)
  - a set of protocols that utilize cryptography to protect data traveling over the internet
  - core protocols:
    - authentication headers (AH)
      - authenticates senders and IP addresses
    - encapsulating security payload
      - encrypts and authenticates the data
  - two modes:
    - tunnel mode
      - entirety of the data is wrapped in a packet with a new header (common: site-to-site VPN)
    - transport mode
      - IP header of the data is left unencrypted (common: host-to-site VPN)
  - uses security features:
    - security associations
      - which type of hashing and encryption are used
    - internet key exchange
      - secures exchange of cryptographic keys
    - encryption and hashing algorithms
      - algorithms that scramble data
    - anti-replay protection
      - standard that stop hackers from using the data