# PostgreSQL DDL, DML, and Schema Management - Comprehensive Guide

## Introduction to SQL Command Categories

### Understanding DDL (Data Definition Language)

**What is DDL?**
DDL stands for Data Definition Language. These are SQL commands used to define, modify, and delete database structures but not the data within them. Think of DDL as the blueprint or architecture of your database - it creates the containers that will hold your data.

**Key DDL Commands:**

- `CREATE` - Builds new database objects like tables, indexes, views
- `ALTER` - Modifies existing database structures
- `DROP` - Removes database objects entirely
- `TRUNCATE` - Empties tables but keeps the structure
- `RENAME` - Changes names of database objects

**When to use DDL:**

- When setting up a new database system
- When you need to add new tables or columns
- When modifying the structure of existing tables
- During database maintenance or upgrades

### Understanding DML (Data Manipulation Language)

**What is DML?**
DML stands for Data Manipulation Language. These commands work with the actual data stored within the database structures created by DDL. If DDL is the architecture, DML is the furniture and people inside the building.

**Key DML Commands:**

- `INSERT` - Adds new records to tables
- `UPDATE` - Modifies existing records
- `DELETE` - Removes records from tables
- `SELECT` - Retrieves data from tables (sometimes considered DQL - Data Query Language)

**When to use DML:**

- When adding new data to your application
- When modifying existing information
- When removing outdated or incorrect data
- When generating reports or extracting information

## Schema Management

### What is a Database Schema?

**Conceptual Understanding:**
A schema is like a folder within your database that contains related database objects. Imagine a large office building:

- The database is the entire building
- Schemas are different departments (HR, Finance, Sales)
- Tables are the filing cabinets within each department

**Why Use Schemas?**

1. **Organization** - Group related tables together
2. **Security** - Control access at the schema level
3. **Avoiding Name Conflicts** - Two tables can have the same name if they're in different schemas
4. **Multi-tenancy** - Separate data for different clients or applications

### Creating and Managing Schemas in Practice

```sql
-- Create a new schema for an e-commerce application
CREATE SCHEMA ecommerce;

-- Create a schema with specific ownership
CREATE SCHEMA inventory AUTHORIZATION store_manager;

-- What happens behind the scenes:
-- PostgreSQL creates a namespace called 'ecommerce'
-- The user who creates the schema becomes its owner
-- The schema is empty until we add tables to it
```

**Setting Search Paths:**

```sql
-- Tell PostgreSQL where to look for tables
SET search_path TO ecommerce, public;

-- This means: "When I reference a table name, first look in the ecommerce schema,
-- then look in the public schema if you don't find it there"
```

**Real-world Schema Organization:**

```sql
-- Create separate schemas for different application modules
CREATE SCHEMA hr;           -- Human Resources
CREATE SCHEMA finance;      -- Financial data
CREATE SCHEMA inventory;    -- Product inventory
CREATE SCHEMA sales;        -- Sales and orders
CREATE SCHEMA reporting;    -- Reports and analytics

-- Now create tables in appropriate schemas
CREATE TABLE hr.employees (...);
CREATE TABLE finance.invoices (...);
CREATE TABLE inventory.products (...);
```

**Schema Operations:**

```sql
-- View all schemas in the database
SELECT schema_name 
FROM information_schema.schemata;

-- See which schema is currently first in search path
SHOW search_path;

-- Transfer a table from one schema to another
ALTER TABLE public.old_customers SET SCHEMA ecommerce;

-- Drop an empty schema
DROP SCHEMA temporary_data;

-- Drop a schema and everything in it (use with caution!)
DROP SCHEMA old_application CASCADE;
```

## DDL

### CREATE TABLE - Building Your Data Structures

**Understanding Table Creation:**
When you create a table, you're defining:

- What columns the table will have
- What type of data each column can hold
- What rules (constraints) the data must follow
- How the table relates to other tables

