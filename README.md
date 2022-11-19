# Data_Engineering_Capstone

## Introduction

This project uses all the knowledge acquired during the Data Engineer Professional Certificate offered by IBM and issued by Coursera. 
The whole project is divided in 6 modules, described as follows:


1. Design a data platform that uses ***[MySQL](#module-1-mysql)*** as an OLTP database. 
2. Design a data platform that uses ***[MongoDB](#module-2-nosql)*** as a NoSQL database.
3. Design and implement a ***[data warehouse](#module-3-data-warehouse)*** and generate reports from the data.
4. Design a ***[reporting dashboard](#module-4-reporting-dashboard)*** that reflects the key metrics of the business.
5. Extract data from OLTP and NoSQL databases, transform, load it into the data warehouse and then create an ***[ETL.](#module-5-etl-and-apache-airflow)***
6. Create a ***[Spark](#module-6-apache-spark)*** connection to the data warehouse and then deploy a ***machine learning*** model.


## Module 1: MySQL 

In this section, a database with a single table is created. 

![createtable](https://user-images.githubusercontent.com/103103116/202383844-f9e417dc-4d41-42ba-ab1e-7117bfad6032.PNG)

Then, data gets imported using phpMyAdmin from a csv file. 

![importdata](https://user-images.githubusercontent.com/103103116/202384311-416c1509-a6c2-44bb-a70e-5cf232dbf603.PNG)

After creating an index, the table gets exported using a bash script into a sql file.

![exportdata](https://user-images.githubusercontent.com/103103116/202384024-7e7718cc-8418-4775-963e-deb166dad902.PNG)


[Return](#introduction)

## Module 2: NoSQL
The company needs a product catalog, so MongoDB is chosen to store the catalog data. All the information comes from a json file provided by the owners, so the first step is to import it to a collection named "electronics"

![mongoimport](https://user-images.githubusercontent.com/103103116/202385299-e2e58496-3338-46b1-9c98-239568bd69ea.PNG)

Then, an index on the field "type" will help in querying the data due to the amount of records in the collection.

![create-index](https://user-images.githubusercontent.com/103103116/202837002-42380205-d967-42b5-a30f-0372e73521f8.PNG)

Knowing the average of something is incredibly useful on an e-commerce business, so here is the average screen size of a product:

![mongo-query-mobiles2](https://user-images.githubusercontent.com/103103116/202837068-a5508517-6792-457c-acf1-f278ed628737.PNG)

Finally, some records are exported into a csv file for future use using *mongoexport* 

![mongoexport](https://user-images.githubusercontent.com/103103116/202837104-667a362a-dcf4-496f-8369-67ba92e5124f.PNG)


[Return](#introduction)
## Module 3: Data warehouse
The company retails download-only items like E-books, movies, songs, etc. The company has an international presence and customers from all over the world.

With that said, the company would like to create a data warehouse so that it can create reports like:
- Total sales per year per country.
- Total sales per month per category.
- Total sales per quarter per country.
- Total sales per category per country.


The warehouse will be designed according to the following initial diagram made using PgAdmin:
![softcartRelationships](https://user-images.githubusercontent.com/103103116/202838268-60f71c93-e1ef-4608-9dfd-5df056c14bd4.PNG)


[Return](#introduction)
## Module 4: Reporting dashboard


[Return](#introduction)
## Module 5: ETL and Apache Airflow


[Return](#introduction)
## Module 6: Apache Spark


[Return](#introduction)
