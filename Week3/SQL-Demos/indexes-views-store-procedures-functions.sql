
-- Yesterday we went through beginner to intermediate/advanced DQL.

/* Transactions and TCL 

    We use transactions when we have complex operations (more than one query/statement) that
    we want to affect the database as a unit. We want to ensure that all commands execute OR
    no changes are persisted. 

    Before we get into creating Transactions, we need to go over ACID

    ACID - 
        Atomicity: This operation can't be broken down any further. All parts of our 
        transaction must succeed OR they all fail. 

        Consistency: Database moves from one valid state to another. 

        Isolation: Transactions cant interfere or step on one another.

        Durability: Once a transaction is committed, changes are permanent. 
*/

-- Lets model a transaction inside our chinook Database. 
-- Lets transfer a track between playlists

-- Starts a transaction block, all following statements belong to the transaction
BEGIN TRANSACTION; 

-- Remove the track from one playlist
DELETE FROM playlist_track -- Some light DML: Deleting a record from a TABLE
WHERE playlist_id = 1 AND track_id = 1; -- Because this table has a composite primary key, 
-- we need to specify both key columns to select one unique row 

SAVEPOINT deleted_track;

-- Add the track to another playlist 
INSERT INTO playlist_track (playlist_id, track_id)
VALUES (2, 1);

SAVEPOINT inserted_track;

-- Lets verify (for illustrative purposes) our changes before we commit
SELECT * FROM playlist_track
WHERE track_id = 1 AND playlist_id IN (1, 2);

-- Transactions can involves many many operations all grouped together, some that can fail.
-- In a large transaction we want to add SAVEPOINTs and places where if an error is detected
-- we ROLLBACK 

-- We can then target a specific savepoint to rollback to, and then either abort the transaction
-- try the step again, etc. 
ROLLBACK to deleted_track; 

ROLLBACK;
COMMIT; -- Commit applies the changes to the database. Always end a transaction with a commit.

/* 
    Indexes 

    Indexes in SQL are like indexes in a book, they help you find data faster.
    There are some costs though - they increase storage space and can make writes slower. 

*/

-- Basic select with no index
EXPLAIN ANALYZE
SELECT * FROM track
WHERE composer LIKE '%John%';

-- Lets create a simple index to speed up composer searches
CREATE INDEX idx_track_composer ON track(composer);

EXPLAIN ANALYZE
SELECT * FROM track
WHERE composer LIKE '%John%';

--If you find yourself using more than one column to filter data in a specific table often
--you can create a multi-column index
CREATE INDEX idx_invoice_customer_total ON invoice(customer_id, total);

EXPLAIN ANALYZE
SELECT * FROM invoice
WHERE customer_id = 1 AND total > 5;


/*
    Views - Saved queries that we can then easily re-use

    Views are virtual tables based on saved queries.
    We can then re-use the result set as if it was a table - even within other queries
*/

CREATE OR REPLACE VIEW rock_tracks_view AS
SELECT 
    t.track_id,
    t.name as track_name,
    a.title as album_title,
    ar.name as artist_name,
    t.milliseconds,
    t.unit_price
FROM track t    
JOIN album a ON t.album_id = a.album_id
JOIN artist ar ON a.artist_id = ar.artist_id
JOIN genre g ON t.genre_id = g.genre_id
WHERE g.name = 'Rock';

-- Once we have our view we can then query and filter it (and even use it in joins) like a table
SELECT * FROM rock_tracks_view
WHERE album_title = 'Restless and Wild';


-- Store Procedures - reusable SQL code blocks
-- Kind of like functions, but SQL also has user defined functions
-- which are their own thing.
-- To do this in PSQL we need a *little bit* of SQL Procedural Language - psql's extension of sql 

-- Lets create a stored procedure to update track prices
-- We'll do this genre wide, and increase the pricing by a certain percent
ROLLBACK;

CREATE OR REPLACE PROCEDURE update_track_prices(
    genre_name TEXT,
    price_increase_percent NUMERIC
)
LANGUAGE plpgsql -- using that Postgres procedural language
AS $$
BEGIN 
    UPDATE track
    SET unit_price = unit_price * (1 + (price_increase_percent / 100)) -- we do follow order of operations
    WHERE genre_id IN (
        SELECT genre_id FROM genre WHERE name = genre_name -- Getting back the genre_id for a given genre name
    );

    RAISE NOTICE 'Updated pries for % genre by %', genre_name, price_increase_percent; -- psql equivalent to print()

END;
$$;


SELECT track_name, unit_price FROM rock_tracks_view; -- Lets see the prices of rock tracks before calling our procedure

CALL update_track_prices('Rock', 10.0);


/* 

    In general, Stored Procedures affect data and perform some action against the database, 
    Functions return values. 

    Functions can be used within SQL statements - think things like SUM() or COUNT(). 

    We can define our own functions if we need to. 
*/

-- Lets create a function to get a single value back - in this case how much a specific user
-- spent at our music store


CREATE OR REPLACE FUNCTION get_customer_total_spent(customer_id_param INTEGER)
RETURNS NUMERIC -- return type
LANGUAGE plpgsql -- using that procedural language again for psql
AS $$ 
DECLARE
    total_spent NUMERIC; -- declaring any variables, total will hold the total amount spent.
BEGIN
    SELECT SUM(total) INTO total_spent
    FROM invoice
    WHERE customer_id = customer_id_param;

    RETURN total_spent; -- Notice we use RETURNS up top, but just RETURN at the end of the function
END;
$$;

-- If we want to use our function, we can use it as any other function. So like selecting the COUNT() as part
-- of a query
SELECT first_name, get_customer_total_spent(customer_id) as total_spent
FROM customer;


/*

    Triggers - A stored procedure in a database that happens automatically when a specific event occurs.GROUP BY
    Triggers can be set up to automatically run on things like INSERT, UPDATE, DELETE, etc.

    Can be useful for logging, task automation, etc. 

*/