```sql
-- Basic table creation breakdown:
CREATE TABLE products (
    -- Column definitions:
    product_id SERIAL PRIMARY KEY,      -- Unique identifier
    product_name VARCHAR(100) NOT NULL, -- Product name (required)
    price DECIMAL(10,2) NOT NULL,       -- Price with 2 decimal places
    description TEXT,                   -- Optional description
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Auto-filled timestamp
);

-- What each part means:
-- CREATE TABLE products - "Create a new table called 'products'"
-- product_id SERIAL - "Create an auto-incrementing number column"
-- PRIMARY KEY - "This column uniquely identifies each row"
-- VARCHAR(100) - "Text column that can hold up to 100 characters"
-- NOT NULL - "This field is required and cannot be empty"
-- DECIMAL(10,2) - "Number that can have up to 10 digits with 2 decimal places"
-- TEXT - "Can hold large amounts of text"
-- DEFAULT CURRENT_TIMESTAMP - "If no value is provided, use the current time"
```

**Creating Tables with Relationships:**

```sql
-- Customers table (parent table)
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

-- Orders table (child table that references customers)
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,           -- References customers table
    order_date DATE DEFAULT CURRENT_DATE,
    total_amount DECIMAL(10,2) DEFAULT 0,
    
    -- Foreign key constraint explicitly named
    CONSTRAINT fk_orders_customers 
    FOREIGN KEY (customer_id) 
    REFERENCES customers(customer_id)
    ON DELETE RESTRICT
);

-- How this works:
-- Each order must have a valid customer_id that exists in the customers table
-- The ON DELETE RESTRICT prevents deleting customers who have orders
```

### ALTER TABLE - Modifying Existing Structures

**When to Use ALTER TABLE:**

- When you need to add new columns to an existing table
- When you want to modify column data types
- When you need to add or remove constraints
- When renaming tables or columns

```sql
-- Starting with a simple table
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

-- Add new columns as business needs evolve
ALTER TABLE employees 
ADD COLUMN email VARCHAR(100),
ADD COLUMN hire_date DATE,
ADD COLUMN salary DECIMAL(10,2);

-- Modify existing columns
ALTER TABLE employees 
ALTER COLUMN first_name SET NOT NULL,
ALTER COLUMN last_name SET NOT NULL;

-- Add constraints to existing columns
ALTER TABLE employees 
ADD CONSTRAINT uk_employees_email UNIQUE (email);

-- Change column data type (be careful with existing data!)
ALTER TABLE employees 
ALTER COLUMN salary TYPE DECIMAL(12,2);

-- Rename a column
ALTER TABLE employees 
RENAME COLUMN salary TO annual_salary;

-- Rename the entire table
ALTER TABLE employees 
RENAME TO staff_members;
```

### DROP TABLE - Removing Tables

**Understanding DROP TABLE:**
The DROP TABLE command completely removes a table and all its data from the database. This is a destructive operation and should be used carefully.

```sql
-- Basic table removal
DROP TABLE temporary_data;

-- Safe drop (won't cause errors if table doesn't exist)
DROP TABLE IF EXISTS temp_logs;

-- Forceful drop (removes table and dependent objects)
DROP TABLE departments CASCADE;

-- What CASCADE does:
-- If other tables have foreign keys pointing to this table,
-- those constraints will also be dropped along with the table
```

### TRUNCATE TABLE - Quickly Emptying Tables

**TRUNCATE vs DELETE:**

- `TRUNCATE` removes all rows quickly and resets auto-increment counters
- `DELETE` removes rows one by one and can be rolled back
- `TRUNCATE` is faster but has fewer safety features

```sql
-- Remove all data from a table quickly
TRUNCATE TABLE audit_logs;

-- Truncate multiple tables at once
TRUNCATE TABLE table1, table2, table3;

-- Truncate and reset the auto-increment counter
TRUNCATE TABLE customers RESTART IDENTITY;

-- Truncate with CASCADE (affects foreign key references)
TRUNCATE TABLE parent_table CASCADE;

-- When to use TRUNCATE:
-- Clearing log tables
-- Resetting test data
-- Emptying temporary tables

-- When to use DELETE instead:
-- When you need to remove specific rows with WHERE clause
-- When you want the operation to be transactional (can rollback)
-- When you don't want to reset auto-increment counters
```

