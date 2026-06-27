# MacOS & Virtualiztion

### macOS overview
- apple desktop OS
- functions of common file types of macOS
- personal apple IDs and managed apple IDs
- backup solution, time machine

- Big Sur -> Monterey -> Ventura
- File Types
  - .dmg
    - disk images
  - .pkg
    - files and applications required for certain packages
  - .app
    - required files necessary for applications
- App store
  - software updates, and patches
  - enables automatic updates with the option for manual updates
- Apple ID
  - access to iCloud, app store, and device settings
- managed Apple ID
  - associated with corporate email accounts
  - enables restriction
- MDMs
  - allows businesses to manage and control devices remotely 
  - enforcement to security permissions
- Time machines
  - allows for backups for entire systems to an external system
  - receivers files 
  - ensure data security and recoverability

### macOS features
- features of macOS and tools
- using macOS to increase productivity, organization and system control

- features and tools
  - streamline workflows
  - manages files
  - safeguards data
- multiple desktops
- mission control
  - navigating between different applications and windows
- keychains
  - stores passwords securely
- spotlight
  - finding important files and documents instantly
- dock
  - centralized launch pad
  - quick access to applications, folders, and files
- FileVault
  - disk encryption feature
  - helps keep data secure
  - protects your files and fodlers using an encryption algorithm
- disk utility
  - allows to manage disk and folders
- terminal
  - command-line interface
  - run commands, launch scripts, perform system configs

### Virtualization
- benefits
- types

- purpose
  - hardware poses physical constraints
  - abstracts hardware capabilities
  - helps use, maintain, and manage hardware infrastructure
  - foundation for cloud computing
- benefits
  - resources efficiency
  - easier management
  - reduced downtime
  - faster provisioning
- utilization
  - uses a hypervisor that creates multiple VMs on one physical computer
  - hypervisor types
        1. type 1 - interacts with physical resources
        2. type 2 - runs as an application on an exisiting OS
- VMs
  - digital replicas of real computers operating in virtual envs
    - Guest - VMs
    - Host - PCs
- Types of VMs
  - desktop
    - different desktop OSs on VMs
  - network
    - to create virtual network view
    - allows admins to control elements without physical access
  - storage
    - combines storage devices into single managed unit
  - data
    - integration and simplifies data sources
  - application
    - without direct installation on the users OS
    - application, local, server-based application virutalization
  - data center
    - simplifies cloud adoption enabling establishment
  - CPU
    - dividing a single CPU into virtual CPUs for multiple VMs

### Cloud Computing Overview
- benefits 
- origin
- components
- distinguishing between different services
- types of cloud computing

- cloud
  - computing resources over the internet through a pay-per-use bias
    - more scalability
    - customer engagement

- benefits
  - reduces maintenance costs
  - elimanating the need for physical hardware

- components
  - data center
    - infrastructure
  - networking
    - used for high-speed connections
  - virtualization
    - resource efficiency

- different services
  - IaaS
    - basic computing resources
    - e.g. servers, networking, and storage over the internet
  - PaaS
    - helps to develop, manage, and deliver applications
    - e.g. servers, networks, storage and development tools
  - SaaS
    - access to a vendor's software
    - works on a subscription basis
  - Serverless
    - shifts all backend infrastructure management tasks to the cloud provider

- types of cloud computing
  - public
    - accessible to everyone
  - private
    - accessible to a single customer
    - hosted on or off sites
    - e.g. hospitals, and financial institutions
  - hybrid
    - combination of both private and public
    - workload deployment across platforms
    - e.g. web application development and testing

### Containers 
- traditional computing issues for software devs
- characteristics
- benefits and challenges
- popular vendors

- helps on making the application portable and ability to run on multiple platforms
- encapsulates the application code, runtime, system tools, system libraries, and settings for programmers to build, ship and run apps

- traditional 
  - no isolation and allocation
    - no resource boundary defined
  - no server utilization
  - provisioning & costs
  - performance
  - portability
  - resiliency
  - scalability
  - automation

- characteristics
  - virtualizes the operating system
  - less memory space
  - one machine hosts multiple containers

- challenges
  - security is impacted if OS affected
  - migrating legacy technology is complex

- popular vendors
  - docker
    - robust and most popular
  - podman
    - more security
  - LXC
    - data-intensive apps and ops
  - vagrant
    - best for high levels of isolation on running on a physical machine 

### Docker
- process and underlying technology
- benefits
- challenges

- process
  - isolates apps from the infrastructure
  - written in Go languages
  - uses Linux kernel for functionality
  - namespaces for isolated workspace
- innovations
  - docker compose
  - docker CLI
  - prometheus
  - storage plug-ins

- benefits
  - fast deployments
  - repeatability and automation
  - consistent and isolated envs
  - supports agile and CI/CD devops practices
  - versioning for easy testing, rollbacks, and redeployments

- challenges
  - security concerns
  - requires knowledge of Linux
  - complex networking