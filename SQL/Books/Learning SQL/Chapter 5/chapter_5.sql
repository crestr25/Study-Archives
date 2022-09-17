---------------
-- CHAPTER 5 --
---------------






---------------
-- EXERCISES --
---------------

-----------------
-- EXERCISE-01 --
-----------------
SELECT c.first_name, c.last_name, a.address, ct.city
FROM sakila.customer c
	INNER JOIN sakila.address a
	ON c.address_id = a.address_id
	INNER JOIN sakila.city ct
	ON a.city_id = ct.city_id
WHERE a.district = 'California';

-----------------
-- EXERCISE-02 --
-----------------
select f.title
from sakila.actor ac
	inner join sakila.film_actor fa
		on fa.actor_id = ac.actor_id 
	inner join sakila.film f
		on f.film_id = fa.film_id
where ac.first_name = 'JOHN';

-----------------
-- EXERCISE-03 --
-----------------
select a.address, a.city_id, a2.address, a2.city_id 
from sakila.address a
inner join sakila.address a2 
on a.city_id = a2.city_id
and a.address_id <> a2.address_id;