## Constraints - Enforcing Data Integrity

### What Are Constraints?

**Purpose of Constraints:**
Constraints are rules that enforce data integrity at the database level. They ensure that your data follows business rules and maintains consistency, even if application code has bugs.

**Benefits of Constraints:**

- Prevent invalid data from being inserted
- Maintain relationships between tables
- Ensure data consistency across the application
- Provide documentation about data rules

### NOT NULL Constraint

**Understanding NOT NULL:**
This constraint ensures that a column must always have a value - it cannot be left empty or NULL.

```sql
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,           -- Username is required
    email VARCHAR(100) NOT NULL,             -- Email is required
    phone VARCHAR(15),                       -- Phone is optional
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- What happens with NOT NULL:
INSERT INTO users (username, email) VALUES ('john_doe', 'john@email.com');  -- Works
INSERT INTO users (username) VALUES ('jane_doe');  -- Fails: email is NULL
INSERT INTO users (email) VALUES ('test@email.com');  -- Fails: username is NULL

-- Adding NOT NULL to existing column (only if column has no NULL values)
ALTER TABLE users 
ALTER COLUMN phone SET NOT NULL;
```

### UNIQUE Constraint

**Understanding UNIQUE:**
This constraint ensures that all values in a column are different from each other.

```sql
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_code VARCHAR(20) UNIQUE NOT NULL,    -- Each product code must be unique
    product_name VARCHAR(100) NOT NULL,
    sku VARCHAR(50) UNIQUE,                      -- SKU must be unique but can be NULL
    price DECIMAL(10,2) NOT NULL
);

-- How UNIQUE works:
INSERT INTO products (product_code, product_name, price) 
VALUES ('LAP-001', 'Laptop', 999.99);  -- Works

INSERT INTO products (product_code, product_name, price) 
VALUES ('LAP-001', 'Another Laptop', 899.99);  -- Fails: duplicate product_code

-- Multiple NULL values are allowed in UNIQUE columns
INSERT INTO products (product_code, product_name, price, sku) 
VALUES ('LAP-002', 'Laptop', 999.99, NULL);  -- Works

INSERT INTO products (product_code, product_name, price, sku) 
VALUES ('LAP-003', 'Laptop', 999.99, NULL);  -- Works (NULL != NULL)
```

### PRIMARY KEY Constraint

**Understanding Primary Keys:**
A primary key uniquely identifies each record in a table. It's the main way to reference specific rows.

```sql
-- Single column primary key (most common)
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,      -- Auto-incrementing primary key
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

-- Composite primary key (multiple columns together form the key)
CREATE TABLE order_items (
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (order_id, product_id)   -- Combination must be unique
);

-- What makes a good primary key:
-- 1. Unique - no two rows can have the same value
-- 2. Never NULL - always has a value
-- 3. Stable - doesn't change over time
-- 4. Simple - easy to work with
```

### FOREIGN KEY Constraint

**Understanding Foreign Keys:**
Foreign keys create relationships between tables by referencing the primary key of another table.

```sql
-- Parent table
CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(100) UNIQUE NOT NULL
);

-- Child table with foreign key
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    department_id INTEGER NOT NULL,
    
    -- Foreign key constraint
    FOREIGN KEY (department_id) 
    REFERENCES departments(department_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
);

-- How this works:
-- Each employee must belong to a valid department
-- You cannot delete a department that has employees (RESTRICT)
-- If a department_id changes, employee references update automatically (CASCADE)
```

### CHECK Constraint

**Understanding CHECK Constraints:**
CHECK constraints allow you to define custom rules that data must follow.

