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
  - FAT
    - simple storage formats and floppy disks
    - features
      - compatability
      - easy management
      - limited storage
  - NTFS
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
