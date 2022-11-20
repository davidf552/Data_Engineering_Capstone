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

In this section, a database with a single table is created: 

![createtable](https://user-images.githubusercontent.com/103103116/202383844-f9e417dc-4d41-42ba-ab1e-7117bfad6032.PNG)

Then, data gets imported using phpMyAdmin from a csv file:

![importdata](https://user-images.githubusercontent.com/103103116/202384311-416c1509-a6c2-44bb-a70e-5cf232dbf603.PNG)

After creating an index, the table gets exported using a bash script into a **[sql file.](salesdata.sql)**


[Return](#introduction)

## Module 2: NoSQL
The company needs a product catalog, so MongoDB is chosen to store the catalog data. All the information comes from a **[json file](catalog.json)** provided by the owners, so the first step is to import it to a collection named "electronics".

Then, an index on the field "type" will help in querying the data due to the amount of records in the collection.

![create-index](https://user-images.githubusercontent.com/103103116/202837002-42380205-d967-42b5-a30f-0372e73521f8.PNG)

Knowing the average of something is incredibly useful on an e-commerce business, so here is the average screen size of a product:

![mongo-query-mobiles2](https://user-images.githubusercontent.com/103103116/202837068-a5508517-6792-457c-acf1-f278ed628737.PNG)

Finally, some records are exported into a **[csv file](electronics.csv)** for future use using *mongoexport*. 

[Return](#introduction)
## Module 3: Data warehouse
The company retails download-only items like E-books, movies, songs, etc. The company has an international presence and customers from all over the world.

With that said, the company would like to create a data warehouse so that it can create reports like:
- Total sales per year per country.
- Total sales per month per category.
- Total sales per quarter per country.
- Total sales per category per country.


The warehouse will be designed according to the following initial diagram created on PgAdmin:
![softcartRelationships](https://user-images.githubusercontent.com/103103116/202838268-60f71c93-e1ef-4608-9dfd-5df056c14bd4.PNG)

The schema will then be exported into the file named ["staging.sql"](staging.sql):
![createschema](https://user-images.githubusercontent.com/103103116/202838516-02af1b59-629a-45df-a3e6-92e457d9754c.PNG)

[Return](#introduction)
## Module 4: Reporting dashboard
With the data warehouse successfully created, the company now requires a dashboard that shows the key metrics of the business. In this module, ***IBM db2*** and ***Cognos*** will be used to solve this problem.

First, data is imported to IBM db2 from a csv file:


![dataimport](https://user-images.githubusercontent.com/103103116/202838772-866dbebf-3eb6-4539-a5ae-867e7d132d95.PNG)

A data source is then created in order to link db2 with Cognos. After a successful connection, a simple dashboard is created with the following reports:

- Total monthly sales from 2020:


![linechart](https://user-images.githubusercontent.com/103103116/202838959-4e36cf1f-4a7d-4387-943a-6f3616024a0c.PNG)

- Total sales by category:


![piechart](https://user-images.githubusercontent.com/103103116/202838983-ce2befa9-c53f-4111-b347-3f550f394887.PNG)

- Quarterly sales of mobile phones:


![barchart](https://user-images.githubusercontent.com/103103116/202839037-7a25e585-35e8-4bb0-8e14-aac528d1f60d.PNG)

[Return](#introduction)
## Module 5: ETL and Apache Airflow
The data warehouse gets information from several sources, including the transactional OLTP database (MySQL). The OLTP database needs to be propagated to the warehouse on a frequent basis. This data movement can be updated using ETL processes. To connect Mysql and db2, a Python script called ["automation.py"](automation.py) will be used.


The script will automatically load yesterday's data from the production database into the warehouse.


The data platform includes a Big Data repository that is used for analytics using machine learning with Apache Spark. This big data repository gets data from several sources including the data warehouse and the web server log. As data from the web server is logged, it needs to be added to the big data system on a frequent basis, therefore making it an ideal process to automate using a data pipeline.


Using Apache Airflow, daily data from the web server log will be extracted, processed and stored in a format to prepare it for loading into the big data platform. The DAG will be called ["process_web_log".](process_web_log.py)


[Return](#introduction)
## Module 6: Apache Spark
The search terms from the e-commerce web server needs to be analyzed. This process will be run inside a **[Jupyter Notebook](Module6_Spark.ipynb)** against the web server csv file. A pre-trained sales forecasting model will be used to predict next year's sales as well.

![forecast](https://user-images.githubusercontent.com/103103116/202885316-1355ad8c-988d-4cb2-ba73-9e187cc02265.PNG)


[Return](#introduction)