```sql
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    hire_date DATE NOT NULL,
    department VARCHAR(50),
    
    -- Various CHECK constraints
    CONSTRAINT chk_salary_positive CHECK (salary > 0),
    CONSTRAINT chk_hire_date_reasonable CHECK (hire_date >= '2000-01-01'),
    CONSTRAINT chk_valid_department CHECK (
        department IN ('HR', 'Engineering', 'Sales', 'Marketing', 'Finance')
    ),
    CONSTRAINT chk_email_format CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
);

-- What CHECK constraints enforce:
INSERT INTO employees (first_name, last_name, email, salary, hire_date, department)
VALUES ('John', 'Doe', 'john.doe@company.com', 50000, '2020-01-15', 'Engineering');  -- Works

INSERT INTO employees (first_name, last_name, email, salary, hire_date, department)
VALUES ('Jane', 'Smith', 'invalid-email', 50000, '2020-01-15', 'Engineering');  -- Fails: email format

INSERT INTO employees (first_name, last_name, email, salary, hire_date, department)
VALUES ('Bob', 'Wilson', 'bob@company.com', -1000, '2020-01-15', 'Engineering');  -- Fails: negative salary
```

## DEFAULT Values

### Understanding DEFAULT Values

**Purpose of DEFAULT:**
Default values are automatically used when no value is provided for a column during INSERT operations. They help ensure data consistency and reduce the amount of data that needs to be explicitly provided.

```sql
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    order_number VARCHAR(20) UNIQUE NOT NULL,
    
    -- Various DEFAULT value examples:
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Current date and time
    status VARCHAR(20) DEFAULT 'pending',              -- Fixed default value
    priority INTEGER DEFAULT 1,                        -- Numeric default
    is_approved BOOLEAN DEFAULT FALSE,                 -- Boolean default
    notes TEXT DEFAULT 'No special instructions',      -- Text default
    
    -- Default with expression
    expires_at TIMESTAMP DEFAULT (CURRENT_TIMESTAMP + INTERVAL '30 days')
);

-- How DEFAULT works in practice:
INSERT INTO orders (order_number) VALUES ('ORD-001');
-- Resulting row automatically gets:
-- order_date: current timestamp
-- status: 'pending'
-- priority: 1
-- is_approved: false
-- notes: 'No special instructions'
-- expires_at: 30 days from now
```

**Advanced DEFAULT Patterns:**

```sql
-- Default with UUID generation
CREATE TABLE documents (
    document_id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    document_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Default with conditional logic
CREATE TABLE tasks (
    task_id SERIAL PRIMARY KEY,
    task_name VARCHAR(100) NOT NULL,
    due_date DATE DEFAULT (CURRENT_DATE + INTERVAL '7 days'),
    status VARCHAR(20) DEFAULT 'pending',
    
    -- Default based on another column's value
    is_urgent BOOLEAN DEFAULT FALSE,
    priority INTEGER DEFAULT 
        CASE 
            WHEN is_urgent THEN 1 
            ELSE 3 
        END
);

-- Managing DEFAULT values:
ALTER TABLE orders 
ALTER COLUMN status SET DEFAULT 'new';

ALTER TABLE orders 
ALTER COLUMN status DROP DEFAULT;
```

## CASCADE Operations - Managing Dependencies

### Understanding CASCADE

**What Problem CASCADE Solves:**
When tables have relationships (foreign keys), operations on one table can affect related tables. CASCADE rules define what should happen to related records when you update or delete primary records.

### CASCADE in Foreign Keys

```sql
-- Parent table
CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(100) UNIQUE NOT NULL
);

-- Child table with various CASCADE options
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    department_id INTEGER,
    manager_id INTEGER,
    
    -- Different CASCADE scenarios:
    
    -- 1. CASCADE on DELETE: Delete employees when department is deleted
    FOREIGN KEY (department_id) 
    REFERENCES departments(department_id)
    ON DELETE CASCADE,
    
    -- 2. SET NULL on DELETE: Set manager_id to NULL when manager is deleted
    FOREIGN KEY (manager_id)
    REFERENCES employees(employee_id)
    ON DELETE SET NULL,
    
    -- 3. RESTRICT on DELETE: Prevent department deletion if employees exist
    -- This is the default behavior if not specified
    
    -- 4. CASCADE on UPDATE: Update references when primary key changes
    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
    ON UPDATE CASCADE
);
```

