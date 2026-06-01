# Introduction to DevOps, SRE, Platform Engineering, & DevSecOps

### objectives

- the IT areas
- how they relate to each other
- their importance

### Software Development Lifecycle (SDLC) overview

- any application or software that goes through the steps from idea until it's deployed.
- a dev team will collaborate into a single respository.
- the build/QA testing teams will review code, & provide feedback.
- the code will be iterated until the code is ready.

*Stages:*

1. planning
2. writing the code segments by devs.
3. building the code into the app / merging code together.
4. testing for errors or bugs.
5. providing feedback to devs to fix any spotted issues.
6. releasing the deployment
7. operation & monitoring 

1. automation of different tasks in software development process will ensure better quality & less bugs or integration issues.

*Benefits of SDLC:*
1. ensures systematic approach to software creation.
2. provides a way to measure and improve dev process.
3. allowing for accurate analysis of every step.
4. detects and fixes software issues earlier in the process
5. facilitates faster software delivery

*Old method of SDLC:*

- discrete teams for each phase (devs, testing, release, & operation teams)
- complex integrations
- lots of bugs
- slower-release process

*New method*

- collaboration between teams (build, test, release, operate, code)
- errors can be detected earlier
- fast-release models

#### workflow / SDLC Model

*Waterfall*
- a sequential methodology
- requirements -> design -> development -> testing -> deployment -> maintenance
  • fits projects with well-defined requirements
  • release every 6-12 months
  • manual testing after development
  • operations teams deploy the code

*Agile*
- iterative & flexible software development methodology incorporating a cyclic & collaborative process (every 2-4 weeks)
  • can't accommodate new requirements
  • deliver working software more frquently, collaboratively, & flexible in response to changing requirements.
  • testing is continuous but semi-manual
  •  release managers co-ordinates the dev/ops teams to deploy the code.
  • frequent releases every 2-4 weeks (sprints)
- limitations:
  • agile often ended of the code handoff to operations
  • agile didn't transfer operations.
  • ops teams still used slow, manual processes.

### DevOps

- Increased the automation 
- addressed the problem that fast, slow ops bottleneck
- code was frequently ready while ops teams were deployed monthly / quarterly.
- devs & ops worked in silos with conflicting goals.

- devops is a set of practices, tools, and cultural mindset that combines software development and IT operations 
- it's aimed to extend agile principles beyond dev
- brings automation, collaboration, and shared responsibility

*Benefits*

• faster software delivery
• improved collaboration
• reliable releases
• automated testing, deployment, and monitoring
• better scalablity & performance
• promote collabs between development, and operations.

*Key devops practices*

- CI - triggers automated builds and testing every time code is merged in a shared repo.
- CD - code changes are automatically tested and prepared for release into production.
- IaC - infrastructure is managed as code rather than manual configurations.
- automated testing - less errors and faster code problem detection
- configuration management - standardizing and auotmating system setups

*Continuous Integration / Continuous Delivery*

- development practices aimed at automating software development workflow tasks, improving software quality, & speeding up the software development cycle.

*Workflow*

- devs need to push their code to one shared repository, which trigger the automatic building and testing process 
- validation & code testing need to be added to the CI.

*Continuous Delivery*

- once the software is ready for deployment, there's a manual process
- deploying changes to staging, testing or prod environment should be AFTER the code build step.
- it's dependent on the team's plans and decisions for release time, changes needding to be released, etc.
- changes that pass all CI stages will be released to prod automatically
  - there's no human intervention, and it's fully automated.
  - risky & not commonly used.

*Common tasks requiring coding skills*

- communication & collabing with dev teams
- automation scripts
- writing scripts using SDK, creating/manging cloud resources (IaC - alternatives exist)

*Common languages & scripting tools*

- python / Go
- Bash / Powershell
- Terraform for IaC

# Site reliability engineering overview

- when it's pushed to prod, there needs a reliability, performance, and availability, capacity planning, uptime, incident management require another team.
- it's focused on realiability, performance, uptime of release and applications after DevOps.
- roles & tasks:
  1. incident response
  2. reliability metrics (Service level indicators - SLI & Service Level Objectives - SLOs, error budgets)
  3. root cause analysis
- SRE is a way to implement DevOps, especially in complex 

e.g. - Google or Netflix

- DevOps platform team:
  1. maintains kubernetes clusters, builds CI/CD workflows, supports +1,000 devs with tooling. 

- SRE team for a service (e.g. video playback)
  1. ensuring the service meets 99.99% uptime
  2. handles global traffic
  3. scales on demand
  4. performs well under pressure

### Platform Engineering Overview

- faced issues in devops such as standarization, scaling, ensuring governance.
- they feel overwhelemed with tasks such as:
  1. running IaaS
  2. running K8s clusters
  3. CI/CD 
  4. IaC
  5. Security
  6. Monitoring
- tools include: AWS, azure, google cloud, gitlab, docker, argo, python, jenkins
- Issues with scaling DevOps:
  1. multiple dev teams with multiple devops engineers use different tools or cloud providers without a standardized security or toolchain practices.
    - no consistent tech stack
    - no standardized security and weak compliance
    - EXTRA COST
    - hard to re-use
    - harder for troubleshooting

*Platform engineering*

- designing and building toolchain and workflows enabling self-service capabilities for software engineering organizations in cloud-native era.
- building a IDP (internal development platform) - a list of a tool sets required along with cloud-service tools. 
  - users will open a portal where they self-service their tool sets
  - deploy code without worrying about infrastructure
  - monitoring apps with minimal setup
  - running tests, stage environnments, or rollbacks.
  - launching new services using templates

*Use case of platform engineering*

- company wants to deploy 100 microservices to kubernetes.

*Platform engineers role:*

1. builds self-service portal for devs to self-service their tool set
   - pre-configured repository
   - working CI/CD pipeline
   - deployment target
   - built-in monitoring
2. makes developement feel easy and safe

*DevOps engineering:*

1. sets up ArgoCD
2. helm charts
3. CI/CD pipelines

*SREs:*

1. monitoring latency
2. manages on-call
3. handling reliability issues

### DevSecOps Overview

- development, security, operations
- integrating security practices & tools into every stage of the DevOps pipeline
- responsible for securing the DevSecOps

*Phases:*

1. planning - including security requirements and threat modeling in design discussions.
2. coding - using static code analysis tools to catch vulnerabilities.
3. building - scan dependencies for known CVEs using tools (e.g. Snyk, Trivy, Dependabot)
4. CI/CD - automates security tests in pipelines (e.g. secret scanning, policy checks)
5. containerization - scanning container images for vulnerabilites before pushing to registry.
6. Infra as Code (IaC) - uses tools to ensure secure infrastructure definitions. (e.g. Checkov or terraform sentinel)
7. secrets management - using tools to detect hard-coded secrets in code/repos (e.g. hashicorp vault, AWS secrets manager or sealed secrets)
8. production monitoring - monitoring for security events, misconfigurations, or drift (e.g. Falco, OSSEC, AWS GuardDuty, etc)