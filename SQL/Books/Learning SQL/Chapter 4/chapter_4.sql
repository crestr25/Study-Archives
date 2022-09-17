---------------
-- CHAPTER 4 --
---------------

-- <> opetator maps to a NOT
select * from actor where not actor_id = 3;
select * from actor where actor_id <> 3;

-- Both select are equal

---------------
-- EXERCISES --
---------------

-- Query for the exercise
SELECT payment_id, customer_id, amount, date(payment_date) FROM sakila.payment where payment_id between 101 and 120;

-----------------
-- EXERCISE-01 --
-----------------
select * from (SELECT payment_id, customer_id, amount, date(payment_date) as payment_date
FROM sakila.payment
where payment_id between 101 and 120) as p
where p.customer_id <> 5
and (p.amount > 8 OR p.payment_date = '2005-08-23');

-----------------
-- EXERCISE-02 --
-----------------
select * from (SELECT payment_id, customer_id, amount, date(payment_date) as payment_date
FROM sakila.payment
where payment_id between 101 and 120) as p
where p.customer_id = 5
and NOT (p.amount > 6 OR p.payment_date = '2005-06-19');

-----------------
-- EXERCISE-03 --
-----------------
select * from sakila.payment
where amount in (1.98, 7.98, 9.98);

-----------------
-- EXERCISE-04 --
-----------------
select * from sakila.customer where last_name like '_A%W%';
