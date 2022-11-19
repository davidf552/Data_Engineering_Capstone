# Import libraries required for connecting to mysql
import mysql.connector

# Import libraries required for connecting to DB2
import ibm_db

# Connect to MySQL
connection = mysql.connector.connect(user='root', password='MTA2NjMtZGhmcmVp',host='127.0.0.1',database='sales')
cursor = connection.cursor()

# Connect to DB2
dsn_hostname = "2f3279a5-73d1-4859-88f0-a6c3e6b4b907.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud"
dsn_uid = <user>        # e.g. "abc12345"
dsn_pwd = <password>      # e.g. "7dBZ3wWt9XN6$o0J"
dsn_port = "30756"                # e.g. "50000" 
dsn_database = "bludb"            # i.e. "BLUDB"
dsn_driver = "{IBM DB2 ODBC DRIVER}" # i.e. "{IBM DB2 ODBC DRIVER}"           
dsn_protocol = "TCPIP"            # i.e. "TCPIP"
dsn_security = "SSL"              # i.e. "SSL"

#Create the dsn connection string
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd, dsn_security)

# create connection
conn = ibm_db.connect(dsn, "", "")
print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

# Find out the last rowid from DB2 data warehouse
# The function get_last_rowid must return the last rowid of the table sales_data on the IBM DB2 database.

def get_last_rowid():

    SQL="SELECT rowid FROM SALES_DATA ORDER BY rowid desc LIMIT 1"
    stmt = ibm_db.exec_immediate(conn, SQL)
    dictionary = ibm_db.fetch_assoc(stmt)
    result = dictionary["ROWID"]
    return result
    #tuple = ibm_db.fetch_tuple(stmt)
    pass


last_row_id = get_last_rowid()
print("Last row id on production datawarehouse = ", last_row_id)

# List out all records in MySQL database with rowid greater than the one on the Data warehouse
# The function get_latest_records must return a list of all records that have a rowid greater than the last_row_id in the sales_data table in the sales database on the MySQL staging data warehouse.

def get_latest_records(rowid):
    SQL = "SELECT * FROM sales_data WHERE rowid >= " + str(rowid)
    cursor.execute(SQL)  
    rows = cursor.fetchall()
    return rows
pass	

new_records = get_latest_records(last_row_id)

print("New rows on staging datawarehouse = ", len(new_records))

# Insert the additional records from MySQL into DB2 data warehouse.
# The function insert_records must insert all the records passed to it into the sales_data table in IBM DB2 database.

def insert_records(records):

    SQL = "INSERT INTO SALES_DATA(ROWID,PRODUCT_ID,PRICE,CUSTOMER_ID,QUANTITY,TIMESTAMP) VALUES(?,?,?,?,?,?);"
    stmt = ibm_db.prepare(conn, SQL)
    for row in records:
        row1=(row[0],row[1],0,row[2],row[3],0)
        ibm_db.execute(stmt, row1)
pass

insert_records(new_records)
print("New rows inserted into production datawarehouse = ", len(new_records))

# disconnect from mysql warehouse
connection.close()
# disconnect from DB2 data warehouse
ibm_db.close(conn)
# End of program
