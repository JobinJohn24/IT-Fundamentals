# Threats 

*Types of actors and motives*

### Actor Types & Motives
- threat actors
- threat actors types based on motives
- importance

- threat actor
  - group or individual that causes harm on network
  - split into 5 categories:
    - `organized crime syndicates`
      - agenda of financial gain
      - mimicing legitimate websites
      - e.g. lazarus group, stole $300 of cryptocurrency accounting for 20% of losses
    - `hacktivits`
      - motivated by political or social
      - e.g. anonymous that enabled threats against government, religious, and corporate websites
    - `nation-state actors`
      - conducted by government for cyber espionage and cyber attacks
      - with the intent to destablize nations infrastructure, and steal IP
      - e.g. cyber warfare - used in the russian-ukraine conflict, used to spread propaganda and establish dominance
    - `script kiddes`
      - inexperienced individuals that use exising programs or scripts
      - with a motive of random, thrill, and excitment
      - e.g. 15 year old distributed denial-of-service attack to hack numerous websites, which led to his arrest
    - `insider threat actors`
      - stemming from former employee
      - with the motives of malice, grievance, and financial hardship or gain
      - e.g. eric snowden

### Insider Attacks

- prepetrated by people who have authorized access to resources, personnel systems, and networks
- intentional or unintentional
- types of insider attacks:
  1. `oblivious insider`
     - unsuspecting employee engages in actions that expose the organization
     - e.g. phishing scam
  2. `negligent insider`
     - individual ignoring protocols due to overconfidence in knowledge or disregard for laws
     - e.g. unsecured system or sharing sensitive information over unencrypted channels
  3. `malicious insider`
     - knowledgeable actor that exploits access to inflict damage, steal data or disrupt operations
     - e.g. motives of financial gain, vengeance, personal grivances
  4. `professional insider`
     - individual being recruited into esionage organization
     - e.g. usually working for a competitor or foreign government

### Cybersecurity Trends
- future looking like the past
- more AI-based trends in the future
- passwords transitioning towards passkeys
- since AI is increasing in popularity, then AI-based phishing emails and attacks will be more common
- deep fakes - simulations of voice, image or likeiness of an individual 
- hallucinations
  - as AI becomes increasingly more popular, the information spewed out by AI will tend to be wrong at times
  - RAG will implement better and more accurate information
- using GenerativeAI for improving cybersecurity

### X-Force Threat
- [PDF for Intelligence Index](./IBM XForce Threat Intelligence Index 2024.pdf)

*Ransomware & Malware*

### Malware
- situation: 
  - portraying as a bad actor
  - mining cryptocurrency
  - using other's system by implementing malware that uses other peoples systems to mine cryptocurrency for the individual = `botnet`
    - knowing gaming computer hold the most GPU
    - using social engineering to hide the malware in a PDF that's disguised as a textbook for a required class
    - once the student opens the PDF, the botnet code will start to install itself
    - a victim gets a malware protection service, which removes the malware
  - advice:
    - regularly updates on a device
    - use protection software
    - be ethical

### Ransonware

- different variations:
  - Data loss
    - the best prevention is a backup
  - breach
    - information will be released if not a ransom is paid
    - have strong access controls (when the right individuals should have access to the data)
    - encrypting the data
  - prevention techniques:
    - patching the software/system
    - installing anit-virus 
    - install end point response capabilities
    - end user training
      - reminding and training individuals for understanding the methodology behind the bad actors

### Preventing Malware Attacks
- defining malware
- methods for preventing malware
- malware defense enhancements 

- malicious software intended to gain unauthorized access
- forms:
  - adware
  - trojans
  - worms
  - viruses
  - spyware
  - ransonware

- preventative actions:
  - updating OS and software
  - installing trusted antivirus and antimalware
  - ensuring password security
    - implementing MFA
  - exercise caution with emails and downloads
    - for organizations and businesses, implementing an email gateway that monitors the communications for threats and training users on recognizing & handling threats
  - back up data
  - educating users


### Malware Detection with Rootkit Hunters
- how hacker leverage rootkits to gain access to a system
- analyzing how a rootkit hunter scans for malware

- hackers deploy rootkits to operate stealthily
- to help prevent this, RKhunter scans will inspect system components and compare them to a database with known *signatures* & *behavioral patterns of common malicious software*
- RKHunters functionalities:
  - scanning file systems to identify anamolies
  - detect rootkits to compare output of system commands
  - identifying backdoors or remote access tools
  - auditing system configs to detect any misconfigs
  - providing reports of suspicious activity and recommend remediation actions

### Rootkit Hunter
- Linux/Unix-based responsible for detecting rootkits, backdoors, and potential local exploits.
- commands for installing, running, and updating the rootkit hunter:
  - `sudo apt-get update`
  - `sudo apt-get install rkhunter`
    1. Enter Y/n if you'd like to continue
    2. Providing the preferred mail server config type
  -  `sudo rkhunter --propupd`
  -  `sudo rkhunter --checkall`  *Scanning the system commands, malware, linux-specific checks, network and local host checks*
  -  `sudo cat /var/log/rkhunter.log | grep -i warning` *viewing a condensed view of all scans that resulted in a warning*


### Social Engineering
- hacking of humans
- motivated by fear, or greed

- compromise:
    - control of a system
    - IP of an organization
    - credentials

- process:
  - gathering intelligence: getting information from social media or other websites
    - e.g. FB, LI, Google
    - asertaining their position, email, organization, and assistant
  - e.g. if the individual wanted/needed a better computer, then the hacker would devise an email that provides a link to get a new computer
- common solutions:
  - having a secure DNS = quad 9 provides a blacklist and restricts individuals from accessing the hackers website

