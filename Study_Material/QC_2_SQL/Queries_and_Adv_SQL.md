# PostgreSQL Study Guide

## 1. Database Fundamentals

### What is a Database?

A database is an organized collection of structured data stored electronically in a computer system. It allows for efficient storage, retrieval, and manipulation of data.

**Key Characteristics:**

- Data is organized in tables with rows and columns
- Supports multiple users accessing data simultaneously
- Provides data integrity and security
- Allows relationships between different data entities

### What is SQL?

SQL (Structured Query Language) is a standard programming language specifically designed for managing and manipulating relational databases.

```sql
-- This is a basic SQL query that retrieves all customer records from the USA
-- The asterisk (*) means "all columns"
SELECT * FROM customers WHERE country = 'USA';

-- Explanation:
-- SELECT: Specifies which columns to retrieve
-- FROM: Specifies which table to query
-- WHERE: Filters records based on conditions
```

## 2. SQL Table Structure

Tables are the fundamental storage structures in relational databases. They consist of columns (attributes) and rows (records).

```sql
-- Creating a table with various constraints and data types
CREATE TABLE employees (
    -- SERIAL is an auto-incrementing integer, PRIMARY KEY ensures uniqueness
    employee_id SERIAL PRIMARY KEY,
    
    -- VARCHAR(50) allows variable-length strings up to 50 characters
    -- NOT NULL constraint prevents null values
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    
    -- UNIQUE constraint ensures no duplicate email addresses
    email VARCHAR(100) UNIQUE,
    
    -- DEFAULT sets a default value if none is provided
    hire_date DATE DEFAULT CURRENT_DATE,
    
    -- DECIMAL(10,2) stores numbers with up to 10 digits, 2 after decimal
    salary DECIMAL(10,2),
    
    -- Foreign key (would reference departments table)
    department_id INTEGER
);

-- Example of table relationships:
-- employees.department_id → departments.department_id
```

## 3. Common SQL Data Types

| Category | Data Types | Description & Use Cases |
|----------|------------|-------------|
| **Numeric** | `INTEGER`, `SERIAL`, `DECIMAL(p,s)`, `REAL` | `SERIAL` auto-increments (like employee IDs), `DECIMAL` for money |
| **Character** | `VARCHAR(n)`, `CHAR(n)`, `TEXT` | `VARCHAR` for names, `TEXT` for descriptions |
| **Date/Time** | `DATE`, `TIME`, `TIMESTAMP`, `INTERVAL` | `TIMESTAMP` for exact moments, `DATE` for birthdays |
| **Boolean** | `BOOLEAN` | True/False for flags like "is_active" |
| **Binary** | `BYTEA` | Store files, images, or binary data |

## 4. SQL Sublanguages Explained

### DDL (Data Definition Language) - Defines Database Structure

```sql
-- CREATE: Defines new database objects
CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL  -- Department name cannot be null
);

-- ALTER: Modifies existing database objects
ALTER TABLE employees ADD COLUMN phone VARCHAR(15);
-- Adds a new column to store phone numbers

-- DROP: Removes database objects
DROP TABLE temporary_data;
-- Completely removes the table and its data (use with caution!)
```

### DML (Data Manipulation Language) - Manages Data

```sql
-- INSERT: Adds new records
INSERT INTO employees (first_name, last_name, email) 
VALUES ('John', 'Doe', 'john.doe@email.com');
-- Adds a new employee record

-- UPDATE: Modifies existing records
UPDATE employees SET salary = 50000 WHERE employee_id = 1;
-- Increases salary for employee with ID 1

-- DELETE: Removes records
DELETE FROM employees WHERE employee_id = 5;
-- Removes employee with ID 5 from the database
```

### DQL (Data Query Language) - Retrieves Data

```sql
SELECT first_name, last_name, salary 
FROM employees 
WHERE salary > 60000 
ORDER BY last_name;
-- Retrieves well-paid employees sorted alphabetically by last name
```

### TCL (Transaction Control Language) - Manages Transactions

```sql
BEGIN;  -- Starts a transaction block

-- Transfer $100 from account 1 to account 2
UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;

-- Only if both updates succeed:
COMMIT;  -- Makes changes permanent

-- If there's an error:
-- ROLLBACK;  -- Undoes all changes in the transaction
```

### DCL (Data Control Language) - Manages Security

