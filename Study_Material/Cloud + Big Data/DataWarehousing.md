# Data Storage and Architecture Primer

## Table of Contents

- [Data Storage and Architecture Primer](#data-storage-and-architecture-primer)
  - [Table of Contents](#table-of-contents)
  - [OLTP Systems](#oltp-systems)
  - [OLAP Systems](#olap-systems)
  - [Denormalization](#denormalization)
  - [Star Schema](#star-schema)
    - [Core Components](#core-components)
    - [How It Works](#how-it-works)
    - [Benefits of Star Schema](#benefits-of-star-schema)
    - [Example Implementation](#example-implementation)
    - [Best Practices](#best-practices)
  - [Data Warehouse Architecture](#data-warehouse-architecture)
    - [Core Components](#core-components-1)
    - [Common Architectures](#common-architectures)
  - [Data Warehouses vs Data Lakes](#data-warehouses-vs-data-lakes)
    - [Data Warehouse](#data-warehouse)
    - [Data Lake](#data-lake)
  - [Operational Data Store](#operational-data-store)
  - [Data Mart](#data-mart)
  - [Data Cleansing](#data-cleansing)
  - [Data Store Vendors](#data-store-vendors)
    - [Traditional Database Vendors](#traditional-database-vendors)
    - [Cloud Data Warehouse Vendors](#cloud-data-warehouse-vendors)
    - [NoSQL and Specialized Vendors](#nosql-and-specialized-vendors)
    - [Data Lake Platforms](#data-lake-platforms)

## OLTP Systems

OLTP (Online Transaction Processing) systems are designed for managing daily business transactions. These systems focus on processing a large number of small, quick transactions in real-time.

**Key Characteristics:**

- Optimized for fast writes and updates
- Maintains current state data
- Supports many concurrent users
- Ensures data integrity and consistency

**Common Examples:**

- Point-of-sale systems in retail stores
- Banking transaction systems
- Hotel reservation systems
- E-commerce order processing

**Technical Features:**

- Uses normalized database schemas
- Implements ACID properties (Atomicity, Consistency, Isolation, Durability)
- Typically handles high-volume, simple queries
- Maintains detailed, up-to-date records

For example, when you purchase something online, the OLTP system processes your order, updates inventory, and processes payment - all within seconds.

## OLAP Systems

OLAP (Online Analytical Processing) systems are designed for complex queries and data analysis. These systems are optimized for reading large volumes of data to support business intelligence and reporting.

**Key Characteristics:**

- Optimized for complex queries and aggregations
- Contains historical data
- Supports fewer concurrent users doing intensive analysis
- Focuses on read performance

**Common Examples:**

- Sales trend analysis over multiple years
- Customer behavior analysis
- Financial reporting and forecasting
- Inventory optimization analysis

**Technical Features:**

- Uses denormalized schemas (star/snowflake)
- Handles complex joins and aggregations
- Processes large data volumes
- Supports multidimensional analysis

For instance, an OLAP system might analyze five years of sales data to identify seasonal patterns and predict future demand.

## Denormalization

Denormalization is the process of combining database tables to reduce the number of joins needed for queries. This improves read performance at the cost of some data redundancy.

**When to Use Denormalization:**

- When read performance is critical
- For data warehouse and reporting databases
- When dealing with complex queries that join multiple tables
- When data updates are infrequent

**Common Denormalization Techniques:**

- **Flattened Tables**: Combining related tables into one wide table
- **Pre-joined Tables**: Storing the results of common joins
- **Summary Tables**: Pre-calculating aggregates and totals
- **Redundant Columns**: Adding frequently accessed columns to multiple tables

**Example:**
Instead of storing customer addresses in a separate table and joining every time, you might include the most common address fields directly in the orders table for faster order reporting.

## Star Schema

A star schema is a database organizational structure optimized for use in data warehouses and dimensional modeling. It gets its name from the visual appearance of the schema diagram, which resembles a star with one central table and multiple surrounding tables.

### Core Components

**Fact Tables**

- Contain the quantitative metrics and measurements of a business process
- Typically store numerical values that can be aggregated (sales amounts, quantities, counts)
- Include foreign keys that link to dimension tables
- Tend to be very large, containing millions or billions of rows

**Examples of Fact Tables:**

- Sales transactions with amount, quantity, and profit
- Website clicks with timestamp and session duration
- Inventory movements with quantity and cost

**Dimension Tables**

- Contain descriptive attributes that provide context to the facts
- Store textual or descriptive information
- Typically smaller than fact tables
- Act as the "who, what, when, where, why" of the business process

**Examples of Dimension Tables:**

- **Time Dimension**: Date, month, quarter, year, holiday flags
- **Product Dimension**: Product name, category, brand, supplier
- **Customer Dimension**: Customer name, demographics, region
- **Store Dimension**: Store location, size, manager, region

### How It Works

In a retail sales example:

- The **fact_sales** table contains transaction details: sale amount, quantity, cost
- The **dim_date** table describes when the sale occurred
- The **dim_product** table describes what was sold
- The **dim_customer** table describes who made the purchase
- The **dim_store** table describes where the sale occurred

### Benefits of Star Schema

**Query Performance**

- Simple structure with minimal joins needed for most queries
- Optimized for aggregate operations and analytical queries
- Fast response times for business intelligence tools

**Ease of Use**

- Business users can easily understand the structure
- Intuitive navigation for ad-hoc querying
- Simplified report development

**Maintenance**

- Clear separation between metrics (facts) and descriptors (dimensions)
- Easy to add new dimensions without affecting existing queries
- Straightforward ETL processes

### Example Implementation

A typical sales star schema might look like:

```
Fact_Sales
------------
sale_id
date_key (links to dim_date)
product_key (links to dim_product)
customer_key (links to dim_customer)
store_key (links to dim_store)
sales_amount
quantity_sold
profit_amount

Dim_Date
---------
date_key
full_date
day_of_week
month
quarter
year
is_holiday

Dim_Product
-----------
product_key
product_name
category
subcategory
brand
supplier

Dim_Customer
------------
customer_key
customer_name
city
state
country
segment

Dim_Store
---------
store_key
store_name
city
state
country
region
manager
```

### Best Practices

**Surrogate Keys**

- Use system-generated keys rather than business keys in dimension tables
- Provides stability when business keys change over time
- Improves join performance

**Consistent Dimensions**

- Maintain the same dimensions across different fact tables
- Enables cross-business process analysis
- Supports conformed dimensions in larger data warehouses

**Slowly Changing Dimensions**

- Implement Type 1: Overwrite history when attributes change
- Implement Type 2: Preserve history by creating new dimension records
- Implement Type 3: Track limited history with previous value columns

## Data Warehouse Architecture

Data warehouse architecture typically follows a layered approach to transform raw data into usable business intelligence.

### Core Components

**Source Systems**

- Operational databases (OLTP systems)
- External data sources
- Application logs and files

**ETL Process**

- **Extract**: Collect data from source systems
- **Transform**: Clean, validate, and reformat data
- **Load**: Move processed data into the warehouse

**Storage Layers**

- **Staging Area**: Temporary storage for raw data
- **Data Warehouse**: Central repository of integrated data
- **Data Marts**: Department-specific subsets of data

**Presentation Layer**

- Business intelligence tools
- Reporting and dashboard systems
- Data visualization platforms

### Common Architectures

**Kimball Approach**

- Uses dimensional modeling (star schemas)
- Focuses on business processes
- Bottom-up implementation starting with data marts

**Inmon Approach**

- Uses normalized data models
- Top-down implementation with enterprise data warehouse
- Emphasizes data integration and consistency

## Data Warehouses vs Data Lakes

### Data Warehouse

- Stores processed, structured data
- Uses predefined schemas (schema-on-write)
- Optimized for SQL queries and reporting
- Contains curated business-ready data
- Typically more expensive storage
- Used by business analysts and executives

### Data Lake

- Stores raw data in native format
- Uses flexible schemas (schema-on-read)
- Supports various data types and processing methods
- Contains data at all stages of refinement
- Cost-effective storage for large volumes
- Used by data scientists and engineers

**Practical Example:**
A retail company might use a data lake to store raw clickstream data, social media feeds, and sensor data, while using a data warehouse for sales reports and inventory analysis.

## Operational Data Store

An Operational Data Store (ODS) is a database designed to integrate data from multiple operational systems for near-real-time reporting and operational reporting.

**Key Characteristics:**

- Contains current or near-real-time data
- Integrated view across multiple source systems
- Supports operational reporting and decision-making
- Typically updated more frequently than a data warehouse

**Common Uses:**

- Customer service systems needing integrated customer views
- Daily operational reporting
- Real-time dashboards for operations teams
- Data integration before warehouse processing

**Example:**
A bank might use an ODS to combine data from checking accounts, savings accounts, and loan systems to give customer service representatives a complete view of a customer's relationship.

## Data Mart

A data mart is a subset of a data warehouse focused on a specific business department or function. Data marts are designed to make relevant data easily accessible to particular user groups.

**Types of Data Marts:**

- **Dependent**: Built from an existing data warehouse
- **Independent**: Built directly from source systems
- **Hybrid**: Combines data from warehouse and other sources

**Common Examples:**

- **Sales Data Mart**: Contains customer, product, and sales data for the sales team
- **Marketing Data Mart**: Stores campaign data, customer segments, and response metrics
- **Finance Data Mart**: Includes financial transactions, budgets, and accounting data

**Benefits:**

- Improved performance for department-specific queries
- Easier access for business users
- Reduced complexity compared to full warehouse
- Faster implementation for specific use cases

## Data Cleansing

Data cleansing (or data cleaning) is the process of detecting and correcting inaccurate records from a dataset. This ensures data quality and reliability for analysis.

**Common Data Quality Issues:**

- Missing values and incomplete records
- Inconsistent formatting (dates, phone numbers, addresses)
- Duplicate records
- Invalid or out-of-range values
- Spelling errors and typos

**Cleansing Techniques:**

- **Standardization**: Converting data to consistent formats
- **Validation**: Checking data against business rules
- **Deduplication**: Identifying and removing duplicate records
- **Enrichment**: Adding missing information from external sources
- **Parsing**: Breaking down fields into components

**Example:**
Cleaning customer data might involve standardizing address formats, removing duplicate customer records, validating email addresses, and correcting misspelled names.

## Data Store Vendors

### Traditional Database Vendors

- **Oracle**: Enterprise relational databases with strong transaction support
- **Microsoft SQL Server**: Windows-based database system with business intelligence features
- **IBM Db2**: Enterprise database system with strong legacy presence
- **MySQL**: Open-source relational database popular for web applications
- **PostgreSQL**: Advanced open-source database with extensive features

### Cloud Data Warehouse Vendors

- **Amazon Redshift**: Cloud data warehouse with strong AWS integration
- **Google BigQuery**: Serverless data warehouse with machine learning capabilities
- **Snowflake**: Cloud-native data platform with separate compute and storage
- **Azure Synapse Analytics**: Microsoft's analytics service with cloud data warehouse
- **Databricks**: Unified analytics platform with data warehousing capabilities

### NoSQL and Specialized Vendors

- **MongoDB**: Document database for flexible, JSON-like data
- **Cassandra**: Distributed database for handling large amounts of data across many servers
- **Redis**: In-memory data store for caching and real-time applications
- **Elasticsearch**: Search and analytics engine for unstructured data

### Data Lake Platforms

- **AWS S3 + Lake Formation**: Object storage with data lake management
- **Azure Data Lake Storage**: Cloud storage optimized for analytics
- **Google Cloud Storage**: Unified object storage for data lakes
- **Cloudera**: On-premises and cloud data platform for big data

**Selection Considerations:**

- Data volume and velocity requirements
- Query patterns and performance needs
- Integration with existing systems
- Team skills and expertise
- Total cost of ownership
- Compliance and security requirements
