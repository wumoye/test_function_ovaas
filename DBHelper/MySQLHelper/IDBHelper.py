from abc import ABCMeta, abstractmethod

# An ABCMeta base class can be constructed through the ABCMeta module. The abstract base class cannot be instantiated. For example, dbhelper = DBHelper()
# And the method annotated by @abstractmethod must be overridden by subclasses

class DBHelper(metaclass=ABCMeta):
    @abstractmethod
    def init(self, db_config):
        """
        Initialize database connection
        :param db_config: Database connection object
        :return: True/False
        """
        pass

    @abstractmethod
    def table_is_exist(self, tablename):
        """
        Determine whether the table exists
        :param tablename:
        :return:
        """
        pass

    @abstractmethod
    def select(self, sql, param=None, size=None):
        """
        Query data
        :param sql:
        :param param:
        :param size: The number of data expected to be returned. If it is blank, all data will be returned
        :return:
        """
        pass

    @abstractmethod
    def execute(self, sql, param=None):
        """
        Execute DML statement：INSERT、UPDATE、DELETE
        :param sql:
        :param param:
        :return:
        """
        pass

    @abstractmethod
    def get_conn(self):
        """
        Get a connection
        :return:
        """
        pass

    @abstractmethod
    def close_conn(self):
        """
        Close connection
        :return:
        """
        pass
