# Normalization

## Database Keys

### Primary Key

**Definition:** A column or set of columns that uniquely identifies each row in a table.

**Characteristics:**

- Must contain unique values
- Cannot contain NULL values
- Only one primary key per table
- Used to enforce entity integrity

**Example:**
In an `Employees` table, `EmployeeID` serves as the primary key, ensuring each employee has a unique identifier.

### Candidate Key

**Definition:** Any column or set of columns that could serve as the primary key because they contain unique values and cannot contain NULLs.

**Characteristics:**

- Multiple candidate keys can exist in one table
- Each candidate key must be unique and non-NULL
- One candidate key is chosen as the primary key

**Example:**
In a `Users` table, both `UserID` and `Email` could be candidate keys because both are unique and non-NULL.

### Composite Key

**Definition:** A primary key that consists of two or more columns.

**Characteristics:**

- Each column alone may not be unique
- The combination of columns must be unique
- All columns in the composite key cannot be NULL

**Example:**
In an `Order_Items` table, the combination of `OrderID` and `ProductID` forms a composite key, as the same product can appear in multiple orders and multiple products can appear in the same order, but the combination is unique.

### Unique Key

**Definition:** A constraint that ensures all values in a column are different.

**Characteristics:**

- Allows NULL values (unless combined with NOT NULL)
- Multiple unique keys can exist per table
- Used to enforce uniqueness on non-primary key columns

**Example:**
In an `Employees` table, `SocialSecurityNumber` can be a unique key to prevent duplicate SSNs while `EmployeeID` remains the primary key.

### Secondary/Alternate Key

**Definition:** Any candidate key that wasn't chosen as the primary key.

**Characteristics:**

- Provides alternative ways to access records
- Often have unique indexes for performance
- Useful for business logic and data retrieval

**Example:**
In a `Products` table, `ProductCode` (like "PROD-001") might be an alternate key while `ProductID` (auto-increment number) is the primary key.

### Foreign Key

**Definition:** A column or set of columns that establishes a link between data in two tables.

**Characteristics:**

- References the primary key of another table
- Enforces referential integrity
- Can have NULL values (unless constrained otherwise)
- Prevents orphan records

**Example:**
In an `Orders` table, `CustomerID` is a foreign key that references the `CustomerID` primary key in the `Customers` table.

## Multiplicity (Cardinality)

**Definition:** Describes the numerical relationship between entities in a database.

### Types of Multiplicity

#### One-to-One (1:1)

- One record in Table A relates to exactly one record in Table B
- **Example:** `Users` and `UserProfiles` - each user has exactly one profile

#### One-to-Many (1:N) & Many-to-One (N:1)

- One record in Table A relates to many records in Table B
- **Example:** `Customers` and `Orders` - one customer can place many orders

#### Many-to-Many (M:N)

- Many records in Table A relate to many records in Table B
- Requires a junction table to resolve the relationship
- **Example:** `Students` and `Courses` - students take many courses, courses have many students

## Normalization: From Unstructured Data to 3NF

### The Normalization Principle
>
> **"The key, the whole key, and nothing but the key"**
>
> - Every non-key attribute must depend on the key (1NF)
> - The whole key (2NF)  
> - And nothing but the key (3NF)

### Starting Point: Unstructured Data (0NF)

**Example - School Enrollment System:**

| StudentID | StudentName | Course1 | Course1_Instructor | Course2 | Course2_Instructor | Phone | City | State |
|-----------|-------------|---------|-------------------|---------|-------------------|-------|------|-------|
| S101 | John Doe | Math | Dr. Smith | Science | Dr. Johnson | 555-001 | Boston | MA |
| S102 | Jane Smith | History | Dr. Brown | Math | Dr. Smith | 555-002 | Boston | MA |
| S103 | Bob Wilson | Science | Dr. Johnson | | | 555-003 | Cambridge | MA |

**Problems with 0NF:**

- Repeating groups (Course1, Course2 columns)
- Partial dependencies
- Transitive dependencies
- Update, insertion, and deletion anomalies
- Data redundancy

---

### First Normal Form (1NF) - Eliminate Repeating Groups

**Rules:**

1. Each column contains atomic values
2. No repeating groups of columns

**Transformed Structure:**

**Students Table:**

| StudentID | StudentName | Phone | City | State |
|-----------|-------------|-------|------|-------|
| S101 | John Doe | 555-001 | Boston | MA |
| S102 | Jane Smith | 555-002 | Boston | MA |
| S103 | Bob Wilson | 555-003 | Cambridge | MA |

**Courses Table:**

| CourseID | CourseName | Instructor |
|----------|------------|------------|
| C201 | Math | Dr. Smith |
| C202 | Science | Dr. Johnson |
| C203 | History | Dr. Brown |