```sql
GRANT SELECT, INSERT ON employees TO manager_role;
-- Allows managers to view and add employees

REVOKE DELETE ON customers FROM user1;
-- Prevents user1 from deleting customer records
```

## 5. SELECT Statement - Complete Breakdown

### Basic SELECT Operations

```sql
-- Retrieve all columns from products table
SELECT * FROM products;

-- Retrieve only specific columns
SELECT product_name, price FROM products;

-- Get unique categories (no duplicates)
SELECT DISTINCT category FROM products;
```

### WHERE Clause - Filtering Records

```sql
-- Complex conditions with AND/OR
SELECT * FROM employees 
WHERE salary > 50000 
AND department_id = 3 
OR hire_date > '2020-01-01';
-- Employees who earn >50K AND in dept 3 OR hired after 2020

-- BETWEEN (inclusive range) and IN (multiple possible values)
SELECT * FROM products 
WHERE price BETWEEN 10 AND 100  -- Prices from 10 to 100 (inclusive)
AND category IN ('Electronics', 'Books');  -- In either category
```

### ORDER BY and LIMIT - Sorting and Limiting Results

```sql
SELECT product_name, price 
FROM products 
ORDER BY price DESC, product_name ASC  -- Sort by price high-to-low, then name A-Z
LIMIT 10;  -- Show only top 10 results
```

### GROUP BY and HAVING - Aggregating Data

```sql
-- GROUP BY collapses rows into groups
-- HAVING filters groups (WHERE filters individual rows)
SELECT department_id, AVG(salary) as avg_salary, COUNT(*) as employee_count
FROM employees 
GROUP BY department_id  -- Group employees by their department
HAVING AVG(salary) > 45000;  -- Only show departments where average salary > 45K
```

## 6. Functions - Data Transformation and Analysis

### Aggregate Functions - Work on Groups of Data

```sql
SELECT 
    COUNT(*) as total_employees,           -- Count all rows
    AVG(salary) as average_salary,         -- Calculate average
    MAX(salary) as highest_salary,         -- Find maximum value
    MIN(salary) as lowest_salary,          -- Find minimum value
    SUM(salary) as total_salary_budget     -- Calculate sum
FROM employees;
-- All these functions ignore NULL values
```

### Scalar Functions - Work on Individual Values

```sql
SELECT 
    UPPER(first_name) as upper_name,       -- Convert to uppercase
    LENGTH(last_name) as name_length,      -- Count characters
    ROUND(salary, 0) as rounded_salary,    -- Round to whole number
    CONCAT(first_name, ' ', last_name) as full_name,  -- Combine strings
    EXTRACT(YEAR FROM hire_date) as hire_year  -- Extract year from date
FROM employees;
-- Each function transforms individual values row by row
```

## 7. Subqueries - Queries Within Queries

### Single-row Subquery - Returns One Value

```sql
-- Find employees who earn more than the company average
SELECT first_name, last_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);  -- Subquery runs first
-- The subquery must return exactly one value for comparison
```

### Multiple-row Subquery - Returns Multiple Values

```sql
-- Find products in electronic categories
SELECT product_name, price
FROM products
WHERE category_id IN (SELECT category_id FROM categories 
                     WHERE category_name LIKE '%Electronic%');
-- IN operator handles multiple values from subquery
```

### Correlated Subquery - References Outer Query

```sql
-- Find employees who earn more than their department average
SELECT first_name, last_name, salary, department_id
FROM employees e1
WHERE salary > (SELECT AVG(salary) FROM employees e2 
                WHERE e2.department_id = e1.department_id);
-- The subquery executes for each row in the outer query
-- e1.department_id comes from the outer query
```

## 8. Aliases - Giving Names to Columns and Tables

```sql
SELECT 
    e.first_name AS "First Name",           -- Column alias with spaces
    e.last_name AS "Last Name",             -- Use quotes for special characters
    d.department_name AS Department,        -- Simple column alias
    
    -- Correlated subquery in SELECT with alias
    (SELECT COUNT(*) FROM employees e2 
     WHERE e2.department_id = e.department_id) AS dept_count
     
FROM employees e  -- Table alias for shorter references
JOIN departments d ON e.department_id = d.department_id;

-- Benefits of aliases:
-- 1. Make column names more readable
-- 2. Shorten table names in complex queries
-- 3. Provide names for calculated columns
```

## 9. Joins - Combining Data from Multiple Tables

