# Cloud Computing Study Guide

## Table of Contents

- [Cloud Model Types](#cloud-model-types)
- [Cloud Service Types](#cloud-service-types)
- [Advantages & Challenges](#advantages--challenges)
- [Cloud Pricing & Agreements](#cloud-pricing--agreements)

## Cloud Model Types

### Public Cloud

Public cloud services are provided over the internet and shared among multiple organizations. Companies like Amazon, Microsoft, and Google operate these large-scale data centers that many customers use simultaneously.

This approach works well for data engineering tasks that have variable demands. For example, if you need to process large amounts of data overnight but don't need those computing resources during the day, public cloud lets you pay only for what you use. It's also good for trying out new tools or approaches without making large upfront investments in hardware.

### Private Cloud

Private cloud is dedicated to a single organization. This can be infrastructure you own and operate yourself, or dedicated infrastructure managed by a cloud provider just for your organization.

Data teams typically choose private cloud when they have strict security requirements, need to meet specific compliance standards, or have legacy systems that can't easily move to public cloud. While it gives you more control, it also requires more management and upfront investment.

### Hybrid Cloud

Hybrid cloud combines both public and private cloud approaches. This lets you keep some data and applications in a private environment while using public cloud services for other workloads.

This is useful when you want to gradually move to the cloud, when you have applications that need to stay on-premises for performance or compliance reasons, or when you want to use public cloud for handling occasional spikes in demand while maintaining your core systems privately.

## Cloud Service Types

### IaaS (Infrastructure as a Service)

IaaS provides the basic computing building blocks: virtual machines, storage, and networking. With IaaS, you manage the operating systems, applications, and data, while the cloud provider manages the physical hardware and virtualization.

Data engineers might choose IaaS when they need full control over their environment, such as when running custom data processing clusters or migrating existing applications that require specific configurations.

### PaaS (Platform as a Service)

PaaS provides a platform for developing and running applications without managing the underlying infrastructure. The cloud provider handles servers, storage, networking, and operating systems, while you focus on deploying and managing your applications.

For data engineering, PaaS offerings like data warehouses, ETL services, and stream processing platforms can significantly reduce the time spent on infrastructure management. You can concentrate on your data pipelines and transformations while the platform handles scaling and maintenance.

### SaaS (Software as a Service)

SaaS delivers complete software applications over the internet. The provider manages everything from the infrastructure to the application itself.

Data teams use SaaS for tools like business intelligence platforms, data visualization software, and collaborative analytics environments. These services let business users access data insights without needing technical infrastructure knowledge.

## Advantages & Challenges

### Advantages

**Scalability**
Cloud platforms can automatically adjust resources based on your current needs. If your data processing job requires more computing power, you can scale up quickly without buying new hardware. When the work is done, you can scale back down. This is particularly valuable for data engineering workloads that often have unpredictable or variable demands.

**Cost Management**
Instead of large upfront investments in servers and storage, cloud computing uses a pay-for-what-you-use model. This can make it easier to budget for data projects and reduces the financial risk of trying new approaches.

**Managed Services**
Cloud providers offer services that handle routine maintenance tasks like software updates, security patches, and hardware replacements. This lets data engineers focus more on building data solutions and less on infrastructure management.

**Global Infrastructure**
Cloud providers have data centers around the world, which helps with data residency requirements and can improve performance for globally distributed teams and applications.

### Challenges

**Security and Compliance**
While cloud providers implement strong security measures, data teams still need to properly configure access controls, encryption, and monitoring. Understanding what security responsibilities belong to you versus the cloud provider is essential.

**Data Transfer Costs**
Moving data out of cloud environments can incur significant costs. Data engineering architectures should consider these costs and minimize unnecessary data movement.

**Vendor Dependencies**
Using cloud-specific services can make it challenging to move to another provider later. Data teams should consider this when choosing between standard technologies and cloud-specific services.

**Cost Control**
The flexibility of cloud computing can lead to unexpected costs if not properly monitored. Implementing good cost tracking and alerting practices helps avoid surprises.

## Cloud Pricing & Agreements

### Pricing Models

**Compute Pricing**
Cloud providers offer different ways to pay for computing resources:

- **On-demand**: Pay by the hour or second with no long-term commitment. Good for unpredictable workloads.
- **Reserved instances**: Commit to 1-3 years of usage for lower prices. Works well for steady, predictable workloads.
- **Spot instances**: Use unused cloud capacity at significant discounts, but with the risk that resources might be reclaimed with little notice. Suitable for flexible batch processing jobs.

**Storage Pricing**
Storage costs vary based on how frequently you need to access your data:

- Frequently accessed data costs more to store but has low access costs
- Infrequently accessed data costs less to store but has higher access costs
- Archival storage costs the least but can take hours to retrieve data from

**Data Transfer Pricing**
Most cloud providers charge for data moving out of their networks, while data coming in is usually free. Costs also apply for data moving between different cloud regions or availability zones.

### Service Level Agreements (SLAs)

SLAs define the level of service you can expect from a cloud provider, including:

- **Uptime commitments**: The percentage of time services should be available
- **Service credits**: Compensation if the provider doesn't meet their commitments
- **Exclusions**: Situations where the SLA doesn't apply, such as scheduled maintenance

Typical cloud SLAs guarantee between 99.9% and 99.99% availability, which translates to about 9 hours to 52 minutes of potential downtime per year. Some SLA's get into Five 9's - 99.999% availability. Just 5 minutes and 15 seconds of downtime per year.

### Cost Optimization Approaches

**Matching Resources to Needs**
Regularly review your cloud usage to ensure you're using appropriately sized resources. Many organizations over-provision resources, leading to unnecessary costs.

**Automated Data Management**
Set up rules to automatically move older data to cheaper storage tiers. Data that's rarely accessed doesn't need to be on expensive, high-performance storage.

**Using Cost-effective Resources**
For workloads that can handle interruptions, consider using spot instances or similar discounted resources. This can reduce compute costs significantly for appropriate use cases.

**Planning for Steady Workloads**
For consistent, predictable workloads, reserved instances or savings plans can provide better pricing than on-demand resources.

### Managing Cloud Costs

**Resource Tagging**
Use tags to label cloud resources with information like project name, team, or purpose. This makes it easier to track costs and identify what's driving spending.

**Spending Alerts**
Set up notifications when spending approaches budget thresholds. This helps catch unexpected cost increases early.

**Regular Reviews**
Schedule periodic reviews of cloud spending to identify optimization opportunities and ensure costs align with business value.

**Architecture Considerations**
When designing data systems, consider the cost implications of different approaches. Sometimes small design changes can significantly reduce ongoing costs.
