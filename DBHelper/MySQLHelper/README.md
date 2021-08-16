# Python database helper
---
## Instructions for use


   **1. helper.select(sql,param=None,size=None)**
   
   *Method parameters:*
   
   * 1. sql: SQL statement for the query, the parameter uses %s as a placeholder
   * 2. param: SQL parameter
   * 3. size: the number of data items expected to be returned, if it is empty, all data will be returned, for example: return the first 10 items (size=10) 

   **Return result:** return the result of the SQL query


   **2. helper.execute(sql,param=None)**

   *Method parameters:*
   
   * 1. sql: SQL statement for the query, the parameter uses %s as a placeholder
   * 2. param: SQL parameter

   **Return result:** Return the number of rows affected by DML
```python
sql = 'DELETE TABLE user where id=1'
users = helper.execute(sql=sql)
```
---
## Example

```python
from dbhelper.mysql.mysqlhelper import MySQLHelper
import logging

dbconfg = {
    'host':'127.0.0.1',
    'port':3306,
    'username':'root',
    'password':'****',
    'db':'test',
    'charset':'utf8'
}
helper = MySQLHelper(dbconfg)

# Determine whether the table exists
logging.info(helper.table_is_exist('tablename'))

# Query without parameters
sql = "select * from user"
users = helper.select(sql=sql)
logging.info(users)

# Query the first 10 items without parameters
sql = "select * from user"
users = helper.select(sql=sql,size=10)
logging.info(users)

# Query with parameters
sql = "select * from user where id=%s"
users = helper.select(sql=sql,param=(1,))
logging.info(users)

# DML statement：INSERT UPDATE DELETE
sql = "delete from user where id=10"
# sql = "INSERT INTO user (username , password , email , sal) VALUES ('test','im fine','test@email.com',5000);"
users = helper.execute(sql=sql)
logging.info(users)
```