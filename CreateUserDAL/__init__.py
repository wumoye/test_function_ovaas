import logging

import azure.functions as func
from DBHelper.MySQLHelper.mysql_helper import MySQLHelper
from DBHelper.MySQLHelper.db_config import mysql_config,mysql_config_localhost
import datetime

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    id = req.params.get('id')
    password = req.params.get('password')
    email=req.params.get('email')

    if not id or not password or not email:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            id = req_body.get('id')
            password = req_body.get('password')
            email = req_body.get('email')
    
    db_config = mysql_config()
    sql_helper = MySQLHelper(db_config)

    create_datatime = str(datetime.datetime.now())
    update_datatime = str(datetime.datetime.now())

    sql = "insert into user (id,password,email,create_datatime,update_datatime) values(%s,%s,%s,%s,%s)"
    result = sql_helper.execute(sql=sql, param=(
        id, password, email, create_datatime, update_datatime))

    if result == 0:
        logging.info('inster id and password is false')
        return func.HttpResponse('Failed', status_code=210)
    else:
        logging.info('inster id and password is true')
        return func.HttpResponse('success', status_code=200)