**Enrollments Table:**

| StudentID | CourseID |
|-----------|----------|
| S101 | C201 |
| S101 | C202 |
| S102 | C203 |
| S102 | C201 |
| S103 | C202 |

**Improvements:**

- No repeating groups
- Atomic values
- Defined primary keys

**Remaining Issues:**

- **Partial Dependency:** City and State depend only on StudentID, not the full key in some contexts
- **Transitive Dependency:** City to State relationship

---

### Second Normal Form (2NF) - Remove Partial Dependencies

**Definition of Partial Dependency:** When a non-key attribute depends on only part of a composite primary key.

**Rules:**

1. Be in 1NF
2. Remove partial dependencies - all non-key attributes must depend on the entire primary key

**Analysis:**

- In our 1NF design, the `Enrollments` table has a composite primary key (StudentID, CourseID)
- No non-key attributes exist in this table, so no partial dependencies

**However, we identify transitive dependencies in the Students table:**

- StudentID to City to State
- This is a **transitive dependency** (State depends on City, which depends on StudentID)

**Transformed Structure:**

**Students Table:**

| StudentID | StudentName | Phone | ZipCode |
|-----------|-------------|-------|---------|
| S101 | John Doe | 555-001 | 02108 |
| S102 | Jane Smith | 555-002 | 02108 |
| S103 | Bob Wilson | 555-003 | 02138 |

**ZipCodes Table:**

| ZipCode | City | State |
|---------|------|-------|
| 02108 | Boston | MA |
| 02138 | Cambridge | MA |

**Other tables remain the same.**

**Improvements:**

- No partial dependencies
- Reduced data redundancy

**Remaining Issues:**

- **Transitive Dependency:** Still exists if we had attributes like Instructor to Department

---

### Third Normal Form (3NF) - Remove Transitive Dependencies

**Definition of Transitive Dependency:** When a non-key attribute depends on another non-key attribute rather than directly on the primary key.

**Rules:**

1. Be in 2NF
2. Remove transitive dependencies - no non-key attribute should depend on another non-key attribute

**Let's enhance our example to show a transitive dependency:**

Suppose we add department information to courses:

**Courses Table (Problematic):**

| CourseID | CourseName | Instructor | Instructor_Office | Department |
|----------|------------|------------|-------------------|------------|
| C201 | Math | Dr. Smith | Room 101 | Mathematics |
| C202 | Science | Dr. Johnson | Room 202 | Sciences |
| C203 | History | Dr. Brown | Room 103 | Humanities |

**Transitive Dependency Identified:**

- CourseID to Instructor to Instructor_Office
- CourseID to Instructor to Department
- Instructor_Office and Department depend on Instructor, not directly on CourseID

**Transformed Structure:**

**Courses Table:**

| CourseID | CourseName | InstructorID |
|----------|------------|--------------|
| C201 | Math | I001 |
| C202 | Science | I002 |
| C203 | History | I003 |

**Instructors Table:**

| InstructorID | InstructorName | Office | DepartmentID |
|--------------|----------------|--------|--------------|
| I001 | Dr. Smith | Room 101 | D01 |
| I002 | Dr. Johnson | Room 202 | D02 |
| I003 | Dr. Brown | Room 103 | D03 |

**Departments Table:**

| DepartmentID | DepartmentName |
|--------------|---------------|
| D01 | Mathematics |
| D02 | Sciences |
| D03 | Humanities |

**Final 3NF Structure Summary:**

1. **Students** (StudentID, StudentName, Phone, ZipCode)
2. **ZipCodes** (ZipCode, City, State)
3. **Courses** (CourseID, CourseName, InstructorID)
4. **Instructors** (InstructorID, InstructorName, Office, DepartmentID)
5. **Departments** (DepartmentID, DepartmentName)
6. **Enrollments** (StudentID, CourseID)

---

## Benefits of Full Normalization (3NF)

### Data Integrity

- Eliminates update anomalies (change data in one place)
- Prevents insertion anomalies (add data without unnecessary dependencies)
- Avoids deletion anomalies (delete data without losing related information)

### Reduced Redundancy

- Each fact stored only once
- Efficient storage utilization
- Consistent data across the system

### Flexibility and Maintainability

- Easy to modify structure without affecting entire system
- Simplified queries and relationships
- Better performance for certain operations

### Scalability

- Handles growth efficiently
- Clear relationship patterns
- Predictable behavior

## When to Denormalize

While normalization is generally recommended, there are scenarios where deliberate denormalization improves performance:

- **Reporting databases** where read performance is critical
- **Data warehousing** with complex analytical queries
- **High-traffic web applications** requiring fast reads
- **Historical data** that doesn't change

The key is to normalize first, then denormalize strategically based on specific performance requirements.
