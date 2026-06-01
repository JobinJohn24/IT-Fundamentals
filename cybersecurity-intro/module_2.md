# Authentication

### objectives

- purpose of passwords
- different situations in which they're used
- ways in which attackers try to learn your password
- ways in improving the security of passwords
- online identifications methods

### passwords

- transport layer security is responsible for encrypting the communication between the user and server.
  - `https` =  the communication between the web browser and server are fully encrypted before transmission, completely unreadable.
- `hashing` = function of converting the users passwords into a mix of ascii characters (upper & lower case) and digits.
- `salting` = random values added to the plaintext password before the hashing process.
  - conditions:
    1. if the hashing function generates 256-bit hashes, then 256-unique salt should be used for each password.

*use case - RockYou*

- RockYou compromised 32 million users.
- It stored users passwords in plaintext.
- Encouraged the insecure passwords by having *ONLY* 5 alphanumeric characters long (which increased the vulnerabilities)

*breaking into passwords:*

- dictionary attacks - automatically breaking into computers.
  - system admins would perform dictionary attacks to identify weak passwords.
  - often times DA will be targeted attack, instead of randomized combinations of letters
- brute force attacks - methodically attacking through all possible passwords
  - using mathematical computations to generate & try every single possible combination of unicode, digits, and ascii characters.

*Case Study: Linkedln*

- Linkedln was attacked by russian hackers.
- The stolen accounts contained hashed values but the passwords *WEREN'T* salted.
- the hashing algorithm that was using SHA-1 hashing algorithms was used. (algorithm that can calculate millons of SHA-1 hashes per second.)
- The passwords were decrypted within a day, which prompted Linkedln to ask users to change their passwords.

*Proper Passwords*

- avoid picking a passwords that're associated with the following:
  1. pets
  2. quotations
  3. DOB
  4. nicknames
- long & complex *ALWAYS* wins.
- consider using a password manager
  - makes complex passwords for websites / applications
  - avoids phishing
  - using openlearn's resources to construct a password and enabling password strength checker:
[Password Strength Checker](https://www.open.edu/openlearn/pluginfile.php/4488604/mod_fullscreenresource/content/1/password_check/index.html)

*password manager*

- password manager is an application that stores passwords.
- it offers password generation 
- examples of password managers:
  a. lastpass - (operating systems & mobile devices) generates & store passwords & managing the passwords across multiple device.
  b. 1password - (windows & mac) open-sourced, holds confidential documents, and password synchronisation through dropbox service
  c. keepass - (windows, linux, & mac) open-source password manager.

*Password manager alternatives:*

- OAuth provider (e.g. Google) used as a way of checking a user's identity that requires websites to ask the user's computer for some proof. 
- The OAuth provider will generated a digitally signed token that confirms the user's identity.

*Two-factor authentication*

- two pieces of information that makes an account more secure.
- examples of systems that utilize two-factor authentication:
  1. banking card reader - inserting your card and requiring you to provide a pin will allow the user to access their account.
  2. two-factor authentication on web - e.g. apple, ebay, google & microsoft
- special hardware key - restricting authentication to the computer with a unique hardware security key.
- two-factor authentication is also required when connected to a VPN. when connected, you're given a VPN token that generates a sequence of random characters.

