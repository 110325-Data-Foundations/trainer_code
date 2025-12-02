# BigQuery Study Guide

## Table of Contents

- [What is BigQuery?](#what-is-bigquery)
- [Key Concepts](#key-concepts)
- [BigQuery Connectors](#bigquery-connectors)
- [Working with Datasets](#working-with-datasets)
- [Working with Tables](#working-with-tables)
- [Basic Querying](#basic-querying)
- [Connecting to BigQuery](#connecting-to-bigquery)

## What is BigQuery?

BigQuery is Google Cloud's data warehouse service. It's designed for analyzing large amounts of data quickly. Unlike traditional databases, you don't need to manage servers or infrastructure - Google handles all that for you.

**The Basics:**

- Fully managed service (no servers to set up)
- Automatically scales to handle your data size
- You pay for the data you store and the queries you run
- Built for analytical queries, not transaction processing

**Main Uses:**

- Business reporting and dashboards
- Analyzing logs or user behavior data
- Data exploration and ad-hoc analysis
- Processing large datasets for insights

## Key Concepts

### Projects

Every BigQuery resource belongs to a Google Cloud Project. The project is the top-level container for billing, permissions, and resource management.

### Datasets

Datasets are containers for tables and views. Think of them like folders that organize related tables together. Each dataset has settings that apply to all tables inside it, like where the data is stored geographically.

### Tables

Tables hold your actual data. They have a defined structure (columns and data types) and can store massive amounts of information.

### Jobs

When you run a query, load data, or copy tables, BigQuery creates a job. Jobs can be monitored and show information like how much data was processed.

### SQL Dialect

BigQuery uses standard SQL (similar to SQL:2011) with some Google-specific extensions. Most SQL you already know will work, but there are some differences in functions and syntax.

## BigQuery Connectors

Connectors are tools that let you connect BigQuery to other systems and services. They help move data in and out of BigQuery.

### Database Connectors

Tools to connect traditional databases to BigQuery:

- **Cloud SQL Federation**: Query MySQL or PostgreSQL databases directly from BigQuery
- **Database migration tools**: Move data from on-premises databases to BigQuery
- **Third-party ETL tools**: Many data integration tools have BigQuery connectors

### Business Intelligence Connectors

Tools that connect reporting tools to BigQuery:

- **Looker**: Google's BI tool with native BigQuery integration
- **Tableau**: Direct connector available
- **Power BI**: Microsoft's connector for BigQuery
- **Data Studio**: Google's free visualization tool

### Command Line and API

Programmatic ways to work with BigQuery:

- **bq command-line tool**: Run queries and manage resources from terminal
- **REST API**: Programmatic access for custom applications
- **Client libraries**: For Python, Java, Node.js, Go, and other languages

## Working with Datasets

### Creating a Dataset

Datasets are created within a project. The main decisions you make when creating a dataset are:

1. **Location**: Where your data will be stored geographically (like "US" or "EU")
2. **Default expiration**: How long tables should be kept if you don't specify otherwise
3. **Description**: Notes about what the dataset contains

### Dataset Organization

Common approaches include:

- Having separate datasets for raw data, processed data, and reporting data
- Grouping tables by department (sales, marketing, finance)
- Separating production data from test data

## Working with Tables

### Table Types

**Regular Tables**

- Store data inside BigQuery
- Optimized for fast querying
- Can be loaded from files or created from query results

**External Tables**

- Point to data stored outside BigQuery (like in Google Cloud Storage)
- The data stays where it is, but you can query it like a regular table
- Good for data that changes frequently

**Views**

- Saved queries that act like tables
- Don't store data themselves, but show results from other tables
- Useful for simplifying complex queries for end users

### Creating Tables

**From the Web Interface**
BigQuery's web console has tools to create tables by uploading files or defining them manually.

**Using SQL**
You can create tables with CREATE TABLE statements, similar to other databases:

```sql
CREATE TABLE dataset.table_name (
  column1 INT64,
  column2 STRING,
  column3 DATE
)
```

**Loading Data**
You can load data from:

- CSV, JSON, or Avro files
- Other BigQuery tables
- Google Sheets or Cloud Storage

### Table Structure

**Schema**
The schema defines your table's columns, their data types, and whether they're required or optional.

**Partitioning**
You can split large tables by time or other values to make queries faster and cheaper. For example, a sales table might be partitioned by date so queries for a specific month only scan that month's data.

**Clustering**
Data can be organized within partitions based on column values. This further improves query performance for common filters.

## Basic Querying

### Query Structure

BigQuery uses standard SQL syntax:

```sql
SELECT column1, column2
FROM dataset.table_name
WHERE condition
GROUP BY column1
ORDER BY column2
LIMIT 100
```

### Key Differences from Traditional SQL

**Table References**
Tables are referenced as `project.dataset.table` or just `dataset.table` if you're in the same project.

**Cost Model**
You're charged based on the amount of data processed by your query, not by how long it takes. This means:

- Selecting specific columns is cheaper than SELECT *
- Filtering early in your query reduces costs
- Partitioning helps limit the data scanned

**Performance Features**

- Queries run on distributed infrastructure automatically
- Results are cached, so identical queries run faster
- You don't need to create indexes - BigQuery optimizes queries automatically

### Common Operations

**Filtering Data**
Use WHERE clauses to filter rows, similar to other SQL databases.

**Joining Tables**
BigQuery supports standard JOIN operations (INNER, LEFT, RIGHT, FULL).

**Aggregations**
Common functions like SUM, COUNT, AVG work as expected, with optimizations for large datasets.

**Working with Dates and Times**
BigQuery has strong support for date and time functions, which is important for analytical queries.

## Connecting to BigQuery

### Web Interface

The Google Cloud Console provides a web-based query editor and data explorer. This is good for learning and ad-hoc queries.

### Command Line Tool

The `bq` command-line tool lets you run queries and manage resources from your terminal.

### Programming Languages

Client libraries are available for:

- Python
- Java
- Node.js
- Go

These let you run queries and manage BigQuery from your applications.

### Business Intelligence Tools

BigQuery connects to most popular BI tools like:

- Looker (Google's BI tool, integrates closely)
- Tableau
- Power BI
- Data Studio

### APIs

BigQuery provides REST APIs for programmatic access, which the client libraries use internally.

---

## Key Takeaways

1. **Serverless**: No infrastructure to manage, Google handles everything
2. **Scalable**: Automatically handles datasets of any size
3. **Pay for Use**: Costs based on storage and query processing, not reserved capacity
4. **Standard SQL**: Uses familiar SQL with some useful extensions
5. **Multiple Connect ors**: Various ways to get data in and out, from simple file uploads to real-time streaming
6. **Fast Analytics**: Built for analytical queries on large datasets
7.
