# Cryptography

### introduction

- any data is represented as binary format, which can be encrypted by a computer.

### terminology

- `plain-text`: information that can directly read by humans (usually not in binary format)  
- `ciphertext`: encrypted data
- `cipher`: the mathematics associated for turning plaintext into ciphertext & the reverse.
- `encryption`: converting plain-text to cipher text
- `decryption`: reversing cipher text to plain-text

### encryption keys

- the total number of keys can be scientific form as 2^key length -> 2^8 = 256 values.

*short keys:*

- it's vulnerable to brute force attacks.

### key distribution problem

- symmetric encryption *NEEDS* the sender or recipient to create a key to send to the other party.
- key distribution problem - a large number of key pairs are needed between communicating parties.
  - calculation for understanding how many key pairs must be genereated: `n(n-1)/2`
  - e.g. if ten parties wanted to communicate with each other, they would need 45 different key pairs = 10(10-1)/2 = 45.
  - e.g. a coporate enterprise network of 5,000 employees = 5,000(5,000-1)/2 = 12,497,500 keys.
- Diffie-Hellman key exchange method was used as an alternative of distributing keys without sending keys.
- symmetric encryption has the advantage of being fast & ideal for transmitting amounts of data.

### Asymmetric or Public Key Cryptography

- each user creates their own keys:
  - public key: kept safe & never distributed.
  - private key: sent to anyone who wants the exchanged encrypted information.
- both keys are known as `key pair`
- by using the asymmetric method, you would be able to have a public and private key (one that's visible & the other that's strictly secret.)
- public keys can be distributed through email attachments and public key chain servers.
- why isn't the internet encrypted?
  - because not all applications need cryptography for key tasks.
  - e.g. processing payments via online
  - e.g. securing emails

### using cryptographic techniques in practice

*protecting your email communications:*

- end-to-end encryption will require a collection of PGP *pretty good privacy* which are a collection of algorithms for symmetric and asymmetric cryptography. 
- OpenPGP was created under IETF *internet engineering task force* when software vendors develop system that can exchange encrypted information.
  - e.g. GPGMail - integrating with mail software provided by Apple.
  - e.g. Mailvelope - browser plug-in that uses an implementation of OpenPGP standard.

*end-to-end encryption as a service:*

- it can be problematic for organisations and individuals to set up software for encrypted emails on all devices that's being used.

### Cryptographic Techniques

- there are different cryptograph schemes with different applications.
- Common cryptographic techniques:
  - DES *data encryption standard*
    - dubbed as the US government standard for encrypting sensitive information. symmetric cipher using 56-bit keys.
    - later found to be vulnerable to brute-force attacks.
      - variant of DES, Triple DES was created without requiring to develop a completely new cipher. Using 3 rounds of DES and 3 separate 56-bit DES keys.
      - used in e-commerce, online payment applications, securing data
      - was recently deprecated by NIST in 2017.
  - AES *advanced encryption standard*
    - a combination of symmetric ciphers that provide enhanced security over DES.
    - widely used in commercial applications.
    - used to protect archive files, encrypting computer file systems, encrypting hard disks, securing file transmission.
  - Blowfish
    - cipher supporting variable key lengths from 1 -> 448 bits.
    - vunlerabilities have been known.
      - twofish & threefish were designed to overcome these weaknesses.

### using cryptography as authentication

- `hashing` - converting data into data of a fixed length known as a hash.
  - hasing is a one direction pathway that prevents the ability for individuals/organisations to intercept the communication.
- Hashing algorithms:
  - MD5 - known to have vulnerabilties like two different data can generate the same hash value (most common)
    - used for malware targeting windows computers.
  - SHA-1 - known to have vulnerabilties like two different data can generate the same hash value (most common)
  - SHA-2 

### digital signatures & certifications

- a digital signature is used to demonstrate that the data originated with its supposed author.
- it's used to encrypt the hash with the use of the sender's private key.

*Case study Alice & Bob - ensuring the communication is encrypted, not intercepted or altered.*
![alt text](<Screenshot 2026-05-28 at 5.45.16 PM.png>)

*The communcation route of quarterly profit statement earnings from Alice to Bob.*
- Process Breakdown:
  - `quarterly profit statement -> hash -> encrypted with a private key = digital signature -> for more security include Alice can include Bob's public key to encrypt the details of the message -> Bob will decrypt the message using his private key -> decrypt the digital signature with Alice's public key to reveal the hash -> comparing hashes of Alices' & Bob's, if both are identical then confidence is high that the quarterly profit statement wasn't altered by Eve.`

*Case Study #2 - Synthetic Key Pair for interuption:*
- Alice sent a payment to what she thought was Bob, but was actually Eve. This situation occured from Eve, because she curated a new kay pair in Bob's name & placed the copy of the public key on the public server. Eve, then, used her corresponding private key to sign the business invoice and send it to Alice.

*Counteract*
- a digital signature is a way to counteract the ability for intercepting individuals to curate their own key pair, place the copy of the public key on a public key server to mimic another's digital signature.
- a ceritificate authority verifies the ownership before the public key is trusted.
- The public key turns into a digital notarized identify card:
  - they must submit their public key to a universally trusted CA (e.g. digicert or let's encrypt) w/ legal and technical proof of identity.
  - the digital signature acts as a government-issued passport while the public key is your face.

*encrypted network connections*

- prior to 1995, customers were told to make a decision on what they wanted & make a phone call to the company as well as providing credit card information over the phone.
- secure socket layer protocol (SSL) allows web browsers to exchange data.
- transport layer security (TLS) replaced SSL.

*SSL/TLS*

- using a combination of asymmetric and symmetric encryption to exchange data.
- breakdown of the SSL/TLS:
  - handshake & ID check: when a browser connects to the website's server, it's implicitly agrees to the communication rules & verifies the identify card.
  - Secret code: the browser creates a temporary secret code, locks it based on the public key, and send it. Using the private key is the only way to read the code.
  - secure chat (symmetric): if both computers share the secret code, then the a session key is created to encrypt & scramble everything you type.
- `https` > `http` = as being more secure. 
- `http:` sends communication via data in plain text. 