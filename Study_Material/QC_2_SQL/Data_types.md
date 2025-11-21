# PostgreSQL Data Types - Comprehensive Guide

## Introduction to Data Types

### What are Data Types?

Data types define the kind of data that can be stored in a column. They determine:

- What values you can store in a column
- How much storage space the data uses
- What operations you can perform on the data
- How the data is sorted and compared

**Why Data Types Matter:**

- **Data Integrity**: Prevent invalid data from being stored
- **Storage Efficiency**: Use appropriate storage for different data kinds
- **Performance**: Enable efficient queries and indexing
- **Functionality**: Determine available operations and functions

## Numeric Data Types

### Integer Types

Integer types store whole numbers without decimal places.

| Type | Storage | Range | Description |
|------|---------|-------|-------------|
| `SMALLINT` | 2 bytes | -32,768 to 32,767 | Small-range integer |
| `INTEGER` | 4 bytes | -2,147,483,648 to 2,147,483,647 | Typical choice for integers |
| `BIGINT` | 8 bytes | -9.2×10¹⁸ to 9.2×10¹⁸ | Large-range integer |
| `SERIAL` | 4 bytes | 1 to 2,147,483,647 | Auto-incrementing integer |
| `BIGSERIAL` | 8 bytes | 1 to 9.2×10¹⁸ | Auto-incrementing big integer |

**Examples and Usage:**

```sql
-- Creating tables with integer types
CREATE TABLE examples (
    small_id SMALLINT,           -- For small numbers like age, quantity
    normal_id INTEGER,           -- Most common choice for IDs
    big_id BIGINT,               -- For very large numbers
    auto_id SERIAL PRIMARY KEY,  -- Auto-incrementing primary key
    big_auto_id BIGSERIAL        -- Large auto-incrementing
);

-- Inserting integer values
INSERT INTO examples (small_id, normal_id, big_id) 
VALUES (100, 50000, 123456789012345);

-- SERIAL automatically generates values
INSERT INTO examples (small_id) VALUES (10);  -- auto_id gets 1
INSERT INTO examples (small_id) VALUES (20);  -- auto_id gets 2
```

### Decimal and Floating-Point Types

These types store numbers with fractional components.

| Type | Storage | Range | Precision | Use Case |
|------|---------|-------|-----------|----------|
| `DECIMAL(p,s)` | variable | up to 131072 digits | exact | Money, precise calculations |
| `NUMERIC(p,s)` | variable | up to 131072 digits | exact | Same as DECIMAL |
| `REAL` | 4 bytes | 6 decimal digits | approximate | Scientific data |
| `DOUBLE PRECISION` | 8 bytes | 15 decimal digits | approximate | High-precision scientific |

**Understanding Precision and Scale:**

- **Precision (p)**: Total number of digits
- **Scale (s)**: Number of digits after decimal point

**Examples and Usage:**

```sql
-- Creating tables with decimal types
CREATE TABLE financial_data (
    price DECIMAL(10,2),        -- Prices: 99999999.99
    tax_rate DECIMAL(5,4),      -- Tax rates: 0.1234 (12.34%)
    measurement REAL,           -- Approximate measurements
    scientific DOUBLE PRECISION -- High-precision scientific data
);

-- Inserting decimal values
INSERT INTO financial_data (price, tax_rate, measurement, scientific) 
VALUES (199.99, 0.0825, 123.456, 12345.678901234);

-- Common patterns:
-- DECIMAL(10,2)  -- Currency: 99999999.99
-- DECIMAL(5,2)   -- Percentages: 999.99
-- DECIMAL(7,4)   -- Exchange rates: 999.9999
```

## Character Data Types

### String Types

These types store text data.

| Type | Description | Storage | Trailing Spaces |
|------|-------------|---------|-----------------|
| `VARCHAR(n)` | Variable-length with limit | Actual length + 1 byte | Not stored |
| `CHAR(n)` | Fixed-length, padded | n bytes | Padded with spaces |
| `TEXT` | Variable-length, unlimited | Actual length + 1 byte | Not stored |

**Examples and Usage:**

