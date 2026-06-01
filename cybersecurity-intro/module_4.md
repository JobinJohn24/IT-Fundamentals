# networking and communication

### objectives

- learning how data is transmitted across network 
- understanding the difference between the internet and world wide web (www)

### internet

- comprised of multiple networks connected to one another.
- 'network of networks'
- key factors for internet design:
  1. each computer has same authority as every other computer.
  2. network should be able to deliver the communication.
    a. would be able to travel a alternative route to avoid the damaged parts of the network.

### how data moves through the internet

- internet traffic is split and takes the form of multiple routes through the network moving from origin to destination.
- two forms of communication:
  1. IP - responsible for addressing and routing the pieces of data across the network.
  2. TCP - ensures the quality of the message & free of corruption.

### datagram

- documents are split into small, uniformed blocks called datagrams / IP packets
- contents: 
  - header - envelope
  - payload - contents / information being delivered.
- datagrams sent through a series of computer nodes that form the backbone of the internet.
- the nodes contain:
  1. IP address (using 'whois')
  2. providing a geographical location for the node.
  3. providing the country of that node or won't even provide no location information.

- traceroute - diagnostic tool that maps the path from device to destinations.

### wireless (radio) networks

- wireless local networks have been known to be called Wi-Fi.
- wi-fi enables devices to be connected together to form a local area network
- the connection is sent through radio waves rather than through cables and wires.
- IEEE refers to wireless local area networking being compliant with the standards of the IEEE (institute of electrical and electronics engineers)

*connecting to wi-fi:*

- a station needs to know the network.
- the SSID will act as a human-readable broadcast name of the network. (service set identifier)
- wireless access points are continously broadcasted in small management packet to display their presence to any nearby devices.
- some with require the padlock password to access the network.
- SSID allows nodes on a wireless LAN to distinguish themselves from nodes on other wireless LANs operating in the same space
  - in airport, you're capable of conneting to the free wireless LAN services, then use SSID to ensure customers connect to the appropriate wi-fi network.

*Network security limitations:*

- internet routers are designed for the communication from devices to destination.
- programmed strategy:
    1. re-routing: alternative pathway for communication based on disruption or corruption.
- `packet sniffing` - individuals or malicious software monitors, intercepts, and captures raw data packets or datagrams 

*encryption in Wi-Fi*

- to address the issue of intercepting the message through the medium, encryption was 'made' to help ensure both confidentiality and integrity of the data.
- most common methods for protecting wi-fi networks from unauthorised networks:
  1. WEP (wired equivalent privacy) - static vulnerable key for all nodes. *VERY EASY TO CRACK*
  2. WPA2 (wi-fi protected access 2) - default configuration for wi-fi networks.
    a. secures the data traffic through AES *advanced encryption standard* + CCMP *counter mode with cipher block chaining message code protocol* = protecting data confidentialty and packet integrity.
  3. WPA3 - improved shared key validation through SAE *simultaneous authentication of equals* which protects the offline dictionary attacks & brute-force guessing tools.
  4. the only way to enhance security on public wi-fi network is to use a VPN.
- Using a VPN is better than the rest because:
  - WEP, WPA2, & WPA3 only encrypts the radio waves from you device to the local router. This ends as it hits the IGW. Once it's in the IGW, it's susceptible to any type of interuption.
  - VPN is better because it creates a cryptographic tunnel that wraps your data through your local router, ISP, & all intermediate internet hops.

### TCP/IP protocols

- TCP -> transmission control protocol
- IP -> internet protocol

*TCP*

- Ports - physical connection on a device (USB port)
- port number dictates how data is handled when it reaches its destination.

*Common TCP ports:*

- port 20 & 21: file transfer protocol.
  - port 20: receiving files
  - port 21: control
- port 22: secure logins to computers w/ secure shell
- port 25: sending emails w/ simple mail transfer protocol
- port 80: browsing web pages w/ hyper text transfer protocol.

![alt text](<Screenshot 2026-05-27 at 8.49.07 PM.png>)
*Figure 1 - displays the destination IP and it's port number that's established for functionality*

- Another alternative is UDP (user datagram protocol) which is used to move packets across IP address infastructures.
- Breakdown of the difference between UDP & TCP:

| Category        | TCP                   | UDP                            |
| --------------- | --------------------- | ------------------------------ |
| **Connection**  | Requires connection   | No connection needed           |
| **Reliability** | Guarantees delivery   | No delivery guarantee          |
| **Order**       | Keeps data in order   | May arrive out of order        |
| **Speed**       | Slower                | Faster                         |
| **Best for**    | Accuracy              | Speed                          |
| **Examples**    | Web, email, downloads | Gaming, streaming, video calls |

### The IP & IP addresses

*IPv4*

- in need of an update because the number of devices connected to the internet has nearly exhausted the total number of IP addresses available.

*IPv6*

- acts as a replacement for IPv4.
- it can support a theoretical 3.4x10^38 devices.
- considerable amount of time transferring every IPv4 into IPv6 format.

*reserved IP addresses*

- a good amount of IP addresses have been reserved for the following functionalities:
  - special purposes
  - diagnostic utilities
  - internal infrastructure

### DNS

- IP addresses are translated into unique IP address by a name server.
- until 2019, DNS information requested was sent as plain text & can be intercepted when data is being sent.
- after 2019, DNS requests to be encrypted increased in possibility.
  - firefox: settings -> network settings -> DNS over HTTPS checkbox.
  - chrome 78: `chrome://flags/` -> enable -> restart browser for changes to take effect.

### internet vs world wide web

- world wide web access: typed commands -> cryptic instructions -> plain text
- world wide web is a part of the internet that can be accessed through hypertext transfer protocol.
- HTTP relies on TCP for the connection between two machines -> uses IP to send & receive data. (the WWW is an example of hypertext - which are documents joined together using links)
- HyperText Mark-Up Language - programming language used to format web documents.