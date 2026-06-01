# Network Resources - Models & Protocols

### Different for multi-dimensionality for standard

### Standardization with a reference model

- proving more headers in an IP packet than just the source IP address.
- open system interconnection - standard model for networking 
- TCP & UDP protocols

### IP packet

- understanding if more headers are required to the IP packet
- additional headers are required for addressing the application port(s).
- the application on the source should be displayed for accurate response delivery.

*Source & Destination Ports*

- Source (sender) & destination (receiver) ports are required as well as the source and destination IP addresses.
- The source and destination ports are a distinction as to what application the VM is using and transmits the application via IP packet.
- Ports act as a local extension in a phone system of a building, or apartment units within an apartment complexes.

*Open System Interconnect (OSI) - reference model*

- a framework that breaks down how data travels across a network in *7* steps 
  7. `application:` network process to application (defines the application e.g. *DNS, HTTPS/WWW, P2P, EMAIL/POP, SMTP, Telnet, FTP*)
  6. `presentation:` data representation & encryption (session information, how to open/close sessions, how data should look, and identify any scrambling for security)
  5. `session:` interhost communication (controlling the communication)
  4. `transport:` end-to-end connections & reliability (connection between both sides)
  3. `network:` path determination & logical addressing (defines the standards for the routers, the protocols, and routing)
  2. `data link:` physical addressing (required information about switches, & their protocols)
  1. `physical:` media, signal, & binary transaction (whats the length of the cables, the cable type, signal type, the amount of cables)

*Demonstration of IP packet sending & recieving*

• Encapsulation - source software that starts from the application layer -> physical layer. Adding the data with alot of headers, encapsulating the data with 
• De-encapsulation - starting from physical layer -> application layer.

*E.g. a user is trying to access a website*
1. the application layer, presentation layer, and session layer take care of the data
2. the transport layer will add headers for the IP packet.
3. the network will attach the routing & IP addressing
4. the data link will enable the switches to deliver in the same LAN.
5. the physical layer will enable a conversion from electrical, frequencies, or light signals to transport the `message.`

*Example:*
1. user opens web page: browser sends HTTP request `application layer.`
2. HTTP creates request (e.g. GET/index.html)
3. HTTP hands to TCP at layer 4 (adding TCP header including: source port, destination port)
4. Layer 3 (IP)
5. Layer 2 (ethernet)
6. Out of the network

*Benefits of OSI Model*

- standardization & interoperability
- layered troubleshooting
- easier implementation of networking
- modularity (easier to develop software that does certain functions within the 7 layers)

### Layers Explained

![alt text](<Screenshot 2026-05-22 at 11.29.39 AM.png>)

*Overview of the layers representation and the data transferred*

• Application 
    a. closest to the end user.
    b. provides network services directly to applications (email clients.)
    c. handles request and response operations between applications and lower layers.

• Transport layer
    a. transport between two communicating hosts
    b. ports are added and interpreted here

• Networking layer
    a. move data from two hosts that aren't physically connected.
    b. IP is the main protocol.
    c. uses logical IP addressed
    d. IPsec, NAT, & routing protocols operate in this layer

*TCP/IP Model*

- routers operate in layer 3
- while switches operate in layer 2.
- the TCP model combines the application layer, presentation layer, and the session layer into the `application layer.`
- also combines the data link layer and physical layer into being the network access layer.

*TCP/IP Protocols*

- Standard set of rules for formatting and processing data that computes devices need for:
  a. send messages.
  b. understand the messages.
  c. troubleshooting when something arises.

- TCP -> used for/at layer 4 *(protocol 6)*
- connection established between client/server *BEFORE* data is exchanged.
- ensuring packets are sent without errors, in sequences, and retransmission for missed or unreliable packets.
- Slower than UDP.
- e.g. websites, email, file downloads

*User Datagram Protocol*