### INNER JOIN - Only Matching Records

```sql
-- Get employees and their department names
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id;
-- Only returns employees who have a department AND departments that have employees
-- This excludes employees without departments AND departments without employees
```

### LEFT JOIN - All Records from Left Table + Matches

```sql
-- Count employees in each department (including empty departments)
SELECT d.department_name, COUNT(e.employee_id) as employee_count
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name;
-- Returns ALL departments, even those with no employees
-- COUNT(e.employee_id) counts only actual employees (ignores NULLs)
```

### RIGHT JOIN - All Records from Right Table + Matches

```sql
-- Show all projects and their managers (even unmanaged projects)
SELECT e.first_name, p.project_name
FROM employees e
RIGHT JOIN projects p ON e.employee_id = p.manager_id;
-- Returns ALL projects, even those without a manager
-- Manager name will be NULL for unmanaged projects
```

### FULL OUTER JOIN - All Records from Both Tables

```sql
-- Show all employees and departments, regardless of matches
SELECT e.first_name, d.department_name
FROM employees e
FULL OUTER JOIN departments d ON e.department_id = d.department_id;
-- Returns:
-- - Employees with departments
-- - Employees without departments (department_name will be NULL)
-- - Departments without employees (first_name will be NULL)
```

### CROSS JOIN - All Possible Combinations

```sql
-- Create all possible size-color combinations
SELECT s.size_name, c.color_name
FROM sizes s
CROSS JOIN colors c;
-- Returns Cartesian product: every size paired with every color
-- Useful for generating test data or all possible combinations
```

### SELF JOIN - Joining a Table to Itself

```sql
-- Show employees and their managers (managers are also employees)
SELECT e1.first_name AS employee, e2.first_name AS manager
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.employee_id;
-- Uses the same table twice with different aliases
-- LEFT JOIN ensures employees without managers are still shown
```

## 10. Transactions and ACID Properties

### Transactions Example - Bank Transfer

```sql
BEGIN;  -- Start transaction

-- Transfer $100 from account 1 to account 2
UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;

-- At this point, changes are visible only to this transaction
-- Other users still see the original balances

-- If both updates succeed and business logic is satisfied:
COMMIT;  -- Make changes permanent and visible to all

-- If there's an error (insufficient funds, system failure):
-- ROLLBACK;  -- Undo both updates, return to original state
```

### ACID Properties Explained

1. **Atomicity** - "All or Nothing"
   - Entire transaction succeeds or entire transaction fails
   - No partial updates

2. **Consistency** - "Valid State Transitions"
   - Database moves from one valid state to another
   - Constraints are always satisfied

3. **Isolation** - "Concurrent Control"
   - Transactions don't interfere with each other
   - Different isolation levels control visibility of uncommitted changes

4. **Durability** - "Permanent Changes"
   - Committed transactions survive system failures
   - Changes are written to persistent storage

### Transaction Isolation Levels

```sql
-- Set isolation level for current transaction
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

BEGIN;
SELECT * FROM accounts WHERE account_id = 1;
-- In READ COMMITTED level:
-- - Can see other transactions' committed changes
-- - Cannot see other transactions' uncommitted changes
-- - Prevents "dirty reads"
COMMIT;

-- Other isolation levels:
-- READ UNCOMMITTED: Can see uncommitted changes (not recommended)
-- REPEATABLE READ: Consistent reads within transaction
-- SERIALIZABLE: Highest isolation, transactions appear serial
```

## 11. CRUD Operations - Foundation of Data Management

```sql
-- CREATE: Add new records
INSERT INTO customers (name, email) VALUES ('Alice Smith', 'alice@email.com');
-- Creates a new customer record

-- READ: Retrieve records
SELECT * FROM customers WHERE email = 'alice@email.com';
-- Finds the customer we just created

-- UPDATE: Modify existing records
UPDATE customers SET name = 'Alice Johnson' WHERE email = 'alice@email.com';
-- Updates the customer's name (maybe she got married)

-- DELETE: Remove records
DELETE FROM customers WHERE email = 'alice@email.com';
-- Removes the customer record (she closed her account)
```

## 12. Indexes - Improving Query Performance

Indexes are special data structures that improve the speed of data retrieval operations.

