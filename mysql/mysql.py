#!/usr/bin/python2.7
""" 
    create a databse connetion within the init of the TestQuery class 
    and run two queries to return data.
"""
import MySQLdb

class TestQuery(object):
    """ a sample mysql test class """

    def __init__(self):
        """ instantiate the class """
        self.db = MySQLdb.connect(
            host='localhost',
            user='root',
            passwd='root',
        )
        self.db.autocommit(1) 
        self._get_users_sql = """SELECT 
                `%(table)s`.`Host`, 
                `%(table)s`.`User`, 
                `%(table)s`.`Password` 
            FROM `mysql`.`%(table)s`;""" % {'table': 'user'}
        self._get_table_stats_sql = """SELECT 
                `%(table)s`.TABLE_SCHEMA, 
                `%(table)s`.TABLE_NAME, 
                `%(table)s`.TABLE_ROWS, 
                `%(table)s`.DATA_LENGTH, 
                `%(table)s`.CREATE_TIME, 
                `%(table)s`.UPDATE_TIME 
            FROM `information_schema`.`%(table)s` 
                WHERE TABLE_SCHEMA = 'mysql';""" % {'table': 'TABLES'}


    def _execute_query(self, sql):
        """ execute a specifc sql statement and return all the results in 
            a list of dictionaries.
            Args:
                sql (str): sql statement
            Returns:
                None
        """
        _sql = sql
        cursor = self.db.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(_sql)
        for row in cursor.fetchall():
            print sorted(row.items())
        cursor.close()


    def run(self):
        """ run the private _execute_query method with two distinct sql
            queries.
        """
        self._execute_query(self._get_users_sql)
        self._execute_query(self._get_table_stats_sql)
        

if __name__ == '__main__':
    test_query = TestQuery()
    test_query.run()


