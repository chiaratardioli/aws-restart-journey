# Selecting Data from a Database

The database operations team has created a relational database named **world** containing three tables: **city**, **country**, and **countrylanguage**. 
Based on specific use cases defined in the lab exercise, I write a few queries using database operators and the **SELECT** statement.

## Task 1: Connect to the Command Host
I connect to the Command Host EC2 instance using the Session Manager tab and on terminal I type:
```bash
sudo su
cd /home/ec2-user/
mysql -u root --password='re:St@rt!9'
```

## Task 2: Query the world database
Here I query the world database using various **SELECT** statements and database operators.

```sql
SELECT * FROM world.country;                  -- list all rows and columns in the country table
SELECT COUNT(*) FROM world.country;           -- list the number of rows in the country table
SELECT COUNT(Population) FROM world.country;  -- count the number of rows that have a value in a specific column
SHOW COLUMNS FROM world.country;              -- list all columns in the country table

-- query specific columns in the world table
SELECT Name, Capital, Region, SurfaceArea, Population FROM world.country;

-- order the output based on a column
SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population FROM world.country ORDER BY Population;
-- order data in descending order
SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population FROM world.country ORDER BY Population DESC;

-- list all rows with a population greater than 50,000,000
SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population FROM world.country
WHERE Population > 50000000 ORDER BY Population DESC; 

-- construct a WHERE clause by using a number of conditions and operators
-- all rows with a population greater than 50,000,000 and all rows with a population less than 100,000,000
SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population FROM world.country
WHERE Population > 50000000 AND Population < 100000000 ORDER BY Population DESC;
```

## Challenge
Query the country table to return a set of records based on the following question: 
Which country in Southern Europe has a population greater than 50,000,000?

```sql
MariaDB [(none)]> SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population from world.country
WHERE Population > 50000000 AND Region = "Southern Europe";
+-------+---------+-----------------+--------------+------------+
| Name  | Capital | Region          | Surface Area | Population |
+-------+---------+-----------------+--------------+------------+
| Italy |    1464 | Southern Europe |    301316.00 |   57680000 |
+-------+---------+-----------------+--------------+------------+
1 row in set (0.000 sec)
```

## Conclusions
- I used the **SELECT** statement to query a database
- I used the **COUNT()** function
- I used the following operators to query a database:
  - **<**
  - **>**
  - **=**
  - **WHERE**
  - **ORDER BY**
  - **AND**

## Additional resources
- Country, city, and language data, Statistics Finland: The material was downloaded from Statistics Finland's interface service 
on February 4, 2022, with the [license CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.en). 
The original data source is available from [Statistics Finland](https://tilastokeskus.fi/tup/kvportaali/index_en.html).

- For more information about database functions and operators, see the following resources:
  - [SELECT statements](https://mariadb.com/kb/en/select/)
  - [Count function](https://mariadb.com/kb/en/count/)
  - [Order By](https://mariadb.com/kb/en/order-by/)
  - [Operators](https://mariadb.com/kb/en/operators/)
  - [Comparison Operators](https://mariadb.com/kb/en/comparison-operators/)
