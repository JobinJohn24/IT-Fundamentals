# Introduction to Cybersecurity

### Securing Accounts

- `authentication` - way to proving who you are.
- `authorization` - wether or not you should have access or not.
- `usernames` - which present the unquiely identify.
- `passwords` - distinct way of authenticate yourself.
- `Dictionary attacks` - a file which contains english which tries multiple english passwords for geting into your account.
- `brute force attacks` - using software to digitally try all passwords.
- `4 digit` passwords - heuristically speaking there are 10,000 combinations of 4-digit passwords. (`0000` - `9999` or `10^4`)
- `4 letters` - there are 7,311,616 combinations using letters, both upper & lower case (`52^4`)
- `4 characters` - 52 upper & lower case letters, 10 decimal numbers, & 32 punctuation symbols = 78,074, 896 combinations (`94^4`)
- `8 characters` - `94^8` = 6,095,689,385,410,816 combinations.

- websites and application should permit subscriber chose 64 characters in length. With unicode (emoji's) SHOULD be accepted.
- smart adversaries would contain values known, commonly-used, or compromised..
  - websites that have been suceptible to viruses or attack would hold previous breach corpuses.
  - dictionary words
  - repetitive or sequential characters
  - context-specific words (for gmail, the password must not contain 'gmail')
  - memorized secret verifiers should not permit subscriber to store a 'hint' that's accessible to an unauthenticated claimant:
    - should not have personal identifiable information (`what's your favorite dog breed?`)
  - should not require memorized secrets to be changed arbitrarily. (changing your password from a corporate office periodically)
    - why? 
        1. Because the passwords would be closely related to the previous.
        2. changing the password too frequently would make the user not remember the password.
- verifiers should/shall implement a rate-limiting mechanism limits the attempts of failed authentication attempts made on the account.

- multi-factor authentication
  - knowledge - password that's inherently yours
    1. one-time password - password that's texted, push notification, or sent on keychain/keyfob.
  - possesion - physically having 
  - inherence - unique to you (e.g. ideally biometric authnetication)

- SIM-swapping - your phone is associated with the unique identifier of the SIM card. (social engineering attack)
  - convincing the mobile network to swap SIM cards.
  - with the adversary understanding the process, they can gain access to band records, access to the user's phone number.
  - original phone loses cell service, while the adversary's phone "owns" that phone number.

*Types of attacks & solutions*

*Text-Notification vs Separate application:*

- having a application that provides a push notification that prevent SIM-swapping.
- authenticator applications are generally locally on the device, works offline, the requires medium about of user friction.

*Keylogging:*

- to prevent malware, or software that logs your keystrokes.
- keeps records of the keystrokes.

*Credential Stuffing:*

- Adversary using already known usernames and passwords from one website / app -> another website / app.
- preventing this, use different credentials for multiple websites or applications.

*social engineering:*

- circumstanced a belief or trust within the person that's asking/telling you to do so.
- have a healthy skepticism.

*Phising:*

- attempting to that provoke the user into clicking a link. 
- using social engineering in a technical way to convince you otherwise.

*Machine-in-the-middle attacks:*

- many machines with routers, servers that's controlled to make communication. 
- data could be stolen, looking at the data.

*Source for Attacks*

*single sign-on:*

- ability to sign in based off another website.
- e.g. logging with google, facebook, apple, etc.

*Password managers*

- software that manages passwords for you.
- ability to generate passwords for you.
- e.g. apple cloud keychain, google password manager, microsoft credential manager

*Passkeys:*

- your computer or device that generates the passkey for a new website for which you're registering.
- pair of public and private values used to authenticate your website or applications