**CASCADE Options Explained:**

| Option | Behavior | Use Case |
|--------|----------|----------|
| `ON DELETE CASCADE` | Delete child records when parent is deleted | Order items when order is deleted |
| `ON DELETE SET NULL` | Set foreign key to NULL when parent is deleted | Employees when department is removed |
| `ON DELETE SET DEFAULT` | Set foreign key to default value | Assign to default category when category deleted |
| `ON DELETE RESTRICT` | Prevent deletion if children exist | Prevent deleting customers with orders |
| `ON UPDATE CASCADE` | Update child references when parent key changes | When primary key values need to change |

### Practical CASCADE Examples

```sql
-- Example 1: Blog system with posts and comments
CREATE TABLE posts (
    post_id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL
);

CREATE TABLE comments (
    comment_id SERIAL PRIMARY KEY,
    post_id INTEGER NOT NULL,
    comment_text TEXT NOT NULL,
    FOREIGN KEY (post_id) REFERENCES posts(post_id) ON DELETE CASCADE
);

-- When a post is deleted, all its comments are automatically deleted

-- Example 2: User management system
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE user_profiles (
    profile_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    bio TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE user_settings (
    setting_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    setting_name VARCHAR(50) NOT NULL,
    setting_value VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Deleting a user automatically removes their profile and settings
```

### CASCADE in DROP Operations

```sql
-- CASCADE with DROP TABLE
DROP TABLE departments CASCADE;
-- This will drop the departments table AND:
-- Remove any foreign key constraints that reference this table
-- Drop any views that depend on this table

-- CASCADE with DROP SCHEMA
DROP SCHEMA ecommerce CASCADE;
-- This removes the schema and ALL objects within it

-- When to use CASCADE with DROP:
-- During database cleanup or restructuring
-- When you're sure you want to remove all dependencies
-- In development and testing environments

-- When to avoid CASCADE with DROP:
-- In production databases without proper backups
-- When you're not sure what will be affected
-- When other applications might depend on the objects
```

## Auto Incrementing - Automatic ID Generation

### Understanding Auto Incrementing

**Purpose:**
Auto incrementing columns automatically generate unique numeric values for each new row, typically used for primary keys.

### Using SERIAL Data Type

**SERIAL in PostgreSQL:**
PostgreSQL provides the SERIAL pseudo-type that automatically creates a sequence and sets up the auto-increment behavior.

```sql
-- Basic SERIAL usage
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,      -- Auto-incrementing primary key
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

-- What happens behind the scenes:
-- 1. Creates a sequence called "customers_customer_id_seq"
-- 2. Sets customer_id as INTEGER NOT NULL
-- 3. Sets default value to nextval('customers_customer_id_seq')
-- 4. Makes it the primary key

-- Using the table:
INSERT INTO customers (first_name, last_name) 
VALUES ('John', 'Doe');  -- customer_id automatically set to 1

INSERT INTO customers (first_name, last_name) 
VALUES ('Jane', 'Smith');  -- customer_id automatically set to 2

-- You can explicitly get the last generated value
SELECT currval('customers_customer_id_seq');
```

### Using IDENTITY Columns (PostgreSQL 10+)

**Modern Approach:**
IDENTITY columns are the SQL standard way of handling auto-incrementing columns and provide more control than SERIAL.

