import logging

import azure.functions as func
from DBHelper.MySQLHelper.mysql_helper import MySQLHelper
from DBHelper.MySQLHelper.db_config import mysql_config,mysql_config_localhost
import datetime

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # get params
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
    
    # connect to mysql
    db_config = mysql_config()
    sql_helper = MySQLHelper(db_config)

    create_datatime = str(datetime.datetime.now())
    update_datatime = str(datetime.datetime.now())

    # query user_account
    sql = "select id from user where id=%s"
    is_user_account=sql_helper.select(sql=sql,param=(id))
    logging.info(f'query user_account...')
    if len(is_user_account)!=0:
        logging.info('The user exists.')
        return func.HttpResponse('[Failed]: The user exists.',status_code=211)
    else:
        # create user_account
        sql = "insert into user (id,password,email,create_datatime,update_datatime) values(%s,%s,%s,%s,%s)"
        try:
            create_result = sql_helper.execute(sql=sql, param=(
                id, password, email, create_datatime, update_datatime))
            if create_result == 0:
                logging.info(f'[Failed]:Failed to create user {id}.')
                return func.HttpResponse(f'[Failed]: Failed to create user {id}.', status_code=210)
            else:
                logging.info(f'[Success]:User {id} created successfully.')
                return func.HttpResponse(f'[Success]:User {id} created successfully', status_code=200)
        except Exception as e:
            logging.info(f'[Error]:{e}')
            return func.HttpResponse('[Failed]: Failed to create user {id}.status_code is 212}', status_code=212)
