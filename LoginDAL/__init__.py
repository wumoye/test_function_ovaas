import logging

import azure.functions as func
from DBHelper.MySQLHelper.mysql_helper import MySQLHelper
from DBHelper.MySQLHelper.db_config import mysql_config,mysql_config_localhost

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.The function is LoginDAL.')

    logging.info(req.get_body())
    id = req.params.get('id')
    password = req.params.get('password')

    if not id or password:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            id = req_body.get('id')
            password = req_body.get('password')
            
    if id is None or password is None:
        return func.HttpResponse('[Failed]:id or password is empty!', status_code=211)
    
    db_config = mysql_config()
    sql_helper = MySQLHelper(db_config)
    
    sql = "select * from user where id=%s and password=%s"
    user_account = sql_helper.select(sql=sql, param=(id,password))
    logging.info(f"users is {user_account}")

    if len(user_account)==0:
        logging.info('[Failed]:id or password is false.')
        return func.HttpResponse('[Failed]:The result is 0 rows!', status_code=211)
    elif len(user_account) == 1:
        logging.info('[Success]:id and password is true.')
        return func.HttpResponse('[Success]:User exists.', status_code=200)