```sql
-- Create a basic index on last_name for faster searching
CREATE INDEX idx_employee_last_name ON employees(last_name);
-- Now queries like WHERE last_name = 'Smith' are much faster

-- Composite index for multi-column queries
CREATE INDEX idx_employee_dept_hire ON employees(department_id, hire_date);
-- Optimizes queries filtering on both department AND hire date

-- Unique index prevents duplicate values
CREATE UNIQUE INDEX idx_unique_email ON employees(email);
-- Ensures no two employees have the same email
-- Also speeds up email-based lookups

-- Partial index for conditional indexing
CREATE INDEX idx_high_salary ON employees(salary) WHERE salary > 100000;
-- Only indexes high-salary employees, saves space and maintenance time

-- View existing indexes
SELECT * FROM pg_indexes WHERE tablename = 'employees';
```

**When to use indexes:**

- Columns frequently used in WHERE clauses
- Columns used in JOIN conditions
- Columns with high selectivity (many unique values)

**When to avoid indexes:**

- Tables with frequent write operations (slows down INSERT/UPDATE/DELETE)
- Columns with few unique values (low selectivity)
- Small tables where sequential scan is faster

## 13. Triggers - Automated Actions on Data Changes

Triggers automatically execute functions when specified data modification events occur.

```sql
-- Step 1: Create an audit table to track changes
CREATE TABLE employee_audit (
    audit_id SERIAL PRIMARY KEY,                    -- Unique audit record ID
    employee_id INTEGER,                           -- Which employee was changed
    change_type VARCHAR(10),                       -- INSERT, UPDATE, or DELETE
    change_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- When change occurred
);

-- Step 2: Create a trigger function
CREATE OR REPLACE FUNCTION log_employee_changes()
RETURNS TRIGGER AS $$  -- Special return type for triggers
BEGIN
    -- TG_OP contains the operation that fired the trigger
    IF TG_OP = 'DELETE' THEN
        -- OLD contains the row being deleted
        INSERT INTO employee_audit (employee_id, change_type)
        VALUES (OLD.employee_id, 'DELETE');
        
    ELSIF TG_OP = 'UPDATE' THEN
        -- NEW contains the updated row values
        INSERT INTO employee_audit (employee_id, change_type)
        VALUES (NEW.employee_id, 'UPDATE');
        
    ELSIF TG_OP = 'INSERT' THEN
        -- NEW contains the inserted row values
        INSERT INTO employee_audit (employee_id, change_type)
        VALUES (NEW.employee_id, 'INSERT');
    END IF;
    
    -- Return appropriate value (NEW for INSERT/UPDATE, OLD for DELETE)
    RETURN COALESCE(NEW, OLD);
END;
$$ LANGUAGE plpgsql;  -- Use PostgreSQL's procedural language

-- Step 3: Create the trigger
CREATE TRIGGER trigger_employee_audit
    AFTER INSERT OR UPDATE OR DELETE ON employees  -- When to fire
    FOR EACH ROW  -- Row-level trigger (fires for each affected row)
    EXECUTE FUNCTION log_employee_changes();  -- Function to execute

-- Now any change to employees table will be automatically logged!
```

## 14. Views - Virtual Tables for Simplified Access

### Simple View - Abstracting Complex Queries

```sql
-- Create a view that shows only active employees
CREATE VIEW active_employees AS
SELECT employee_id, first_name, last_name, email, department_id
FROM employees
WHERE active = true;
-- The view behaves like a table but doesn't store data

-- Use the view like a regular table
SELECT * FROM active_employees WHERE department_id = 3;
-- Much simpler than repeating the WHERE active = true condition
```

### Materialized View - Storing Pre-computed Results

```sql
-- Create a materialized view that stores computed department statistics
CREATE MATERIALIZED VIEW department_stats AS
SELECT 
    d.department_name,
    COUNT(e.employee_id) as employee_count,
    AVG(e.salary) as avg_salary
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name;
-- Materialized views actually store the query results for fast access

-- Refresh when underlying data changes
REFRESH MATERIALIZED VIEW department_stats;
-- Needed because materialized views don't automatically update

-- Use cases:
-- - Complex aggregations that are expensive to compute
-- - Data that doesn't change frequently
-- - Reporting and dashboard applications
```

### Updatable View - Modifying Data Through Views

```sql
-- Create a view exposing only contact information
CREATE VIEW employee_contact_info AS
SELECT employee_id, first_name, last_name, email, phone
FROM employees;
-- Simple views based on one table are often updatable

-- Update data through the view
UPDATE employee_contact_info SET phone = '555-1234' WHERE employee_id = 1;
-- This actually updates the underlying employees table

-- Limitations:
-- - Views with JOINs, aggregates, or DISTINCT are usually not updatable
-- - Only one underlying table can be modified
```

