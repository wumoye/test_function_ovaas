import logging
import pymysql,pymysql.cursors
import traceback
from DBHelper.MySQLHelper.IDBHelper import DBHelper
from DBHelper.MySQLHelper.dbutils import select, execute, DBConfig


class MySQLHelper(DBHelper):
    """
    MySQLHelper
    """
    _connect = None

    def __init__(self,db_config):
        """
        Construnctor for MySQLHelper
        """
       
        self.init(db_config)

    def init(self, config):
    
        # Construct connection string
        try:
            self.db_config = DBConfig(config)
            self._connect = pymysql.Connect(
                host=str(self.db_config.host),
                port=self.db_config.port,
                user=str(self.db_config.user),
                passwd=str(self.db_config.password),
                database=str(self.db_config.database),
                ssl=self.db_config.ssl,
            )
            logging.info(" Connected to MySQL database [ {db} ]...".format(
                db=self.db_config.database))
            return True
        except Exception as e:
            logging.error(
                " Connect MySQL exception : \n{e}\n".format(e=str(e)))
            return False
            

    def get_conn(self):
        if self._connect:
            return self._connect
        else:
            self.init()
            return self._connect

    # Cleanup
    def close_conn(self):
        if self._connect:
            self._connect.close()
            logging.info(" MySQL database [ {db} ] connection closed....".format(
                db=self.db_config.db))


    def table_is_exist(self, table_name):
            """
            Check table is exist
            :param tablename:
            :return:
            """
            sql = "SHOW TABLES LIKE '{table_name}'".format(table_name=table_name)
            rows = self.select(sql=sql)
            if len(rows) >= 1:
                return True
            else:
                return False


    def select(self, sql, param=None , size=None):
        """
        Query data
        :param sql:
        :param param:
        :param size: Number of rows of data you want to return
        :return:
        """
        cur = self._connect.cursor(cursor=pymysql.cursors.DictCursor)
        rows = None
        try:
            cur.execute(sql, param)
            if size:
                rows = cur.fetchmany(size)
            else:
                rows = cur.fetchall()
        except Exception as e:
            self._connect.rollback()
            logging.error(traceback.format_exc())
            logging.error("[sql]:{} [param]:{}".format(sql, param))
        cur.close()
        return rows

    def execute(self,sql, param=None):
        """
        exec DML：INSERT、UPDATE、DELETE
        :param sql: dml sql
        :param param: string|list
        :return: Number of rows affected
        """
        return execute(self._connect, sql, param)