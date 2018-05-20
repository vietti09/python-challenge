USE sakila;
SELECT first_name, last_name from actor;


SHOW tables;

SET SQL_SAFE_UPDATES = 0;

SELECT UPPER(CONCAT(first_name," ", last_name)) as 'Actor Name' FROM actor;

SELECT actor_id, first_name, last_name from actor WHERE first_name ='Joe';

SELECT * from actor WHERE last_name LIKE '%GEN%';

SELECT * from actor WHERE last_name LIKE '%LI%'
ORDER BY last_name, first_name;

SELECT country, country_id from country WHERE country IN ('Afghanistan', 'China', 'Bangladesh');

ALTER table actor
ADD COLUMN middle_name VARCHAR(50) after first_name;

ALTER table actor
MODIFY middle_name BLOB;

ALTER table actor
DROP middle_name;

SELECT last_name, COUNT(last_name) from actor GROUP BY last_name;

SELECT last_name, COUNT(last_name) from actor GROUP BY last_name HAVING COUNT(last_name) > 1;

SELECT * from actor WHERE first_name = 'GROUCHO';

UPDATE actor
SET first_name = 'HARPO' WHERE actor_id = 172;

UPDATE actor
SET first_name = 'MUCHO GROUCHO' WHERE actor_id = 172;

SHOW CREATE table address;

SHOW CREATE table staff;

SELECT first_name, last_name, address FROM staff
JOIN address ON (staff.address_id = address.address_id);

SELECT SUM(amount), first_name, last_name FROM payment
JOIN staff ON (staff.staff_id = payment.staff_id)
WHERE MONTH(payment.payment_date) = 08 AND YEAR(payment.payment_date) = 2005
GROUP BY staff.staff_id;

SELECT count(actor_id), title FROM film
INNER JOIN film_actor ON (film.film_id = film_actor.film_id)
GROUP BY film.film_id;

SELECT * FROM film 
WHERE title LIKE 'HUNCHBACK IMPOSSIBLE';

SELECT COUNT(film_id) FROM inventory
WHERE film_id = 439;

SELECT SUM(amount), first_name, last_name FROM customer
JOIN payment ON (payment.customer_id = customer.customer_id)
GROUP BY payment.customer_id
ORDER BY customer.last_name;





SELECT SUM(payment.amount), category.name FROM payment
JOIN rental on (payment.rental_id = rental.rental_id)
JOIN inventory on (rental.inventory_id = inventory.inventory_id)
JOIN film_category on (inventory.film_id = film_category.film_id)
JOIN category on (category.category_id = film_category.category_id)
GROUP BY category.name
ORDER BY SUM(payment.amount) DESC
LIMIT 5;