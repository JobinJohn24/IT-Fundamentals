### Networking Fundamentals

## Networks

- definition, network types, types of network traffic or flow within a network, wried network devices, network cabling, data center network (DCN), Campus Area Network, wireless network devices.

- group of two or more computers and devices connected to share data (files, images, vidoes, etc.)
  - devices connecting could be: computers, servers, phones, tablets, printers, etc.
  - each device has a IP address.

## Network Types

- LAN - Local Area Network - (e.g. computer/phones/tablets/CCTV in a school network.)
- WLAN - wireless local area network - (e.g. shopping malls, airport, campus building,) uses a wireless router to connect to internet.
- WAN - wireless area network (e.g. Company LAN in germany's branch connects to the LAN in the HQ in USA through a WAN.) connecting networks over long distances, WAN connects LANs together.
  - (The internet is the largest WAN in the world.)
- CAN - Campus Area Network - multiple buildings close to each other. (e.g. university, hospital, ministry)

## Type of Traffic Flow

- unicast: 1:1, one device to another
  - Online banking for an individual.

- multicast 1:Group, one device sends data to many devices, but NOT ALL
  - IPTV server in a hospital allows patients to watch the same show or movies as the other patients.


- broadcast: (on local network) 1:All, one device sends data to all devices nearby.
  - PA system connected to a airport, whenever a board number, flight number is announced.

## Wired Network Devices

- network devices are need for WANs & LANs
- components include:
  - hub that connect multiple computing devices in a LAN.
        •disadvantage: sends data to all connected devices, filtering or intelligence, slower and less secure*
  - Switch: connects multiple computing devices in a LAN. 
        •can be physical or virtual(software)*
        •advantages: sends data only to the intended device.*
        •faster and secure, more security feature, and able to use full speed
  - router: connects between different VLANs or LAN to LAN.
        • needs to have a physical router connected to the VLAN which connects to wireless devices.
        • Using a router can help with forwarding traffic between segments within a LAN (VLANs)
        • to forward the traffic, the router *MUST* be connected to the different VLANs.
  - switch / router combo: intelligent switches that can perform switching and routing functions.


- Virutal Local Area Network: configuring a switch or virtualize the switch to have multiple or completely isolated from one another. *Virtual LANs(VLANs)*
  • Used to group devices logically.
- switch port is configured/mapped to a specific VLAN.
![alt text](<Screenshot 2026-05-15 at 11.00.58 AM.png>)
- Advantages:
    • Better security.
    • Isolation: data only goes to the right VLAN.

## Network Cabling

- physical cables used to connect computers, routers, switches, and other devices.
  - they carry electronic signals or light signals (e.g. fiber-optic cables) *that represents data*

### Common Networking Cable Types

- Ethernet Cable (Twisted pair)
  • copper, UTP cables - consists of Rj-45, with 8 twisted cables into pairs (4 pairs.)
    *Cat5e, Cat6, & Cat6a*
• transfer data using electrical signals
• supports speeds from 100 Mbps to 10 Gbps depending on the wire type. 

- Fiber-optic cables - carry out light signals used for high-speed, & long-distance connections
  • transfers data using light signals instead of electricity.
  • faster than ethernet and can travel longer distances
  • used and owned by internet providers and data centers.

### DCN (Data Center Network)

- type of LAN that connects all the servers, storages, and networking equipment inside a data center so they have the ability ot communicate at a *very high speed*
  • *translation: able to communicate, serve traffic, connect to the internet at very high speeds.*

- *High availablity or redundancy* - has multiple routers to have more than one internet connection that can serve traffic to the internet. This allows the data center to constantly be connected to the internet 

### Connecting a LAN to a Data Center

- Within safe distance (100 or less meters from the data center), a fiber-optic cable can be used as a *uplink* from the switch to the DC switch.
- With longer distances (200-500 miles away), a router is used to the connect the data center to a WAN.
  • the switch is connected to a router that connects to the WAN to the router at the data center.

### Campus Area Network

- A private, high-speed network that links several buildings.
- (e.g. - A data center will have uplinks to the WAN(building A), & LAN(building B))

### Wireless Network Devices

- needed to create WLANs
- WAPs - wireless access points - providing Wi-Fi access to a certain coverage area.
  • broadcast the wireless signals then connects through a cable into the LAN.
  • requires: a wired connection to the network for functionality.
  • in large offices/ares - separate WAPs are used for larger coverage & control.
    - building A & B will have separate WAPs to provide users a stronger signal to the switch.

- wireless router - connects my home or office to the internet & provides internet access to the connected devices.
  • has a built-in switch.

### The Internet

- consists of millions of LANs, data centers, WANs connected through routers & high-speed links creating one global network.

- The internet consists of:
![alt text](<Screenshot 2026-05-15 at 12.40.19 PM.png>)

- high-speed routers connected throughout the world.