```sql
-- Creating tables with character types
CREATE TABLE user_data (
    username VARCHAR(50),       -- Usernames, emails, names
    status CHAR(1),             -- Single character flags: 'A','I','P'
    description TEXT,           -- Long text: descriptions, comments
    code CHAR(5),               -- Fixed-length codes: 'USD','EUR'
    email VARCHAR(255)          -- Email addresses
);

-- Inserting string values
INSERT INTO user_data (username, status, description, code, email) 
VALUES (
    'john_doe',                 -- VARCHAR: stores exactly what you give
    'A',                        -- CHAR: always 1 character
    'This is a long description that can be very lengthy...',  -- TEXT: unlimited
    'EN',                       -- CHAR(5): stores 'EN   ' (padded with spaces)
    'john@example.com'          -- VARCHAR: stores exactly
);

-- Important behaviors:
-- CHAR(n) always uses n bytes of storage
-- VARCHAR(n) uses only what's needed + overhead
-- TEXT is the same as VARCHAR without length limit
```

**When to Use Each Type:**

- **`VARCHAR(n)`**: When you need to limit length (usernames, emails, addresses)
- **`CHAR(n)`**: When length is always the same (country codes, status flags)
- **`TEXT`**: When length varies greatly (descriptions, comments, content)

## Date and Time Data Types

### Temporal Types

These types store dates, times, and time intervals.

| Type | Storage | Description | Range |
|------|---------|-------------|-------|
| `DATE` | 4 bytes | Calendar date | 4713 BC to 5874897 AD |
| `TIME` | 8 bytes | Time of day | 00:00:00 to 24:00:00 |
| `TIMESTAMP` | 8 bytes | Date and time | 4713 BC to 5874897 AD |
| `TIMESTAMPTZ` | 8 bytes | Date, time with timezone | 4713 BC to 5874897 AD |
| `INTERVAL` | 16 bytes | Time interval | ±178000000 years |

**Examples and Usage:**

```sql
-- Creating tables with date/time types
CREATE TABLE temporal_examples (
    event_date DATE,                    -- Just the date
    event_time TIME,                    -- Just the time
    created_at TIMESTAMP,               -- Date and time without timezone
    updated_at TIMESTAMPTZ,             -- Date and time with timezone
    duration INTERVAL                   -- Time spans
);

-- Inserting date/time values
INSERT INTO temporal_examples 
VALUES (
    '2024-01-15',                       -- DATE: YYYY-MM-DD
    '14:30:00',                         -- TIME: HH:MI:SS
    '2024-01-15 14:30:00',              -- TIMESTAMP: YYYY-MM-DD HH:MI:SS
    '2024-01-15 14:30:00-05',           -- TIMESTAMPTZ: with timezone
    '2 hours 30 minutes'                -- INTERVAL: time span
);

-- Using current date and time functions
INSERT INTO temporal_examples 
VALUES (
    CURRENT_DATE,                       -- Today's date
    CURRENT_TIME,                       -- Current time
    CURRENT_TIMESTAMP,                  -- Current date and time
    NOW(),                              -- Current date and time with timezone
    '1 day'::INTERVAL                   -- One day interval
);
```

**Common Date/Time Patterns:**

```sql
-- Format examples for insertion
DATE: '2024-12-25', '2024/12/25', '25-DEC-2024'
TIME: '14:30:00', '14:30', '02:30 PM'
TIMESTAMP: '2024-12-25 14:30:00', '2024-12-25 14:30'

-- Interval examples
'1 day'::INTERVAL
'2 hours 30 minutes'::INTERVAL
'1 week 3 days'::INTERVAL
'1 month'::INTERVAL
```

## Boolean Data Type

### Boolean Type

Stores true/false values.

| Type | Storage | Values | Description |
|------|---------|--------|-------------|
| `BOOLEAN` | 1 byte | TRUE, FALSE, NULL | Logical true/false |

**Examples and Usage:**

```sql
-- Creating tables with boolean types
CREATE TABLE boolean_examples (
    is_active BOOLEAN,                  -- Active status
    is_verified BOOLEAN,                -- Verification status
    has_permission BOOLEAN              -- Permission flags
);

-- Inserting boolean values
INSERT INTO boolean_examples 
VALUES 
    (TRUE, FALSE, NULL),                -- Different boolean states
    ('yes', 'no', '1'),                 -- Various truthy/falsy inputs
    ('on', 'off', '0'),                 -- More alternative inputs
    ('t', 'f', 'true');                 -- Single character versions

-- Valid boolean inputs:
-- TRUE: true, yes, on, 1, t, y
-- FALSE: false, no, off, 0, f, n

-- Querying with boolean
SELECT * FROM boolean_examples WHERE is_active = TRUE;
SELECT * FROM boolean_examples WHERE is_verified IS NOT TRUE;
SELECT * FROM boolean_examples WHERE has_permission IS NULL;
```