```sql
-- GENERATED ALWAYS AS IDENTITY (recommended)
CREATE TABLE products (
    product_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL
);

-- GENERATED BY DEFAULT AS IDENTITY (allows manual overrides)
CREATE TABLE orders (
    order_id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    order_number VARCHAR(20) NOT NULL
);

-- Differences:
-- GENERATED ALWAYS: Database always generates the value, cannot be overridden
-- GENERATED BY DEFAULT: Database generates value unless explicitly provided

-- Examples:
INSERT INTO products (product_name) VALUES ('Laptop');  -- Works, ID auto-generated

INSERT INTO products (product_id, product_name) VALUES (100, 'Tablet');  
-- Fails with GENERATED ALWAYS: cannot insert into identity column

INSERT INTO orders (order_number) VALUES ('ORD-001');  -- Works, ID auto-generated

INSERT INTO orders (order_id, order_number) VALUES (100, 'ORD-002');  
-- Works with GENERATED BY DEFAULT: manual value accepted
```

### Custom Sequences for Advanced Control

**When to Use Custom Sequences:**

- When you need specific starting points or increments
- When you want to share a sequence across multiple tables
- When you need complex numbering patterns

```sql
-- Create a custom sequence
CREATE SEQUENCE invoice_number_seq 
START WITH 1000          -- Start numbering from 1000
INCREMENT BY 1           -- Increase by 1 each time
MINVALUE 1000            -- Never go below 1000
MAXVALUE 999999          -- Maximum value
CYCLE;                   -- Start over when max is reached

-- Use the sequence in a table
CREATE TABLE invoices (
    invoice_number INTEGER DEFAULT nextval('invoice_number_seq') PRIMARY KEY,
    amount DECIMAL(10,2) NOT NULL,
    customer_name VARCHAR(100) NOT NULL
);

-- Manual sequence control
SELECT nextval('invoice_number_seq');        -- Get and advance to next value
SELECT currval('invoice_number_seq');        -- Get current value without advancing
SELECT setval('invoice_number_seq', 2000);   -- Reset sequence to specific value

-- Using the table:
INSERT INTO invoices (amount, customer_name) 
VALUES (199.99, 'John Doe');  -- invoice_number automatically set to 1000

INSERT INTO invoices (amount, customer_name) 
VALUES (299.99, 'Jane Smith');  -- invoice_number automatically set to 1001
```

### Advanced Auto-increment Patterns

**Custom Formatting with Triggers:**

```sql
-- Create a sequence for custom ID generation
CREATE SEQUENCE order_seq START 1;

-- Table with custom formatted IDs
CREATE TABLE orders (
    order_id VARCHAR(20) PRIMARY KEY,    -- Custom formatted ID
    order_date DATE DEFAULT CURRENT_DATE,
    total_amount DECIMAL(10,2) DEFAULT 0
);

-- Function to generate custom order IDs
CREATE OR REPLACE FUNCTION generate_order_id()
RETURNS TRIGGER AS $$
BEGIN
    -- Format: ORD-YYYYMMDD-000001
    NEW.order_id := 'ORD-' || 
                   to_char(CURRENT_DATE, 'YYYYMMDD-') || 
                   lpad(nextval('order_seq')::text, 6, '0');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger to automatically generate custom IDs
CREATE TRIGGER trg_order_id
    BEFORE INSERT ON orders
    FOR EACH ROW
    EXECUTE FUNCTION generate_order_id();

-- Usage:
INSERT INTO orders (total_amount) VALUES (150.00);
-- order_id automatically set to something like: ORD-20231201-000001
```

## DML

### INSERT - Adding New Data

**Basic INSERT Operations:**

```sql
-- Single row insertion
INSERT INTO customers (first_name, last_name, email) 
VALUES ('John', 'Doe', 'john.doe@email.com');

-- Multiple row insertion (more efficient)
INSERT INTO products (product_name, price, category) 
VALUES 
    ('Laptop', 999.99, 'Electronics'),
    ('Book', 19.99, 'Books'),
    ('T-Shirt', 29.99, 'Clothing');

-- Insert with DEFAULT values
INSERT INTO orders (order_number) 
VALUES ('ORD-001');
-- All other columns use their DEFAULT values

-- Insert with RETURNING clause (get generated values back)
INSERT INTO employees (first_name, last_name, email, salary)
VALUES ('Jane', 'Smith', 'jane.smith@email.com', 75000)
RETURNING employee_id, first_name, last_name;
-- Returns the newly inserted row with generated employee_id

-- Copy data from another table
INSERT INTO archived_orders (order_id, order_date, total_amount)
SELECT order_id, order_date, total_amount 
FROM orders 
WHERE order_date < '2020-01-01';
```

