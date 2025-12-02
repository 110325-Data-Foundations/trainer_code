# ETL, ELT, and Data Modeling Study Guide

## Table of Contents

- [ETL and ELT Overview](#etl-and-elt-overview)
- [Data Modeling Fundamentals](#data-modeling-fundamentals)
- [Dimensional Modeling](#dimensional-modeling)
- [Slowly Changing Dimensions](#slowly-changing-dimensions)
- [Building Data Pipelines](#building-data-pipelines)

## ETL and ELT Overview

### ETL: Extract, Transform, Load

ETL is the traditional approach to data integration. Data is processed in three distinct stages:

**Extract**

- Data is pulled from source systems (databases, applications, files)
- Sources can include CRM systems, ERP systems, web APIs, log files
- Extraction can be done in batches (scheduled) or via change data capture

**Transform**

- Data is cleaned, validated, and reformatted
- Business rules are applied (calculations, aggregations, joins)
- Data quality checks are performed
- Data is structured for the target system

**Load**

- Transformed data is loaded into the target system (usually a data warehouse)
- Loading can replace existing data or append new records
- Indexes and optimizations are applied after loading

**When to Use ETL:**

- When target systems have limited processing power
- When data needs significant cleaning before storage
- When working with traditional data warehouses that prefer structured data
- When compliance requires data to be transformed before storage

**Example:** A retail company extracts daily sales data from their point-of-sale system, transforms it to match their data warehouse schema, and loads it into their on-premises data warehouse overnight.

### ELT: Extract, Load, Transform

ELT is a modern approach where data is loaded first, then transformed in the target system:

**Extract**

- Similar to ETL, data is pulled from source systems
- Often includes raw, unprocessed data

**Load**

- Raw data is loaded directly into the target system
- Target is usually a cloud data warehouse or data lake
- Minimal processing during load

**Transform**

- Transformations happen within the target system
- Uses the processing power of modern cloud platforms
- Transformations are often SQL-based
- Can be done incrementally or in batches

**When to Use ELT:**

- When using cloud data platforms with strong processing capabilities
- When you want to preserve raw data for future analysis
- When transformation logic needs to be flexible and change frequently
- When dealing with large volumes of unstructured or semi-structured data

**Example:** A streaming service loads raw user viewing data into a cloud data lake, then uses SQL transformations in their data warehouse to create aggregated viewing reports.

### ETL vs ELT Comparison

| Aspect | ETL | ELT |
|--------|-----|-----|
| **Processing Location** | Separate transformation server | Within the target data platform |
| **Data Storage** | Stores cleaned, transformed data | Stores raw data and transformed views |
| **Flexibility** | Less flexible - changes require pipeline updates | More flexible - transformations can be adjusted |
| **Infrastructure** | Requires separate processing engine | Leverages target system's compute |
| **Best For** | Traditional data warehouses, strict compliance | Cloud data platforms, exploratory analysis |

## Data Modeling Fundamentals

### Three Levels of Data Modeling

**Conceptual Model**

- High-level view of business entities and relationships
- Focuses on business concepts, not implementation details
- Created with business stakeholders
- Uses simple diagrams showing entities and relationships
- Example: "Customers place Orders" and "Orders contain Products"

**Logical Model**

- Detailed view of data structures and relationships
- Defines entities, attributes, keys, and relationships
- Independent of any specific database technology
- Normalized to reduce redundancy
- Example: Customer table with CustomerID, Name, Email; Order table with OrderID, CustomerID, OrderDate

**Physical Model**

- Implementation-specific design
- Includes database-specific details (data types, indexes, partitions)
- Optimized for performance and storage
- Considers hardware and software constraints
- Example: SQL Server tables with specific data types and indexes

### Why Three Levels?

1. **Conceptual**: Business communication and requirements gathering
2. **Logical**: Technical design and data structure planning
3. **Physical**: Database implementation and performance optimization

## Dimensional Modeling

### What is Dimensional Modeling?

Dimensional modeling is a design technique for data warehouses that organizes data into facts and dimensions. It's optimized for query performance and business user understanding.

### Star Schema

The star schema is the simplest dimensional model:

**Structure:**

- One central fact table containing measurements
- Multiple dimension tables surrounding it (like a star)
- Fact table connects to dimensions via foreign keys
- Dimension tables are denormalized (contain redundant data for performance)

**Components:**

- **Fact Tables**: Store quantitative data (sales amounts, quantities, counts)
- **Dimension Tables**: Store descriptive attributes (product details, customer information, time periods)

**Example:**

```
Fact_Sales
  ├── Links to Dim_Date (when)
  ├── Links to Dim_Product (what)
  ├── Links to Dim_Customer (who)
  ├── Links to Dim_Store (where)
  └── Contains: sales_amount, quantity, profit
```

**Advantages:**

- Simple to understand for business users
- Fast query performance with minimal joins
- Easy to add new dimensions

**Disadvantages:**

- Data redundancy in denormalized dimensions
- Can lead to large dimension tables

### Snowflake Schema

The snowflake schema is a variation of the star schema:

**Structure:**

- Dimension tables are normalized into multiple related tables
- Creates a snowflake-like pattern
- Reduces data redundancy

**Example:**

```
Dim_Product
  └── Links to Dim_Product_Category
        └── Links to Dim_Product_Department
```

**Advantages:**

- Reduces data redundancy
- Saves storage space
- Maintains referential integrity

**Disadvantages:**

- More complex for users to understand
- Slower query performance due to more joins
- More complex ETL processes

### Star vs Snowflake

| Consideration | Star Schema | Snowflake Schema |
|---------------|-------------|------------------|
| **Performance** | Faster queries | Slower due to more joins |
| **Storage** | More redundant data | Less storage needed |
| **Complexity** | Simpler for users | More complex relationships |
| **ETL Complexity** | Simpler to build | More complex transformations |
| **Best For** | Business intelligence, user queries | Large dimensions with many attributes |

## Slowly Changing Dimensions

### What are Slowly Changing Dimensions?

Slowly Changing Dimensions (SCDs) are dimension tables where attributes change slowly over time. The challenge is tracking these changes to maintain historical accuracy.

**Example:** A customer changes their address. Do you overwrite the old address, keep both, or track the change somehow?

### SCD Types

**Type 1: Overwrite**

- Old data is overwritten with new data
- No history is preserved
- Simple to implement

**When to use:** When historical accuracy isn't important (typo corrections, temporary changes)

**Example:** A customer's phone number changes - you just update the record.

**Type 2: Add New Row**

- New row is added for each change
- History is preserved by keeping old records
- Includes effective date columns

**When to use:** When tracking history is important (customer address changes, product price changes)

**Example:** An employee changes departments - you add a new record with the new department and effective date.

**Type 3: Add New Column**

- New columns are added to track changes
- Limited history (usually just previous value)
- More complex than Type 1, less than Type 2

**When to use:** When you need limited history tracking (last promotion date, previous status)

**Example:** A product's price changes - you store current price and previous price in separate columns.

**Other Types:**

- **Type 0**: Never change (attributes are fixed)
- **Type 4**: Mini-dimension (separate table for frequently changing attributes)
- **Type 6**: Hybrid (combines Type 1, 2, and 3)

### Choosing SCD Types

| SCD Type | History Tracking | Implementation Complexity | Storage Impact |
|----------|-----------------|--------------------------|----------------|
| **Type 1** | None | Simple | Minimal |
| **Type 2** | Complete | Moderate | Significant |
| **Type 3** | Limited | Moderate | Minimal |

## Building Data Pipelines

### ETL/ELT Process Design

**Key Considerations:**

1. **Data Volume**: How much data needs to be processed?
2. **Frequency**: How often does data need to be refreshed?
3. **Latency**: How current does the data need to be?
4. **Transformation Complexity**: How much processing is needed?
5. **Error Handling**: How should failures be managed?

### Common Pipeline Patterns

**Batch Processing**

- Process data in scheduled batches
- Good for large volumes of data
- Typically runs overnight or at regular intervals
- Example: Daily sales reports

**Incremental Processing**

- Only process new or changed data
- Reduces processing time and resource usage
- Requires tracking of changes
- Example: Hourly order updates

**Stream Processing**

- Process data in real-time as it arrives
- Low latency, continuous processing
- More complex to implement
- Example: Real-time fraud detection

### Pipeline Components

**Source Connectors**

- Extract data from various sources
- Handle different data formats and protocols
- Manage connection pooling and error recovery

**Transformation Logic**

- Clean and validate data
- Apply business rules
- Aggregate and join data
- Handle SCD logic

**Loading Mechanisms**

- Bulk loading for efficiency
- Upsert operations for updates
- Partition management for large tables
- Index maintenance

**Monitoring and Logging**

- Track pipeline execution
- Log errors and warnings
- Monitor data quality
- Alert on failures or anomalies

### Best Practices

**Idempotency**

- Design pipelines to produce the same result if run multiple times
- Important for error recovery and retry logic

**Testing**

- Test with sample data
- Validate transformations produce expected results
- Test error conditions and recovery

**Documentation**

- Document data sources and transformations
- Maintain data lineage information
- Document business rules applied

**Performance Optimization**

- Process data in parallel when possible
- Use appropriate batch sizes
- Optimize transformation logic
- Monitor and tune regularly

---

## Key Takeaways

1. **ETL vs ELT**: Choose based on your infrastructure and requirements - ETL for traditional systems, ELT for modern cloud platforms
2. **Modeling Levels**: Conceptual for business understanding, logical for design, physical for implementation
3. **Dimensional Modeling**: Star schema for simplicity and performance, snowflake for normalization
4. **SCDs**: Type 1 for simple updates, Type 2 for full history, Type 3 for limited history
5. **Pipeline Design**: Consider volume, frequency, latency, and complexity when building data pipelines
