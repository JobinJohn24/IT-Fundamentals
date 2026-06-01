# IP Addressing

## Objectives
- why is it needed, dealing with them, given a block of IP address and design an IP scheme that helps break down the block of IP address into mulitple network & sub-networks to assign them to WANs, LANs, etc.
- recognizing a local IP address from a remote IP address.
- how computers deal with binary.
- conversion of binary -> decimal & vice-versa.
- hosts and network
- assigning to servers on a specific network.
- versions/types of IP adddresses.
- subnet masks
- IP address classes
- breaking down a range of block of IP addresses (using online tool)
- creating network in the cloud & practicing
- public vs private IP Addresses

## Why?
- e.g. a phone number is directly linked to a single individual & it's not used by anyone else in the globe.
- e.g. a address is given to indivduals to send and recieve mail.
- `Internet Protocol Address:` 
  - you need a client address and a server address. 
  - routing will enable users to initiate a request and the server is able to process the requrest and sends back a response. 

- IP Addresses: set of rules that govern how data is set & recieved over the internet.
- IP defines the routing used to deliver messages between devices.
- The messages using the IP protocol are called `packets`

## Format

- you can find the device's IP address using:
  1. `C:\>ipconfig` on windows
  2. `ip a` linux/macOS 
  3. `ipconfig getifaddr en0` macOS

## IP Address - Versions

1. `IPv4` - decimal notation
   • 32 bits long
   • 4 fields 
   • requires subnet mask
   • public or private ranges

2. `IPv6` - hexadecimal notation (0-9 & A-Z)
   •128 bits long
   •8 fields - each by two bytes long

## Computer's reading IP Addresses

### Numbering System - IP Address

- decimal numbering system with 10 symbols, 0-9
- binary numbering system with 2 symbols, 0-1
- hexcadecimal numbering system - 16 symbols, 0-9 & A-F

    e.g:
    • 521 in decimal
    • 521 in binary is 100000001001
    • 521 in hexadecimal is 0x209

• Computing devices use binary numbering system internally.

(e.g. typing a number on a calcualtor is converted to a binary number internally then converted back to a number based on the decimal numbering system)

### Decimal numbering system - Weights of Positions

| Position | Position Name | Weight |
| :---     | :---          | :---   |
| 1st      | Units         | 1^1    |
| 2nd      | Tens          | 10^1   |
| 3rd      | Hundreds      | 10^2   |
| 4th      | Thousands     | 10^3   |

• e.g: `5394` = (5x1000)+(3x100)+(9x10)+(4x1)
Postion, digit, weight, value = number (e.g. `5394`)

### Binary Numbering System

- Based on two symbols only: 0 & 1

- Each digit is represented by a binary digit or a bit.

| Position | Weight | Weight (Dec.) |
| :---     | :---   | :---          |
| 1st      | 2^0    | 1             |
| 2nd      | 2^1    | 2             |
| 3rd      | 2^2    | 4             |
| 4th      | 2^3    | 8             |
| 5th      | 2^4    | 16            |
| 6th      | 2^5    | 32            |
| 7th      | 2^6    | 64            |
| 8th      | 2^7    | 128           |

| Decimal | Binary  | How to Calculate the Binary Value |
| :------ | :------ | :--------------------------------- |
| **0**   | `00000` | All bits off                       |
| **1**   | `00001` | 1                                  |
| **2**   | `00010` | 2                                  |
| **3**   | `00011` | 2 + 1                              |
| **4**   | `00100` | 4                                  |
| **5**   | `00101` | 4 + 1                              |
| **6**   | `00110` | 4 + 2                              |
| **7**   | `00111` | 4 + 2 + 1                          |
| **8**   | `01000` | 8                                  |
| **9**   | `01001` | 8 + 1                              |
| **10**  | `01010` | 8 + 2                              |
| **11**  | `01011` | 8 + 2 + 1                          |
| **12**  | `01100` | 8 + 4                              |
| **13**  | `01101` | 8 + 4 + 1                          |
| **14**  | `01110` | 8 + 4 + 2                          |
| **15**  | `01111` | 8 + 4 + 2 + 1                      |
| **16**  | `10000` | 16 (The 5th bit turns on)          |