### UPDATE - Modifying Existing Data

**UPDATE Operations:**

```sql
-- Basic single-row update
UPDATE employees 
SET salary = 80000 
WHERE employee_id = 1;

-- Multiple column update
UPDATE products 
SET price = price * 0.9,                    -- 10% discount
    last_updated = CURRENT_TIMESTAMP         -- Update timestamp
WHERE category = 'Electronics';

-- Conditional update with subquery
UPDATE employees 
SET department_id = (
    SELECT department_id FROM departments WHERE department_name = 'IT'
)
WHERE email LIKE '%@company.com';

-- Update with JOIN (PostgreSQL syntax)
UPDATE order_items oi
SET unit_price = p.price
FROM products p
WHERE oi.product_id = p.product_id 
AND oi.unit_price != p.price;

-- Update with RETURNING clause
UPDATE customers 
SET status = 'premium'
WHERE total_orders > 10
RETURNING customer_id, email, status;
-- Returns the updated rows
```

### DELETE - Removing Data

**DELETE Operations:**

```sql
-- Delete specific rows
DELETE FROM customers 
WHERE status = 'inactive';

-- Delete using subquery
DELETE FROM order_items 
WHERE order_id IN (
    SELECT order_id FROM orders 
    WHERE order_date < '2019-01-01'
);

-- Delete with JOIN (PostgreSQL syntax)
DELETE FROM order_items oi
USING orders o
WHERE oi.order_id = o.order_id 
AND o.order_date < '2019-01-01';

-- Delete all rows from a table
DELETE FROM temp_logs;

-- Safe delete with existence check
DELETE FROM products 
WHERE discontinued = true
AND product_id NOT IN (SELECT product_id FROM order_items);

-- Delete with RETURNING clause
DELETE FROM products 
WHERE discontinued = true
RETURNING product_id, product_name;
-- Returns information about deleted rows
```

## Example

