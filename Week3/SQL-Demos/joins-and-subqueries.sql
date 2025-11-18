-- Joins and Subqueries
/*
What if I want to return data from across multiple tables?
I can run individual selects and cross reference manually, but thats not efficient
and Im not returning everything as a discrete set of data. 
*/

-- Lets say I want to return... the album title and artist name
-- of every album. 

-- Lets try an inner join - Only records that match are returned
-- If I leave off the INNER keyword and don't use any other JOIN type
-- just the word "JOIN" - it defaults to inner join
EXPLAIN
SELECT a.title AS album, ar.name AS artist
FROM album AS a 
JOIN artist ar ON a.artist_id = ar.artist_id;

-- Left and Right Joins
-- These are mirrors of eachother, your left table is 
-- the first table you select (next to the FROM), the right table
-- is the second one selected (after the JOIN)

-- LEFT JOIN - ALL records from the left table + matches from the right 
-- LEFT JOIN will return all rows from the left table, as well as the requested
-- data from the right table IF it exists. If the right side row doesn't exist, we get a NULL
-- useful for seeing "whats missing" between two tables. 
SELECT ar.name, a.title
FROM artist ar 
LEFT JOIN album a ON ar.artist_id = a.artist_id
WHERE ar.name LIKE 'A%';

-- Outer joins - Lets start with FULL OUTER JOIN

-- FULL OUTER JOIN returns all rows from both tables.
-- Matches records where possible, shows NULLs where no matches exist.
-- Eseentially the complete union of both tables. 

SELECT ar.name, a.title
FROM artist ar 
FULL OUTER JOIN album a ON ar.artist_id = a.artist_id;

-- Cross Joins - Cartesian Product 
-- CROSS JOIN combines every row from the first table, 
-- with every row from the second table. Notice, no ON is needed.
-- Lets us see every possible combination of selected column values in
-- both tables. 
EXPLAIN
SELECT g.name as genre, mt.name as media_type
FROM genre g      
CROSS JOIN media_type mt
WHERE g.name IN ('Rock', 'Jazz'); -- IN allows you to run a WHERE on a set of VALUES;


-- Equi and Theta Joins
-- Equi joins = any join that use equality conditions in the ON clause
-- So our Inner joins are also EQUI JOINS. 

-- Theta joins... are any other comparison operator. (<, >, <=, >= !=)


-- Lets practice a Theta Join 
-- Lets find tracks that are longer than the average track from their album
EXPLAIN
SELECT 
    t1.name as track_name,
    t1.milliseconds as track_length,
    t2.avg_album_length
FROM track t1
INNER JOIN ( -- We're going to use a subquery. Literally a query within a query.
    SELECT album_id, AVG(milliseconds) as avg_album_length
    FROM track
    GROUP BY album_id
) as t2 ON t1.album_id = t2.album_id AND t1.milliseconds > t2.avg_album_length;


-- Self Join - Don't see it on the curriculum but it can be useful
-- Lets us join a table to itself. You just your normal inner or left 
-- or right join, but the right table is the same as the left table

-- Lets get all employees and their managers
-- Joining employee table to itself
SELECT 
    emp.first_name as employee, 
    mgr.first_name as manager
FROM employee emp
LEFT JOIN employee mgr ON emp.reports_to = mgr.employee_id;


-- Subqueries, queries within queries. We saw one used in an INNER JOIN, but you can use them
-- inside of WHERE, or IN, or even inside a SELECT 

SELECT name, milliseconds
FROM track
WHERE milliseconds > (
    SELECT AVG(milliseconds) FROM track -- Using subquery to get around no aggregate functions in WHERE
)
ORDER BY milliseconds DESC;

-- The subquery calculates the average track length across the data set
-- The outer query finds tracks longer than the average. 
-- The subquery is always evaluated first. 

-- Subquery inside the IN operator
SELECT name, composer
FROM track
WHERE album_id IN (
    SELECT album_id
    FROM album
    WHERE title LIKE '%Greatest%Hit%'
);

-- Subquery in a SELECT
-- Usually used for scalar values (things that return one value)

SELECT 
    name, 
    unit_price, 
    (SELECT  MAX(unit_price) FROM track) as max_price_in_catalog,
    (SELECT AVG(unit_price) from track) as avg_price_in_catalog
FROM track
WHERE unit_price > 1.00;

--test


