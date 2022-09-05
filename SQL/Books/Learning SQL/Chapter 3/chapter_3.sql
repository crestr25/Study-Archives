/* SELECT STATEMENT */
use sakila;

SELECT * FROM language; -- from the table language show all columns and all rows.

SELECT name FROM language; -- from the table language show all rows of column name

SELECT language_id, -- Row to be included from table
        'COMMON' language_str, -- String literal
        language_id * 100 lang_mult, -- Expression
        upper(name) language_name -- Built in function
FROM language;

SELECT VERSION(), USER(), DATABASE() FROM DUAL;

-- To select a distinct entry for all column
SELECT distinct actor_id FROM film_actor;

-----------------
-- TABLE TYPES --
-----------------

-- DERIVED TABLES
select concat(cust.last_name, ', ', cust.first_name) full_name
from (select first_name, last_name, email
        from customer where first_name = 'JESSIE') cust;

-- TEMPORARY TABLES
CREATE TEMPORARY TABLE actors_j
(actor_id smallint(5),
first_name varchar(45),
last_name varchar(45));

INSERT INTO actors_j (SELECT actor_id, first_name, last_name FROM actor WHERE last_name LIKE 'J%');

-- VIEWS
CREATE VIEW cust_vw AS (SELECT customer_id, first_name, last_name, active FROM customer);

SELECT * FROM cust_vw;

------------------
-- WHERE CLAUSE --
------------------
SELECT title, rating, rental_duration
FROM film
WHERE (rating = 'G' AND rental_duration >= 7) 
    OR (rating = 'PG-13' AND rental_duration < 4);


---------------------
-- GROUP BY CLAUSE --
---------------------
SELECT c.first_name, c.last_name, count(r.rental_id) count_films
FROM customer c
    INNER JOIN rental r
    ON c.customer_id = r.customer_id
GROUP BY c.first_name, c.last_name
HAVING count_films > 40;

---------------------
-- ORDER BY CLAUSE --
---------------------
SELECT c.first_name, c.last_name, time(r.rental_date) rental_time
FROM customer c
    INNER JOIN rental r
    ON c.customer_id = r.customer_id
WHERE date(r.rental_date) = '2005-6-14'
ORDER BY 3 desc limit 3;


---------------
-- EXERCISES --
---------------


-----------------
-- EXERCISE-01 --
-----------------
SELECT actor_id, first_name, last_name
FROM actor
ORDER BY last_name, first_name;

-----------------
-- EXERCISE-02 --
-----------------
SELECT actor_id, first_name, last_name
FROM actor
WHERE last_name in ('WILLIAMS', 'DAVIS')
ORDER BY last_name, first_name;

-----------------
-- EXERCISE-03 --
-----------------
SELECT customer_id
FROM rental
WHERE date(rental_date) = '2005-7-5'
GROUP BY customer_id
ORDER BY customer_id;


SELECT DISTINCT customer_id
FROM rental
WHERE date(rental_date) = '2005-7-5';


-----------------
-- EXERCISE-04 --
-----------------
SELECT c.email, r.return_date
FROM customer c
    INNER JOIN rental r
    ON c.customer_id = r.customer_id
WHERE date(r.rental_date) = '2005-06-14'
ORDER BY r.return_date desc;
