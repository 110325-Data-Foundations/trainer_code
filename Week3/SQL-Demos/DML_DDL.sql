-- CREATE DATABASE companydb;

-- Lets create a simple database to represent a company.

-- Schemas are like folders for database objects. Related tables will be put 
-- into their respective schemas. Using DCL (not in this demo) you can fine tune
-- what users can take what actions within each individual schema. 
CREATE SCHEMA hr;
CREATE SCHEMA audit;


-- DDL - Data Definition language

-- DDL commands allow us to define the structure of our database and its objects
-- CREATE ALTER DROP TRUNCATE - these all affect tables and other db objects, not rows

-- Lets create a table with some constraints

CREATE TABLE hr.departments ( -- Column name, data type

    -- In addition to giving every column a name and a data type, we can have our db
    -- enforce constraints. These can help us enforce data integrity.
    -- Column_name data_type constraint(s), 
    department_id SERIAL PRIMARY KEY, -- Auto incrementing primary key
    department_name VARCHAR(50) NOT NULL UNIQUE,
    budget NUMERIC(10, 2) DEFAULT 10000.00, -- Setting a default value if none is provided
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- This gets the time at creation 
)

CREATE TABLE hr.employees (
    employee_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    salary NUMERIC(8,2) CHECK (salary >= 30000),   -- We can use a CHECK constraint to make sure its atleast some value
    department_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- DepartmentId is a foreign key - the database won't know this unless we inform it
    -- We do that with a foreign key constraint
    CONSTRAINT fk_employee_department
        FOREIGN KEY (department_id) -- Telling it which column is a foreign KEY
        REFERENCES hr.departments(department_id) -- Telling it which table and column it references

        -- We can tell the database how to handle things like DELETE and UPDATE with regards to the fk constraint
        ON DELETE SET NULL -- if the department gets deleted, any fks will be set to null - preserving reference integrity.
        ON UPDATE CASCADE -- update foreign key references when the other table changes (if it ever does)
)       

CREATE TABLE audit.employee_log (

    log_id SERIAL PRIMARY KEY,
    employee_id INTEGER NOT NULL,
    action VARCHAR(10) NOT NULL CHECK (action IN ('INSERT', 'UPDATE', 'DELETE')), -- action must be one of these three
    action_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    details TEXT -- TEXT is like a huge varchar, can technically hold a 1GB string
)


-- DML - Data Manipulation Language 
-- DML lets us work with individual rows/records in our db
-- INSERT, UPDATE, DELETE 

INSERT INTO hr.departments (department_name, budget) VALUES
('IT', 1000000),
('Accounting', 500);


SELECT * FROM hr.departments;


INSERT INTO hr.employees (name, salary, department_id) VALUES
('Matthew', 60002, 10);


SELECT * FROM hr.employees;


--Just want to see the data in both tables
SELECT e.employee_id, e.name, d.department_name, d.department_id
FROM hr.employees e 
JOIN hr.departments d ON e.department_id = d.department_id;


-- Update a department_id
UPDATE hr.departments
SET department_id = 10 -- new value  
WHERE department_id = 1; -- some constraint to identify a column (or several columns)


DELETE FROM hr.departments
WHERE department_id = 10;

SELECT * FROM hr.employees; 

-- Lets create that trigger

-- Triggers in PSQL are technically user defined functions that RETURN a trigger

CREATE OR REPLACE FUNCTION hr.log_employee_insert()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN

    INSERT INTO audit.employee_log (employee_id, action, details)
    VALUES (
        NEW.employee_id,
        'INSERT',
        format('New employee: %s has been created', NEW.name)
    );

    RETURN NEW;
END;
$$;

-- Only handles inserts into hr.employees
-- Accesses NEW record values for the inserted row with NEW
-- Logs the inserts with our custom message to audit.employee_log (technically a different schema)
-- Returns that NEW record so that the insert can complete 

-- After we create our function that returns a trigger, we need to associate it with a specific action (or actions)
-- on a specific table 

CREATE TRIGGER employee_insert_audit_trigger
    AFTER INSERT ON hr.employees -- When and where will this run?
    FOR EACH ROW -- frequency it will run on? - in our case every time something is inserted
    EXECUTE FUNCTION hr.log_employee_insert() -- what function does that trigger call?


INSERT INTO hr.employees (name, salary, department_id) VALUES
('Ryan', 999999, 2);

SELECT * FROM audit.employee_log;