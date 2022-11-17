# Data_Engineering_Capstone

This project uses all the knowledge adquired during the Data Engineer Professional Certificate offered by IBM and issued by Coursera. It is divided in 6 modules, described as follows:

## Module 1: MySQL and NoSQL

The objective of this module is to design a data platform that uses MySQL and MongoDB as databases for an e-commerce company.


### MySQL
In this section, a database with a single table is created. 

![createtable](https://user-images.githubusercontent.com/103103116/202383844-f9e417dc-4d41-42ba-ab1e-7117bfad6032.PNG)

Then, data gets imported using phpMyAdmin from a csv file. 

![importdata](https://user-images.githubusercontent.com/103103116/202384311-416c1509-a6c2-44bb-a70e-5cf232dbf603.PNG)

After creating an index, the table gets exported using a bash script into a sql file.

![exportdata](https://user-images.githubusercontent.com/103103116/202384024-7e7718cc-8418-4775-963e-deb166dad902.PNG)

### NoSQL
The company needs a product catalog, so MongoDB is chosen to store the catalog data. All the information comes from a json file provided by the owners, so the first step is to import it to a collection named "electronics"

![mongoimport](https://user-images.githubusercontent.com/103103116/202385299-e2e58496-3338-46b1-9c98-239568bd69ea.PNG)
