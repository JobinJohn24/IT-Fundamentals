### Malware

- the collective name for software that's designed to disrupt or damage data, software, or hardware.

*viruses*

- software that's written to insert copies of itself into applications and data
- self-replicating programs
- attached to specific applications on a computer but activated when the program is first run.
- intended to corrupt the data, attack the operating system, providing exploitable 'backdoors.'
- they consume memory, disk space & processing power.

*worms*

- spreadable through network connections, and hijack resources.
- stages of a worm attack:
  1. worm probes machine that looks for vulnerabilities.
  2. penetrate vulnerable machines by performing operations for exploiting the vulnerabilities. (e.g. detecting a open network connection)
  3. worms will download itselt to the remote machine, and store itself.
  4. the worm will propagate itself by picking new machines to attempt to probe.

*trojans*

- disguised an a legitimate program, that would allow someone else to gain control, copying keystrokes, or using the email software to pass itself onto other companies.
- they primarily cause problems for android apps.
  - why?
  - android natively support sideloading - where you download & install files from anywhere.

*spyware & adware*

- adware forces users to view advertisting 
- spyware is attempting to access personal information and user passwords. 

*case study: conficker*

- windows computers was infected by a worm called conficker, which was spread when users shared files, through other networks or USB flash drives.
-  the authors constantly released new variants to overcome weakenesses based off the original malware.
-  It included digital signatures to prevent hijacking the program

*Phishing*

- attempting to steal valuable information by pretending to be a trustworthy person (form of social engineering)
- email phishing: 
  - AOHell allowed AOL users to impersonate other people
- social media:
  - used in social media sites as in SMS
- attackers will include malware-infected software in personal messages posted in social media.
- spam:
  - email is transferred using SMTP (simple mail transfer protocol) 
  - SMTP is a set of protocols used to specify set of messages that's exchanged between a computer and their functionality.
  - original SMTP had no authentication method, so SMTP-AUTH was designed to authenticate the user that corresponds to it. 

*spoofing:*

  - attacks the system by changing the email 'envelopes.'
  - disguises the actual address by writing new addresses for the sender & destination.
  - estimated to be 7 billion spam messages, which accounts for 85% of all email messages in 2011. 
- spoting a phishing email:
  - recognizing the sender
  - understanding spelling mistakes
  - poor quality images
  - email contents
  - links

*role of malware in click fraud:*

- e.g. money spent on advertising growing rapidly with more than 16 billion euros spent in the UK alone. Expected to exceed 26 billion euros in 2020.
- common type of advertising is 'pay per click' which advertisers pay the owners of a site when user clicks on an advert.
- types of click fraud (using botnets to generate clicks):
  1. clicking on targeted company ads to waste their advert revenue.
  2. criminal sets up dummy websites (a duplicate of original sites), they sign up for adverts (adsense with Google). They use a bot network to click on ads to collect shares of the ad revenue based on clicking on the advert.

*use cases of click fraud:*

- FBI broke a click fraud operation that infected 4 million computers in 100 countries that stole over $14 million from advertisers.
- a russian group created 6,000 websites with 250,000 pages with video adverts, and using a bot network it was able to 'watch' the videos over 300 million videos ads each day. This generated over $4 million a day.

*Botnets*

- there are harmful and harmless botnets
- harmless botnet:
  - internet relay chat: used to automate tasks across multiple computers.
- process:
  - botnets spread by worms & viruses.
  - They use internnet to make contact with a control computer & infect it (making the computers that's compromised a `zombie`)
  - The zombie computer won't do anything further than periodically check for instructions from the control computer.
  - over time, more computers become zombies.
- primary use:
  - flood the internet with spam messages
  - commit fraud against adverts
  - performing DoS attacks on companies and governments.

*Antivirus Software:*

- developer of computer operating systems are incorporating a wider range of security features that stop malware from running.
- aimed to detect, isolate and delete malware on a computer before it can harm data.
- uses two techniques for detecting malware:
  - signatures:
        a. signature is a distinctive pattern of data in memory or file
        b. software only catches bad files if it's already been seen & cataloged before.
        c. the time-gap (zero day) provides notice that a new hack being investigated and the antivirus company sending out an update to fix it would be create a gap in time.
        d. variants can be created by releasing different versions of the same malware. This would require the antivirus company to issue new releases.
        e. polymorphism can deal with sophisticated malware, this can avoid matching any static comparitive to the original malware.

  - Heuristics:
        a. a software that initiates solutions based on the list of suspicious behaviors.
        b. detects malware from behavioral features not signatues.
        c. it tests suspicious files inside a safe env to watch malicious actions.
        d. addresses the 'zero day' malware even before the signature is created.
        e. limitations include: the behavioral rules are based on past criminal activity, if the criminal invents a radical, and unique way, then the malware will 'walk right past' undetected.

- limitations for anti-virus:
  - failing to update itself
  - consuming large amount of compute power
  - inaccuracy

*use cases for anti-virus software:*

- british police shut down two indian call centers over their initiatives of using web pages and phones call to sell fake computer security services.
- city of london police reported 2,000 cases to the Action Fraud every month.

*keeping everything up to date:*

- `patching` - updating the software created through automation, which checks software updates, prompting user to install the updates, and performing the update.

*end-of-life software:*

- companies will cease telephone and internet support for queries.
- older products would be exposed to more vulnerabilities for longer because of the constant maintanance of newer products.

*sandboxes & code signing*

- software sandbox - running programs in a controlled environment. Allowing limited access to resources like OS files, disks & network.
  - sandbox will theoritically not allows software to break through the sandbox even if malicious software attempts to overwrite parts of the disks.
  - use case: modern web browsers utilize sand boxes to prevent internet content causing damage to files on the computer.

- code signing - authentication checks from digitally signed copies of programs that issued from software companies.
  - windows uses code signing to have direct access to the heart of the OS.
  - apple's OS version restricts users to only running programs certified by Apple (greater advantage against malware) but restricts choice & prevents users from running unsigned applications from 3rd parties. 