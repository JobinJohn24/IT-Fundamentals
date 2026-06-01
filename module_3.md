# Data Centers & Cloud Computing

### Objectives:
- Data Centers
- Cloud Computing 
- Cloud Computing Services
- cloud deployment models
- specializations (AI)

## Data Centers
- traditional IT has servers and applications hosted in client specific, purpose designed IT.
- placed in racks, mounted & cabled inside DC racks.

## On-Premise DC - 100% customer controlled
- responsible for the design, cost, build, operations, optimization, upgrades, and security.
- responsible for network, storage, hardware, virtualization, OS, middleware (message broker, which is responsible for routing, caching, data translationg, and IPC), runtime (i.e. programs responsible for running python) data, app.
- CAPEX Model - Capital expenditure model, which allows the customer to pay upfront to rent or own the place.

## Cloud Computing 
- helps prevent the CAPEX Model, which is very expensive.
- everything is pre-built, ready-for-use, starting from infastructure, applications, DBs, security, and storage. (e.g. AWS, Microsoft, Google)
- OPEX Model - operational expenditure model, what you use will send a bill for usage.

## Infastructure
- DC requires orchestration and automation layer to become a Cloud. (for provisioning, updating, & monitoring services.) 
- *Console Home for AWS*
- DC + automation/orchestration = cloud

## Cloud Service Model
- as a Service (aaS) model
- Infrastructure as a Service (IaaS) - using infrastructure from a cloud provider.
- e.g. hosting a VM in AWS, you dictate the data, OS, & specs.
- Platform as a Service (PaaS) - the cusomter is responsible for data and the applications.
- Software as a Service (SaaS) - access to a end-user application through the internet.(e.g. google workspace, salesforce, slack, netflix, & microsoft 365)

## Cloud Deployment models
- ![alt text](<Screenshot 2026-05-15 at 9.52.10 AM.png>)
- public (e.g. azure, aws, GCP) vs private (hospitals, banks) cloud.
- hybrid cloud - mix of public and on-premises private cloud orchestrated to run a single task.
- more complex because the organization must use multiple platforms.
- suitable for most use cases.

#### Multi-Cloud
- The use of multi-cloud computing services in a heterogenous architecture
- benefit: Helps provide the best features for the lowest cost.

### Hybrid - Multi-Cloud
- definition: mix of hybrid and multi cloud
- challenges: deployment, automation, and orchestration.

## Cloud Providers
- best use case for beginning: use the Gartner Magic Quadrant for benchmarking and understanding which cloud provider is best used for learning.
- GCP & Azure are best for ML & AI.