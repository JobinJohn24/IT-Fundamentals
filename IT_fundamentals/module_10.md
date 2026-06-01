# modern architecture & IT tools printer

### Linux Overview

- 95% running on server-side.
- devOps and cloud careers are dependent on linux skills.
- learning linux helps learning docker, kubernetes, cloud and more
- linux adminstrator is a good/quick entry point in IT
- creating, deleting & nativigating folders
- using the terminal/shell
- working with files & permissions
- install & tune packages
- Red Hat RHCSA certificate -> IT as junior administrator or techinical support engineer

### Navigating the CLI

*Common commands:*

- `whoami` -> prints the username of the current device
- `pwd` -> print current directory
- `ls` -> listing files/folders
- `cd` -> changing directories
- `mkdir` -> creating new directory
- `cat` -> printing file contents
- `touch` -> creating new file
- `nano` -> editing a file
- `echo "hello world">>hello.txt` -> redirects output to a file.

*demo - nativgating the CLI*

- setup -> creating a public instance in AWS with a public IP address & a security group allowing SSH inbounds from anywhere.
- scenario -> joined as a junior support technician. Team lead asks you to explore the linux server & do basic file and folder operations that helps getting used to the environment.
- objective -> learning how to navigate, create, and manage files & folders in a linux system.

1. create new folder `linux-practice`
2. move into the new folder
3. location of the user in the file system.
4. create a file `hello.txt`
5. list folder content
6. provide contents into the file
7. editing the file
8. creating a subfolder in the `linux-practice`
9. moving the `hello.txt` 
10. delete the file `hello.txt`
- root = super user of the system

### Bash overview/scripting

- command-line interface & scripting language for linux.
- allows you to talk to the computer, automate tasks, and chain commands together.

*Common use cases for Bash*
- ![alt text](<Screenshot 2026-05-23 at 10.29.38 PM.png>)

*Modern IT roles utilizing Bash*
- ![alt text](<Screenshot 2026-05-23 at 10.30.31 PM.png>)

*bash vs powershell vs python*

-![alt text](<Screenshot 2026-05-23 at 10.31.48 PM.png>)
- helping to apply the distinction between all three options.

*Demo - Using a bash user-data script to boostrap a AWS EC2 Linux Instance*

*Manually scripting for bootstraping a AWS EC2 Instance*

- `overview:` 
  1. creating a EC2 instance in a public subnet, ensuring security group allows port HTTP (80) inbound.
  2. passing the following scripts to install Apache as it boots up.
1. `#!bin/bash`
2. `dnf update -y` - updating the system
3. `dnf install -y httpd` - installs apache 
4. `systemctl start httpd` - starts apache
5. `systemctl enable httpd` - ensuring it starts everytime, the instance is rebooted.
6. echo "<h1>Welcome to My EC2 Instance</h1>"> /var/www/html/index.html

### Demo - web testing

- SSH inbound into the security group
- apache works on port 80 by default
- use the public IP address & put `.80` to see the https website.
- launching a instance with a bash script.
- make sure there's line breaks for every line in bash scripting.