- doesn't use sequencing, error control, or acknowledgement
- used at layer 4 *(protocol 17)*
- faster but not reliable comparative to TCP
- e.g. video chats, gaming, application that's senstive to latency, live video streaming

### Common TCP/IP Protocols - Internet Control Message Protocol (ICMP)

- protocol used to send a message (ping), and waits for the response to understand if the receiver is *alive.*
- useful for troubleshooting.
- functions at the network layer (layer 3)
-  used in network attacks, *this is why some networks block it*
-  echo request/reply
-  `ping 8.8.8.8` - pinging google's IP address for it's DNS (IP Address translator)

*Secure Shell (SSH)*

- runs on TCP
- secure way to remotely access and control another computer over a network.
- the data transfer between the two is secure *encrypted.*
- operates at the application layer (layer 7)
- runs over port TCP 22.
- used for managing servers.
- e.g. login to remote linux system to manage it and run commands.

• Process: 
  1. client sends connection to server
  2. server sends the public key (the key is used for scrambling)
  3. neogitiating parameters and establishing connections

*Demo - SSH to an AWS linux EC2 instance from Mac/Linux clients*

- overview of demo:
- creating a instance, you can create a SSH key pair.
  - public key will remain in AWS
  - private key will get downloaded to the computer.
- the key pair is used to authenticate SSH connections to the EC2 instance.

*HTTP & HTTPS*

- using web browser, the communication between the browser and web server is based on HTTP *hypertext transfer protocol*
- set of rules for web browsers and websites used to communicate with each other.
- allows browsers to request web pages, and the websites servers to send them back.
- functions at application layer (layer 7)
- TCP port 80 at transport layer (layer 4)
- e.g. `https://http.badssl.com` - not HTTPS meaning not secure
- https - ensures anything you type, or view is protected from hackers.
- operates at application layer (layer 7)
- uses TCP port 443 at transport layer (layer 4)
- e.g. `https://www.cnn.com`

* Differences between HTTP & HTTPS:
  a. HTTPS is more secure than HTTP, it uses port 443 not port 80, and it's verifies websites via security certificate.
  b. favored by search engines and faster because of web protocols.
  c. HTTPS provides 3 security features:
    1. data integrity
    2. authentication
    3. encryption

*TCP/IP Packet Anatomy*

- Protocol: TCP = 6, UDP  = 17

![alt text](<Screenshot 2026-05-22 at 1.24.54 PM.png>)
*TCP packet autonomy*

- IP Headers enables the protocol, source IP address, destination IP address
- TCP (UDP) Headers enables the source port & destination port

*Protocol Port Ranges*

- Ports are interpreted at Transport Layer (layer 4).
- known ports: 0-1023.
  • SSH: TCP port 22 (for Linux)
  • HTTP: TCP port 80
  • HTTPS: TCP port 443
  • DNS: TCP *OR* UDP 53
  • RDP - 3389 (remote desktop protocol - microsoft protocol, where microsoft servers are trying to get to the client.)
  • MySQL - 3306
- registered ports: 1024 - 49151
- dynamic or private ports: 49152 - 65535 (the source & destination port becomes opposite when the sender versus the receiver recieves the IP packet, i.e. the client's dynamic source port becomes server's destination port, while the server's original destination port becomes the return packet's source port.)

*Client to Server Communications*

![alt text](<Screenshot 2026-05-22 at 2.39.55 PM.png>)
- overview of communication of client -> server then server -> client.
-

*Ephemeral Port Range*
- used for SSH servers
- e.g. a server with 3 active applcations/services
  - SSH server: port 22
  - DNS server: port 53
  - web server: port 80 / port 443
- a user/admin wants to connect to the SSH server to make code changes, or website.
- if the admin is trying to connect security preferences then it would connect to the SSH server use source & destination port & to send back it's vice versa.
  - source ranges from 49152 - 65535

![alt text](<Screenshot 2026-05-22 at 3.49.47 PM.png>)
*Ephemeral Port Range - Source & Destination Communication*

