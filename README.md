# Data Engineering Portfolio

Welcome to my Data Engineering Portfolio! Here, I showcase various projects that highlight my passion for using data and technology to solve real-world problems. Each project represents my dedication to learning and innovation in data engineering.

In this portfolio, you'll find projects covering different technologies and areas, with detailed guides and step-by-step instructions. Whether it's integrating APIs, building cloud-based solutions, or automating data workflows, these projects demonstrate my skills and curiosity in turning data into valuable insights.

I mainly use popular cloud providers like AWS, Google Cloud Platform, and Azure, which offer free-tier accounts. This means you can replicate my projects and explore the technologies I've used at no cost.

Feel free to explore the projects, check out the technologies I've used, and see how I've tackled various challenges in data engineering. With each project, I continue to grow and expand my capabilities in this exciting field.

---

## Index
- [Projects Overview](#projects-overview)
  - [AWS + Terraform + GitHub Actions Project](#aws--terraform--github-actions-project)
  - [Weather Data and Text Message Notification](#weather-data-and-text-message-notification)
  - [Extract Daily Statistics YouTube](#extract-daily-statistics-youtube)
- [Contributions](#contributions)
- [License](#license)
- [Contact](#contact)

## Projects Overview

### [AWS + Terraform + GitHub Actions Project](https://github.com/rublaman/data-engineering-portfolio)
A comprehensive Infrastructure-as-Code (IaC) solution that automates AWS infrastructure deployment using Terraform and GitHub Actions. This project implements a multi-environment deployment strategy (dev, stg, pro) with robust security practices, designed to help teams efficiently manage cloud infrastructure following industry best practices.

#### Main Purpose to Learn
- Infrastructure as Code principles and implementation
- CI/CD automation for infrastructure deployment
- Multi-environment strategy with secure state management
- DevOps security best practices and access control

#### Technologies Used
- Terraform
- AWS
  - S3
  - IAM
- GitHub Actions
- Bash Scripting
- Git
- Mermaid Diagrams

#### Key Highlights
- **S3 Data Lake Architecture**
  - Design and deploy a structured data lake with four specialized S3 buckets per environment.
  - Implement proper data flow patterns from landing to raw, curated, and ready zones.
  - Configure private bucket access with versioning for secure data tracking.
- **Infrastructure as Code with Terraform**
  - Leverage Terraform 1.11 for defining and provisioning modular AWS infrastructure.
  - Create reusable modules for consistent infrastructure deployment across environments.
  - Maintain separate state management for each environment with remote state in S3.
- **CI/CD Pipeline with GitHub Actions**
  - Implement environment-specific workflows triggered by branch-based deployments.
  - Enforce code reviews and approval processes before infrastructure changes.
  - Automate planning, validation, and deployment of infrastructure changes.
- **Security and Access Control**
  - Apply the principle of least privilege with environment-specific IAM credentials.
  - Implement secure credential management through GitHub Secrets.
  - Establish proper branch protection rules to prevent unauthorized changes.

### [Weather Data and Text Message Notification](Text-message-notification-weather/guide.md)
This project obtains weather data and sends them by text message. The project seamlessly integrates Weather APIs, Twilio's SMS service, and AWS EC2 instances, all while adhering to cost-effectiveness within the AWS Free Tier.

#### Main Purpose to Learn
- API integration and consumption with third-party services
- Cloud computing fundamentals with AWS EC2
- Automation using scheduled tasks
- SMS notification systems implementation

#### Technologies Used
- Python
- Weather API
- Twilio API
- AWS
  - EC2
- Cron Jobs

#### Key Highlights
- **Weather API Integration:** Harness the power of a Weather API to obtain up-to-the-minute weather data.
- **Twilio SMS Service:** Explore the integration of Twilio for seamless delivery of concise and informative weather updates directly to mobile devices.
- **AWS EC2 Instances:** Dive into the reliability and scalability of AWS EC2 instances, ensuring periodic execution and cost-effective operation within the AWS Free Tier.

### [Extract Daily Statistics YouTube](Extract-daily-statistics-youtube/guide.md)
Automating YouTube channel metric extraction, this project integrates Google Cloud for YouTube API access and AWS Lambda for serverless processing with S3 storage. Scheduled updates via AWS EventBridge ensure timely data refresh. AWS Athena and Glue facilitate thorough analysis, offering SQL-like queries and comprehensive table creation for insightful metrics exploration.

#### Main Purpose to Learn
- Serverless computing architecture with AWS Lambda
- Data pipeline development across multiple cloud services
- Scheduled automation with event-driven processing
- Data lake implementation and analytics with AWS services

#### Technologies Used
- Python
- Google Cloud Platform
  - YouTube API
- AWS
  - Lambda
  - S3
  - SDK for Pandas
  - EventBridge
  - Athena
  - Glue

#### Key Highlights
- **Google Cloud Setup**
  - Enable YouTube API v3 service.
  - Create a secure API key and control access by IP for enhanced security.
- **YouTube API Analysis**
  - Utilize the YouTube API for daily channel statistics analysis.
- **AWS Lambda Function**
  - Implement a serverless solution with AWS Lambda.
  - Leverage S3 for data storage and AWS SDK Pandas Layer for efficient data processing.
- **AWS EventBridge Integration**
  - Schedule daily execution with EventBridge for reliable and automated updates.
- **AWS Athena and AWS Glue**
  - Set up Athena for SQL-like queries and Glue for crawling and table creation, enabling comprehensive data analysis.

---

*Gradually I will be adding more projects with different challenges and technologies.*

## Contributions
Any contributions you make are greatly appreciated.
- Fork the Project
- Create your Feature Branch (`git checkout -b feature/new-feature`)
- Commit your Changes (`git commit -m 'Add some new-feature'`)
- Push to the Branch (`git push origin feature/new-feature`)
- Open a Pull Request

## License
This project is licensed under the GPL-3.0 License.

## Contact
Please feel free to contact me if you have any questions.
[LinkedIn](https://www.linkedin.com/in/rublaman)
