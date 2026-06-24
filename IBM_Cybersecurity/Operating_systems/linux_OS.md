# Linux OS

### Linux Systems Overview
- open source software with importance
- linux desktop OS editions
- differences between CLI & GUI

- open source
  - allows users to view, modify, and distribute the source code

- linux desktop OS editions
  - kernel
    - used for managing hardware resources
  - package management systems
  - distributions:
    - `ubuntu`
      - intuitive desktop experience
    - `fedora`
      - utilizes Btrfs (B-Tree Filesystem)
    - CentOS
      - providing stability and security
      - popular for server deployment
      - distribution of RHEL source code
    - debian
      - community-base source code
    - linux mint
      - user-friendly
      - transition from other OS's
  - interfaces
    - `command-line interfaces` (CLI)
      - complex tasks through command input
      - ideal for automation and scripting
      - consumes fewer system resources
    - `Graphical User Interface` (GUI)
      - visually representation of information, files, structures, and system resources
      - multi-tasking
      - more resource-extensive

### Linux OS Essentials
  - creating a local system account
  - viewing system information
  - using Ubuntu file system
  - monitoring system performance

- creating a local system account
  - settings
  - unlock
  - add user
  - click standard user account
    - fill out the credentials:
      - full name & username
      - password
      - `add`
    - switch user

- system information
  - activities
  - type about in the search bar
  - find the hardware specifications on the left-hand side
  - viewing the preconfigured folder categories

- monitoring system performance 
  - activities
  - search bar
    - `system`
  - select system monitor
    - views:
      - processes 
      - system information
      - resources

### Linux Terminal Overview
- linux shell 
- linux terminal
-  shell and terminal working together
-  using terminal to navigate directories  

- linux shell
  - OS-level applications that interprets commands
  - performing:
    - write, and read files
    - move, and copy files
    - filter, and extract data
  - shells:
    - bash
    - Zsh

- linux terminal
  - application used to interact with the shell
  - entering commands and receives output from the terminal

-  shell and terminal working together
   -  user -> terminal -> shell OS kernel -> hardware
   -  paths in the file sytem:
      -  `~` home directory
      -  `/` root directory
      -  `..` parent of current directory
      -  `.` current directory

### Reading - Linux Commands
- purpose of common linux commands
- terminal window to input linux commands

### Common Linux Commands
- shell
- common bash commands

- common shell commands
  - printing file and string
  - network operations
  - monitoring performance and status
  - working with files and directories
  - running batch jobs

- Scripting commands based on functionality
- getting information
  - whoami - username
  - id - user and group ID
  - uname - operating system name
  - ps - running processes
  - top - resource usage
  - df - mounted file systems
  - man - reference
  - date todays date
- working with files
  - cp - copy
  - mv - change file name
  - rm - remove files
  - touch - create empty file
  - chmod - change and modify file permissions
  - wc - count of lines
  - grep - return lines in matching patterns
- navigating with directories
  - ls - list files
  - find - find files
  - pwd - get present directory
  - mkdir - makes new directory
  - cd - change directory
  - rmdir - removes directory
- printing files and string contents
  - cat - prints entire content
  - more - print file contents
  - head - print first N lines of file
  - tail - print last N lines of file
  - echo - print string or variable value
- compression and archive
  - tar - archive file
  - zip - compress file
  - unzip - extract file
- networking
  - hostname - prints hostname
  - ping - packet sending to URL and prints response
  - ifconfig - configures system network interfaces
  - curl - contents of file of the URL
  - wget - download file from URL

### File System Mangement & Directory Structure
- files and directories
- comparing directory structures
- linux key directories & it's role

- files and directories
  - building blocks for organizing data
  - files
    - units that stores data
  - directories
    - holds information about files and directories
- Directory structure
  - foundation for all directories and files
  - provides write access only to the root user
  - root vs /root
    - foundation of the file system
    - specific directory of the slash partition
- common directories
  - /bin
    - essential binary executables
  - /sbin
    - system maintenance tasks
  - /etc
    - stores configuration files for installed programs
  - /var
    - constantly changing or growing data files 
  - /tmp
    - stores files that's clear upon system reboot
  - /home
    - stores users personal files
  - /boot
    - essential for system startup