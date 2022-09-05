-- Show all databases
SHOW databases;

-- Select db to use
USE sakila -- Sakila is db used in book.

-- Get current time
SELECT now() from dual;

-- Show all character sets available
SHOW charset;

-- To define a database with a specific charset
CREATE DATABASE DUMMY_DB CHARACTER SET latin1;

-- To create just a column with a defined charset
VARCHAR(20) CHARACTER SET latin1;

-- Create table statement with enum
CREATE TABLE person (
    person_id SMALLINT UNSIGNED,
    fname VARCHAR(20),
    lname VARCHAR(20),
    eye_color ENUM('BR', 'BL', 'GR'), -- Merges checkconstraint into the data type definition.
    birth_date DATE,
    CONSTRAINT pk_person_id PRIMARY KEY (person_id)
);

ALTER TABLE person MODIFY person_id SMALLINT UNSIGNED AUTO_INCREMENT;

DESCRIBE TABLE_NAME; -- used to check the table definition.
