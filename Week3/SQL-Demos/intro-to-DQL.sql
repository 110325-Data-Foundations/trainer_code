
-- This is a comment in SQL
/*
SQL has multiple statement/query families.

Statement - Declare something about the shape of the data, or the database schema (users, roles, etc)
Query - Returning data... but also altering the data in a table.

Within SQL there are some "sub-languages" or "sub-families" of commands.

DQL - Data Query Language - SELECT (And its associated keywords)
DML - Data Manipulation Language - INSERT, UPDATE, DELETE
DDL - Data Definition Language - CREATE, DROP, ALTER, RENAME, TRUNCATE 
TCL - Transaction Control Language - START/BEGIN TRANSACTION, COMMIT, ROLLBACK, SAVEPOINT
DCL - Data Control Language - GRANT, REVOKE 

*/

-- We are going to start with DQL - SELECT!
-- SELECT (what you want to select) FROM (table);

SELECT * FROM actor; -- SELECT everything from the actor table

-- Building from that, we can select specific columns to return
SELECT actor_id, first_name FROM actor;

-- Lets start limiting our returns via LIMIT
SELECT * FROM album LIMIT 10;

-- Notice in our album table, we have album_id and artist_id
-- In the album table album_id is the PRIMARY KEY - its what allows us to uniquely 
-- identify a record in this table. Every table NEEDS a primary key.
-- Primary keys MUST be unique AND not null. 

-- In the album table, artist_id is a FOREIGN KEY
-- FOREIGN KEYs are just PRIMARY KEYS in another table denoting some relationship.ACCESS
-- In SQL there are three possible relationship types: One to One, One to Many, Many to Many

-- Filtering and Sorting on SELECTS
-- If we want more than just filtering by returned columns or limiting returned rows...
-- We need to use things like the WHERE clause

SELECT * FROM genre;

SELECT name, composer, genre_id FROM track 
WHERE genre_id = 1; -- Filtering for every rock track

-- We can combine clauses, next lets look at ORDER BY
SELECT name, milliseconds
FROM track
WHERE genre_id = 1
ORDER BY milliseconds DESC
LIMIT 10;

-- We can also combine conditions using things like AND and OR
-- AND: both conditions must be met
-- OR: one condition must be met 
SELECT name, milliseconds
FROM track
WHERE genre_id = 1 AND milliseconds > 500000; -- Both conditions have to be met


-- We can do pattern matching with LIKE (and some regex)

SELECT email FROM customer;

SELECT customer_id, first_name, email
FROM customer
WHERE email LIKE '%@gmail.com';


-- There are prebuilt functions in SQL, and you can also define your own.
-- The two types are scalar and aggregate functions 

-- Scalar Functions - operate on a single value and return a single value 
-- upper(), lower(), length(), round()

-- Aggregate functions - operate over a set of values, and return a single value
-- representing some aggregate
-- count(), sum(), avg(), min(), max()

-- Basic aggregation against tracks table
SELECT 
COUNT(*), ROUND(AVG(milliseconds), 2) AS track_length, MIN(unit_price), MAX(unit_price) 
FROM track;


-- We can create summary rows for each unique genre_id 
-- to see which genres have the most tracks 
-- We can do this using GROUP BY

SELECT genre_id, COUNT(*) as track_count
FROM track 
GROUP BY genre_id -- HAVING is like WHERE but for grouped results
ORDER BY track_count DESC;