```sql
-- Create a database for a small business

-- Step 1: Create schemas for organization
CREATE SCHEMA hr;
CREATE SCHEMA sales;
CREATE SCHEMA inventory;

-- Step 2: Create tables with proper constraints and relationships

-- Departments table in HR schema
CREATE TABLE hr.departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(100) UNIQUE NOT NULL,
    budget DECIMAL(12,2) DEFAULT 0 CHECK (budget >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Employees table in HR schema
CREATE TABLE hr.employees (
    employee_id SERIAL PRIMARY KEY,
    employee_code VARCHAR(10) UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    salary DECIMAL(10,2) NOT NULL CHECK (salary >= 0),
    department_id INTEGER,
    hire_date DATE DEFAULT CURRENT_DATE,
    status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'inactive', 'leave')),
    
    -- Additional constraints
    CONSTRAINT chk_salary_range CHECK (salary BETWEEN 30000 AND 200000),
    CONSTRAINT chk_valid_email CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'),
    
    -- Foreign key with CASCADE rules
    CONSTRAINT fk_employees_departments 
        FOREIGN KEY (department_id) REFERENCES hr.departments(department_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Products table in inventory schema
CREATE TABLE inventory.products (
    product_id SERIAL PRIMARY KEY,
    product_code VARCHAR(20) UNIQUE NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL CHECK (price > 0),
    stock_quantity INTEGER NOT NULL DEFAULT 0 CHECK (stock_quantity >= 0),
    reorder_level INTEGER NOT NULL DEFAULT 10 CHECK (reorder_level >= 0),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT chk_reorder_valid CHECK (reorder_level <= stock_quantity)
);

-- Customers table in sales schema
CREATE TABLE sales.customers (
    customer_id SERIAL PRIMARY KEY,
    customer_code VARCHAR(10) UNIQUE NOT NULL,
    company_name VARCHAR(100) NOT NULL,
    contact_name VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT chk_valid_customer_email CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
);

-- Orders table in sales schema
CREATE TABLE sales.orders (
    order_id SERIAL PRIMARY KEY,
    order_number VARCHAR(20) UNIQUE NOT NULL,
    customer_id INTEGER NOT NULL,
    order_date DATE DEFAULT CURRENT_DATE,
    required_date DATE,
    shipped_date DATE,
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'processing', 'shipped', 'delivered', 'cancelled')),
    total_amount DECIMAL(10,2) DEFAULT 0,
    
    CONSTRAINT fk_orders_customers 
        FOREIGN KEY (customer_id) REFERENCES sales.customers(customer_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    
    CONSTRAINT chk_dates_valid CHECK (shipped_date IS NULL OR shipped_date >= order_date),
    CONSTRAINT chk_required_date_valid CHECK (required_date IS NULL OR required_date >= order_date)
);

-- Order items table (junction table for many-to-many relationship)
CREATE TABLE sales.order_items (
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10,2) NOT NULL CHECK (unit_price > 0),
    discount DECIMAL(4,2) DEFAULT 0 CHECK (discount >= 0 AND discount <= 1),
    
    PRIMARY KEY (order_id, product_id),
    
    CONSTRAINT fk_order_items_orders 
        FOREIGN KEY (order_id) REFERENCES sales.orders(order_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
        
    CONSTRAINT fk_order_items_products 
        FOREIGN KEY (product_id) REFERENCES inventory.products(product_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
        
    CONSTRAINT chk_discount_range CHECK (discount BETWEEN 0 AND 1)
);

-- Step 3: Insert sample data
INSERT INTO hr.departments (department_name, budget) 
VALUES 
    ('Engineering', 500000),
    ('Sales', 300000),
    ('Marketing', 200000);

INSERT INTO hr.employees (employee_code, first_name, last_name, email, salary, department_id)
VALUES 
    ('EMP-001', 'John', 'Doe', 'john.doe@company.com', 75000, 1),
    ('EMP-002', 'Jane', 'Smith', 'jane.smith@company.com', 65000, 2),
    ('EMP-003', 'Bob', 'Johnson', 'bob.johnson@company.com', 80000, 1);

INSERT INTO inventory.products (product_code, product_name, price, stock_quantity, reorder_level)
VALUES 
    ('PROD-001', 'Laptop', 999.99, 50, 10),
    ('PROD-002', 'Mouse', 25.99, 100, 20),
    ('PROD-003', 'Keyboard', 75.50, 75, 15);

INSERT INTO sales.customers (customer_code, company_name, contact_name, email)
VALUES 
    ('CUST-001', 'ABC Corporation', 'Alice Brown', 'alice@abccorp.com'),
    ('CUST-002', 'XYZ Ltd', 'Charlie Wilson', 'charlie@xyzltd.com');

-- Step 4: Demonstrate operations
-- Create a new order
INSERT INTO sales.orders (order_number, customer_id) 
VALUES ('ORD-001', 1)
RETURNING order_id;

-- Add items to the order
INSERT INTO sales.order_items (order_id, product_id, quantity, unit_price)
VALUES 
    (1, 1, 2, 999.99),
    (1, 2, 5, 25.99);

-- Update order total
UPDATE sales.orders 
SET total_amount = (
    SELECT SUM(quantity * unit_price * (1 - discount))
    FROM sales.order_items 
    WHERE order_id = 1
)
WHERE order_id = 1;

-- Query to see the complete order
SELECT 
    o.order_number,
    c.company_name,
    p.product_name,
    oi.quantity,
    oi.unit_price,
    oi.quantity * oi.unit_price as line_total
FROM sales.orders o
JOIN sales.customers c ON o.customer_id = c.customer_id
JOIN sales.order_items oi ON o.order_id = oi.order_id
JOIN inventory.products p ON oi.product_id = p.product_id
WHERE o.order_id = 1;
```
