import logging
import traceback

class DBConfig:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)
        if not hasattr(self, 'charset'):
            self.charset = 'utf8mb4'


def select(connect, sql, param=None, size=None):
    """
    Query data
    :param sql:
    :param param:
    :param size: Number of rows of data you want to return
    :return:
    """
    cur = connect.cursor()
    rows = None
    try:
        cur.execute(sql, param)
        if size:
            rows = cur.fetchmany(size)
        else:
            rows = cur.fetchall()
    except Exception as e:
        connect.rollback()
        logging.error(traceback.format_exc())
        logging.error("[sql]:{} [param]:{}".format(sql, param))
    finally:
        cur.close()
    return rows


def execute(connect, sql, param=None):
    """
    exec DML：INSERT、UPDATE、DELETE
    :param sql: dml sql
    :param param: string|list
    :return: Number of rows affected
    """
    cnt = 0
    try:
        cur = connect.cursor()
        cnt = cur.execute(sql, param)
        connect.commit()
    except Exception as e:
        connect.rollback()
        logging.error(traceback.format_exc())
        logging.error("[sql]:{} [param]:{}".format(sql, param))
    finally:
        cur.close()
    return cnt