*Converting decimal numbering system to binary numbering system*
[converting decimals to binary](https://www.youtube.com/watch?v=rsxT4FfRBaM&t=58s)

### Exponent

- shortcut for repeated multiplication
- base^exponent
- any number ^ 0 = 1

### Conditions for Binary Numbering System

- largest decimal for a 8-bit is 256 [0-255]

### IPv4 Address - Hosts & Networks

- IP address, which is 32-bits long (4 bytes or octets)
- Represented in decimal numbering system format
- IP address' are made of 4 numbers/fields, separated by dots.
- e.g. `120.130.233.12`
- MUST BE LOWER THAN 255 TO BE A VALID IP ADDRESS.
- Each number is one byte (8-bits)

- A host is any device with an IP address on a given network.
- e.g. a street represents a network while the houses within the street with numbers (addresses) represent hosts.

- The copmuting devices must be able to identify the network & it's hosts parts.
- Understood through `subnet masks.`

### Subnet Masks

- Tells the computer: "Which part of the IP address is the network & which part is the device?"
- A subnet separates the network from the host.
- Represented as decimal or/and CIDR format

### Representations - Decimal 

- IP Address: `192.108.1.10`
- Subnet Mask: `255.255.255.0`

    • Explanation: Every bit establish in the network part is represented as one-bit, and a zero for the host part
    • `255.255.255.0` = `network.network.network.host`
    • 24-bits for the network and 8-bits for the host.
    • Network: `192.108.1.0`
    • Host: `.10`

### Representations - CIDR

- Classless Inter-Domain Routing - shorter way to write subnet masks.
- IP Address: `192.168.1.20/24`
- IP Address Explained: `IP.ADDRESS.00/how many bits are utilized for the network portion of the IP.`

- Understanding the binary equivalent of the CIDR/24 = `The first 24-bits of the IP Address set to 1, and the remaining 8-bits are represented as zeros.`

- ![alt text](<Screenshot 2026-05-16 at 12.30.52 PM.png>)
*Decimal & Equivalent CIDR - Subnet Mask Table*

### Subnet Mask - Practice

*Q: Find the Network ID, Host, & Subnet Mask in Decimal format.*

- E.G. `192.168.1.2/24` 


- Binary: `1100 0000.1010 1000.0000 0001.0000 0010`
- Network ID: `192.168.1.0`
- Host: `.2`
- Subnet Mask: `255.255.255.0`

- E.G. `192.168.1.12/26`

- Binary: `1100 0000. 1010 1000. 0000 0001. 00000 1100`
- Network ID: `192.168.1.0`
- Host: `.12`
- Subnet Mask: `255.255.255.192`

- E.G. `192.168.1.80/26`

- Binary: `1100 0000. 1010 1000. 0000 0001. 0101 0000`
- Network ID:`192.168.1.0`
- Host: `.80`
- Subnet Mask: `255.255.255.192`

- E.G. `192.168.1.138`

- Binary: `1100 0000. 1010 1000. 0000 0001. 0101 0000`
- Network ID: `192.168.1.128`
- Host: `.138`
- Subnet Mask: `255.255.255.192`

- E.G. `192.168.1.217/26`

- Binary: `1100 0000. 1010 1000. 0000 0001. 1101 1001`
- Network ID: `192.168.1.192`
- Host: `.217`
- Subnet Mask: `255.255.255.192`

### IP Address Classes

- Created to help assign IP addresses to big, medium and small networks without wasting IP Addresses.
- ![alt text](<Screenshot 2026-05-16 at 3.18.42 PM.png>)
*The following chart represents the classes corresponding to the default CIDR, IP address range, networks & hosts*
*ONLY includes A-C, while D-E represents multi-casting*

| Class | First Bits | First Byte Range | Network Bits | Host Bits | Default Mask          | Networks  | Hosts/Network | Designed For        |
| ----- | ---------- | ---------------- | ------------ | --------- | --------------------- | --------- | ------------- | ------------------- |
| **A** | `0`        | 1 – 126          | 8            | 24        | `255.0.0.0` (/8)      | 126       | 16,777,214    | Very large networks |
| **B** | `10`       | 128 – 191        | 16           | 16        | `255.255.0.0` (/16)   | 16,384    | 65,534        | Medium networks     |
| **C** | `110`      | 192 – 223        | 24           | 8         | `255.255.255.0` (/24) | 2,097,152 | 254           | Small networks      |
| **D** | `1110`     | 224 – 239        | —            | —         | Multicast             | —         | —             | Multicast groups    |
| **E** | `1111`     | 240 – 255        | —            | —         | Reserved              | —         | —             | Experimental        |


- IP addresses has 32-bits. The user is in charge of the amount of shared prefix (network) versus unique devices (hosts.)
    • /24 = 24-bits for network, 8-bits for hosts. 
    • /26 = 26-bits for network, 6-bits for hosts.
    • /30 = 30-bits for network, 2-bits for hosts.

- Bigger numbers after of the slash represents a smaller network. 
- e.g. /`large number` = `smaller network`

- Classes gives three bucket sizes.
- CIDR gives infinite bucket sizes.

### Organizations according to IP Address Classes

• A Class - Massive corporations, government agencies, and *early* internet pioneers 
- e.g - IBM, Apple, MIT, Department of Defense, HP

• B Class - Large universities, ISPs, medium-to-large companies
- e.g. - Microsoft, Stanford, Cisco, Ford Motor Copmany

• C Class - Small businesses, small ISPs, & individual organizations
- e.g - small companies, and local networks

### Why was IP Addresses enlisted in classes?

- Every device has it's own unique entry in the routing table, which accounts for millions of entries.
- *Instead* the class system solved by *aggregation* (i.e. grouping things together & treating them as one thing.)
- *Used to save router's memory.*

### How to distinguish between classes

• Class A - IP Address Range: 1-126
• Class B - IP Address Range: 128-191
• Class C - IP Address Range: 192-223

### Subnets

- Splitting IP Adresses into multiple subnets to be used on different network.
- e.g. subnetting a IP address is like slicing a pizza into slices.

*Why ?*

- Better management, less network traffic, improved security, easier troubleshooting, and efficient address usage (subnetting lets you size each network more appropriate)

- e.g. coporate offices established all over the United States, with the HQ in India. 
- using a WAN, you need to break down and isolate a block of IP addresses for *EACH* office.
- constriants: only able to divide the IP Address into the following: 2, 4, 8, 16, 32, 64

### TCP/IP Addressing - 

*Requirements for subnetting a IP Address:*

• amount of subnets needed
• amount of hosts need *per* subnet (*how many devices are going to be connected to the network*)

*Always aim for MORE hosts per subnets*

• Because if a new employee is added, the employee wouldn't have an available IP Addresses left.
• The business, coporation, or entity `must` account of future growth. 

*Line of questioning to understand the subnets and hosts per subnet needed*

• how many subnets are needed ?
• how many hosts per subnet ?
• what's the annual growth rate ?

*Tips for line of questioning*

- always aiming for more hosts per subnets.
- how many subnets are needed. *chances of building open satellites offices from those offices*
- understanding the growth rates of *hosts* & *subnets* 

*Examples of questioning*

• a company wants 5 different subnets.
> the subnets are divided into: employees, guest, servers, printers, security cameras.

• they list the amount of devices fit within each group
> ![alt text](<Screenshot 2026-05-16 at 7.41.25 PM.png>)
> The largest amount of devices per group is 80 devices so it drops in the `/25` because it supports 126 usable hosts.

• a single department holds 80 devices today & expects to grow by 20% per year.
> 80 * 1.20 = 96 devices
> 96 × 1.20 = 115.2 devices
> 115.2 × 1.20 = 138.24 devices
*After 3 years, the amount of usable hosts may not be enough after 3 years*
*Better choice: /24 = 254 usable hosts*

### IP Address Range Breakdown - Easy way

- network ID or network address
- usable IP addresses in the range
- the broadcast address of the subnet *it's the last IP Address in any network IP range & it's used to send to all hosts in that network*

- e.g. `192.168.1.0/24`

### Questions for Subnetting a IP Address:

1. Dividing range into `4 equal-sized` subnets
2. subnet mask
3. network ID
4. broadcast IP Address
5. number of usable IP Addresses
6. first and last usable IP Addresses

### Resources for IP & Subnet calculators

1. [Calculatequick] (https://www.calculatequick.com/technology/ip-subnet-calculator)
2. [SolarWinds Subnet Calculator](https://www.solarwinds.com/free-tools/advanced-subnet-calculator)

### Practice

- e.g. `192.168.1.0/24`
- network ID: `192.168.1.0`
- bits available for the hosts: 8-bits left since `192.168.1` represents the Network while the last 8-bits represent the hosts.
  - 2^8 = 256 total hosts, but 254 usable host addresses.
  - *Why is the first and last IP addresses not usable*
  - Because `192.168.1.0` represents the network itself & `192.168.1.255` represents the broadcast address which is used to send messages to every device in the subnet.
  - the usable range is `192.168.1.1` - `192.168.1.254`

- Adjusting to the growth of a company: You have to re-address the subnet & provide a larger subnet so it can provide more usable hosts.

*CIDR notation increases when network splits into smaller subnets*

- when you create more subnets, bits are borrowed from the host side, & used for the network side.

### Visual Representation of split network & CIDR notation increase

- /24 : `NNNNNNNN.NNNNNNNN.NNNNNNNN.HHHHHHHH`

- /24: 24 network bits | 8 host bits

• Dividng into 4 subnets by borrowing 2 host bits: `NNNNNNNN.NNNNNNNN.NNNNNNNN.SSHHHHHH`

- Network =  24 original network bits + 2 subnet bits = 26 network bits = `/26`

- when the CIDR number increases the amount of host bits, total addresses & usable hosts decrease.

- when the amount of subnets increases, the CIDR prefix increases (more host bits are borrowed from the host portion), which means a smaller amount of host bits, smaller total addresses and smaller usable hosts. 

### IP Address Range - Breakdown

- `112.168.2.0/24`

- Broadcast Address: `112.168.2.255`
- Address range: `112.168.2.1` - `112.168.2.254` 

### Finding the broadcast IP address

1. find the length of the subnet mask
2. turning all bits in the host field to `1's` (this will give you the broadcast IP Address.)

- E.g. IP Address: `192.168.2.0/24`
- Binary Equivalent: `0111 0000. 1010 1000. 0000 0010. 0000 0000`
- Broadcast IP (Binary): `0111 0000. 1010 1000. 0000 0010. 1111 1111`
- Broadcast IP: `192.168.2.255`

- E.g. IP Address: `112.168.2.0/24`
- Network ID: `112.168.2.0`
- Broadcast IP: `112.168.2.255`
- IP Address range: `112.168.2.1` - `112.168.2.254`

### Practice

- `112.168.209.33/20`

- Network ID:   `112.168.208.0`

- Broadcast ID: `112.168.223.255`

- Subnet range: `112.168.208.0` - `112.168.223.255`
- Usable range: `112.168.208.1` - `112.168.223.254`

### Subnetting Skills Quiz & Answers

[Subnetting-Skills](link to subnetting skills)
[Subnetting-Skills-&-Answers](link to subnetting skills & answers)

### Subnetting - In Details

- Taking ranges, breaking them down based on requirements, and understanding real use cases for subnetting.
- With an infrastructure, you have multiple offices, which requires different networks.
- This requires a IP addressing range that's has requirements and boundaries between the different networks.
- When subnetting, this provides more security & better performance quality.

### Splitting Subnets 

| Subnets | Bits  |
|---------|-------|
|   2     | 1-bit |
|   3-4   | 2-bits|
|   5-8   | 3-bits|
|   9-16  | 4-bits|

* Once a IP Address range is submitted, then the subnets range can be used but *NOT* the original!

### Public IP Addresses

- IP address that's available and accessed over the internet.
- e.g. when you access a website, `cnn.com`, a private IP Address is used, the wireless router will convert the private IP addresses into public to be accessible. 

- Features for *public* IP addresses

1. visble on the internet
2. globally unique
3. used for communcation
4. routable

### IP Addressed Assigned
- Addresses are assigned and managed globally by official organizations. (The IP Address Hierarchy)

![alt text](<Screenshot 2026-05-18 at 10.47.32 AM.png>)

*Representing the hierarchy of IP Addresses*
*Organization -> Continents -> Resource Allocation Hierarchy -> Service Providers*

- IANA: Internet assigned numbers authority
- RIRs: regional internet registries
    1. ARIN - North America
    2. RIPE NCC - Europe, miidle east
    3. APNIC - asia pacific
    4. LACNIC - latin america
    5. AFRINIC - africa
- NIRs: national internet registries
- ISPs: internet service providers

### Private IP Address Ranges (RFC1918) - *RFC - request for comment*

- ranges:
    1. not routable, won't directly on the internets.
    2. Can be used freely within private networks.

![alt text](<Screenshot 2026-05-18 at 11.01.22 AM.png>)
*Private IP Address Ranges based on size, comment, and common use*

### Conversion of Private -> Public

- Network Address Translation (NAT) *Port Address Translation*

- e.g your device (iPhone, computers, etc) have private IP addresses which then use *NAT* to convert the private IP to public using the router. 