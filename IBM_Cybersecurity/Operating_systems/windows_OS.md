# Introduction to OS

- file systems
- user accounts
- 32-bit & 64-bit applications
- windows user mode & kernel mode components
- windows security settings

### Introduction to Windows OS
- OS purpose & functions
- types of OS
- OS generations
- history of modern OS

- purpose & functions
  - functions:
    - input, output, processing, & storage

- history
  - gen 1:
    - OS for multiple computer were nonexistent
  - gen 2
    - mainframe computers used for commercial and scientific use
    - IBM; first company to create OS to accompany computers
    - embedded OS used for single tasks, and recieving second response times (low latency)
  - gen 3
    - companies started creating thier own batch files OS
    - network OS that supplied scalable and secure network communications
    - creation of UNIX OS that's adminstered among multiple computers which features processor timesharing
  - gen 4
    - multitask OS
    - mobile OS: e.g. android, windows, iOS, and windows

### Windows System
- editions
- features of each edition

- windows 10
  - adaptable OS
  - multiple editions tailored to needs
  - updates designed for features, security
  - features:
    - onedrive
    - cortana
    - windows defenders
  - windows 10 pro
    - business-oriented version
    - features
      - remote desktop
      - bitlocker
      - windows domain
  - W10 enterprise
  - features
    - applocker 
    - experience control
  - W10 for workstations
    - features
      - 4 CPUs
      - 6 TB of RAM
      - ReFS (better data protection)
- W11 Home
  - enhanced security features
  - secure boot
  - firewall and network protection
  - W11 PRO
    - better device security
    - features
      - parental control settings
      - internet protection 
      - windows hello
    - W11 Enterprise
      - features
        - OS deployment
        - universal print
        - autopatch
        - app and device management
    - W11 PRO for Workstations
      - features
        - 4 CPUs & 6 TBs of RAM

### File Systems
- functionality
- types
- file allocation table (FAT)
- new technology file system (NTFS)

- filing systems functions as a digital interactions across devices
- retrevial from hard drives, and SSDs

- functionality
  - works with metadata
  - monitors and retrieves files
  - structure:
    - arrangement of files and directories in a tree-like format

- types
  - `FAT`
    - simple storage formats and floppy disks
    - features
      - compatability
      - easy management
      - limited storage
  - `NTFS`
    - standard OS
    - support large volumes of data
    - maintains a change journal
    - enables setting disk quota limits
    - uses a master file table
      - better file access and data recovery
      - support file permissions and encryption

### Directory Structure
- user, windows, and program file directory
- hidden 
- 32-bit and 64-bit directories

- windows
  - organization of files in a hierachical sense
  - seperates settings and files
  - serves as the primary storage location
- user
  - stores user information and settings
  - includes:
    - desktop
    - downloads
    - documents

- Hidden directories
  - enhances the OS functionality and security
  - prevents accidental modification and deletion
  - PerLogs, pagefile.sys, hiberfil.sys

- architectures
  - 32-bit
    - processes 32 digits simultaneously
  - 64-bit
    - handles 64 digits at once

![alt text](<Screenshot 2026-06-18 at 12.01.06 AM.png>)
*Bits Architecture Table*

### User & Kernel Modes
- troubleshoot issues
- communication of modes


- processor modes in kernel, and user mode
- user mode
  - works in a restricted mode
  - prevents direct access to hardware and system components
  - virtual address space is limited
  - prevents damage to OS

- kernel mode
  - reserved mode
  - allows interactions between OS and hardware
  - e.g. printing a document supplies the software connection with the physical hardware (printer)
 
  ![alt text](<Screenshot 2026-06-18 at 8.57.58 PM.png>)
*Communication between modes*

### Windows Servers
- functionalities
- funtionalities of network services
- features and components of security and access of Windows Server OS

- windows server
  - responsible for:
    - storing data
    - communication for businesses
    - management of network
  - functionalities
    - virutalization options
  - features
    - active directory
      - centralized system for authentication, directory services, and policy enforcement
    - hyper V
      - multiple virtual machines on a single server
    - powershell
      - scripting and automation framework

- network services
  - features
    - DNS
      - converting domain into numerical IP addresses
    - DHCP
      - assigning addresses, subnet masks, and other config params
      - simplifies network management
    - RDS
      - remote management capabilities
      - manages servers remotely
    - VPN
      - enables secure remote access

- access controls and security
  - used for safeguarding user identities, data, and storatge

### Windows command prompt tools for admin
- prompt interface
- types of OS user accounts
- features that use command prompt tools

- CLI
  - interface for executing commands
  - performing tasking
  - config systems

- user account OS types:
  - `standard user account`
    - used for regular tasks BUT not criitcal system-based changes
  - `admin account`
    - perform admin tasks
      - managing accounts
      - CLI tools
      - changing system settings
      - installing software

- group policy
  - managing settings on networks
  - `gpupdate`
  - `gpresult`
  - used for troubleshooting
- drive letters:
  - `vol`, `chdir`, `cd`
    - used for accessing data on other storage drives on CLI
    - having access over your file management
- system maintenance and information:
  - `shutdown`, `sc`, `diskpart`, `winver`, `format`
    - used for system controls, diagnostic, partitions, and OS version retrieval
- file management
  - `dir`, `md`, `rd`, `ren`, `del`
    - used of managing directories and deleting files
- file copying and backup
  - `xcopy`
- hostname and network
  - `ipconfig`, `ping`, `hostname`
    - used for learning more about network config, and verifying connectivity, and diagnosing network issues

### Management Console (MMCs)
- importance
- built-in functions

- management console
  - system management
  - env customization
  - snap-ins = control system management
    - provides organization, streamlined workflows
    - tools:
      - disk management
      - device management
      - event viewer
  - assigns MMC tools to users and groups

### Active Directory
- admin features
- structure: domain, forests, and trees

- helping admin manage account, network resources, and computer systems
- features:
  - OUs
    - managing resource
    - delegating admin tasks
    - manage permissions
    - apply group policy
  - security groups
    - access management
    - simpfilies:
      - permission assignments
  - folder redirection
    - from local machine folder to another on a network
  - home folder
    - admins can:
      - config
      - permission setting
      - access rights
      - maintaing security

- active directory organization:
  - domain
  - trees
    - interconnected domains 
  - forests
    - collection of domain tree with common configs