## 15. Stored Procedures and Functions

| Feature / Capability                     | Stored Procedure | Function |
|-----------------------------------------|-----------------|---------|
| Return value                             | Does not have to return a value. Procedures can return data through output parameters or result sets, but returning a single value is not required. | Must return a value. Functions are required to return a scalar, composite type, or a table. |
| Multiple result sets                      | Can return multiple result sets. Useful for complex operations where several queries are executed. | Can return only a single value or a single table. Cannot return multiple independent result sets. |
| Data modification (INSERT/UPDATE/DELETE)| Can modify database data. Procedures are commonly used to perform DML operations. | Cannot modify database data directly if used in SQL statements. Functions are expected to be side-effect free when used in queries. |
| Transaction control (COMMIT/ROLLBACK)   | Can perform transaction control inside the procedure. | Cannot perform transaction control inside the function. Functions are executed within the transaction context of the caller. |
| Use inside SQL statements                | Cannot be called directly in a SELECT, WHERE, or other SQL expressions. | Can be used directly inside SELECT, WHERE, or other SQL expressions. |
| Input and output parameters             | Can accept both input and output parameters, allowing flexible data exchange. | Can accept input parameters, but only a single return value is allowed (no separate output parameters). |
| Exception handling                        | Supports exception handling using BEGIN...EXCEPTION blocks. | Limited exception handling. Functions can raise exceptions but cannot handle them as flexibly as procedures. |
| Calling other database objects           | Can call functions and other stored procedures. | Can call other functions, but cannot directly call stored procedures. |
| Use cases                                | Best suited for complex business logic, performing multiple DML operations, and orchestrating multiple queries. | Best suited for reusable calculations, data transformations, and returning computed values or tables within queries. |

### Stored Procedure - Performing Complex Operations

```sql
-- Create a procedure to increase an employee's salary
CREATE OR REPLACE PROCEDURE increase_salary(
    p_employee_id INTEGER,      -- Input parameter: employee ID
    p_percentage DECIMAL        -- Input parameter: percentage increase
)
LANGUAGE plpgsql                -- Use PostgreSQL's procedural language
AS $$
BEGIN
    -- Update the employee's salary
    UPDATE employees 
    SET salary = salary * (1 + p_percentage/100)
    WHERE employee_id = p_employee_id;
    
    -- If no rows were affected, the employee doesn't exist
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Employee with ID % not found', p_employee_id;
    END IF;
    
    -- Commit the transaction
    COMMIT;
END;
$$;

-- Call the procedure to give employee #1 a 10% raise
CALL increase_salary(1, 10);
```

### User-Defined Functions - Reusable Code Blocks

#### Scalar Function - Returns Single Value

```sql
-- Create a function that returns an employee's full name
CREATE OR REPLACE FUNCTION get_employee_full_name(
    p_employee_id INTEGER      -- Input parameter
)
RETURNS VARCHAR               -- Return type: string
LANGUAGE plpgsql
AS $$
DECLARE
    full_name VARCHAR;        -- Local variable declaration
BEGIN
    -- Query the database and store result in variable
    SELECT CONCAT(first_name, ' ', last_name)
    INTO full_name           -- Store query result into variable
    FROM employees
    WHERE employee_id = p_employee_id;
    
    -- Return the computed value
    RETURN full_name;
END;
$$;
```

#### Table Function - Returns Multiple Rows

```sql
-- Create a function that returns a table of employees by department
CREATE OR REPLACE FUNCTION get_employees_by_department(
    p_department_id INTEGER
)
RETURNS TABLE(                -- Define the structure of returned table
    emp_id INTEGER,
    full_name VARCHAR,
    emp_salary DECIMAL
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- RETURN QUERY sends query results directly as function output
    RETURN QUERY
    SELECT 
        employee_id,
        CONCAT(first_name, ' ', last_name),
        salary
    FROM employees
    WHERE department_id = p_department_id;
END;
$$;

-- Using the functions:
-- Scalar function in SELECT
SELECT get_employee_full_name(1) as employee_name;

-- Table function in FROM clause (treat like a table)
SELECT * FROM get_employees_by_department(3);
```
