-- easy

SELECT * FROM CITY
WHERE COUNTRYCODE = "USA" AND POPULATION > 100000;

SELECT NAME FROM CITY
WHERE COUNTRYCODE ="USA" AND POPULATION > 120000;

SELECT * FROM CITY
WHERE ID =1661;

SELECT NAME FROM CITY
WHERE COUNTRYCODE = "JPN";

SELECT CITY, STATE FROM STATION;

SELECT DISTINCT CITY FROM STATION
WHERE MOD(ID, 2) = 0; 

-- # Find the difference between the total number of CITY entries
-- # in the table and the number of distinct CITY entries in the table.

SELECT (COUNT(CITY) - COUNT(DISTINCT(CITY))) FROM STATION;

-- # Query the two cities in STATION with the shortest and longest CITY names, 
-- # as well as their respective lengths (i.e.: number of characters in the name). 
-- # If there is more than one smallest or largest city, 
-- # choose the one that comes first when ordered alphabetically.


select city, length(city) from station
order by length(city) asc, city asc limit 1;

select city, length(city) from station
order by length(city) desc, city desc limit 1;

-- # Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. 
-- # Your result cannot contain duplicates.

SELECT DISTINCT(CITY) FROM STATION 
WHERE lower(SUBSTR(city,1,1)) IN ('a','e','i','o','u');

-- # last name this time
select distinct CITY from STATION 
where right(city,1) in ('a', 'e', 'i', 'o', 'u');

-- # BOTH 1st abd last are vowels
select DISTINCT CITY FROM STATION 
WHERE lower(SUBSTR(city,1,1)) IN ('a','e','i','o','u') AND right(city,1) in ('a', 'e', 'i', 'o', 'u');
