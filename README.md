# Data Engineering Portfolio

Welcome to my Data Engineering Portfolio! Within this repository, I'll showcase various data engineering projects where I employ a range of tools offered by AWS, Azure, and GCP for data extraction, transformation, and loading. Additionally, I'll demonstrate the consumption of API services (Weather, YouTube) and the utilization of containerization tools like Docker, along with data warehouses such as Snowflake."

---

## Projects Overview

### [Weather Data and Text Message Notification](Weather_forescast_text_message_notification/guide.md)

This project obtains weather data and sends them by text message. The project seamlessly integrates Weather APIs, Twilio's SMS service, and AWS EC2 instances, all while adhering to cost-effectiveness within the AWS Free Tier.

#### Key Highlights

- **Weather API Integration:** Harness the power of a Weather API to obtain up-to-the-minute weather data.
- **Twilio SMS Service:** Explore the integration of Twilio for seamless delivery of concise and informative weather updates directly to mobile devices.
- **AWS EC2 Instances:** Dive into the reliability and scalability of AWS EC2 instances, ensuring periodic execution and cost-effective operation within the AWS Free Tier.

### [Extract Daily Statistics YouTube](Extract_daily_statistics_youtube/guide.md)

Automating YouTube channel metric extraction, this project integrates Google Cloud for YouTube API access and AWS Lambda for serverless processing with S3 storage. Scheduled updates via AWS EventBridge ensure timely data refresh. AWS Athena and Glue facilitate thorough analysis, offering SQL-like queries and comprehensive table creation for insightful metrics exploration.

#### Key Highlights

- **Google Cloud Setup**
  - Enable YouTube API v3 service.
  - Create a secure API key and control access by IP for enhanced security.

- **YouTube API Analysis**
  - Utilize the YouTube API for daily channel statistics analysis.

- **AWS Lambda Function**
  - Implement a serverless solution with AWS Lambda.
  - Leverage S3 for data storage and AWS SDK Pandas Layer for efficient data processing.

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
