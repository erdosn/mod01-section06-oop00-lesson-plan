import sqlite3
import pandas as pd

class SqliteConnector(object):


    def __init__(self, filename=None):
        self.conn = sqlite3.Connection(filename)
        self.curs = self.conn.cursor()
    

    def list_tables(self):
        query = "select name from sqlite_master where type='table';"
        res = self.curs.execute(query).fetchall()
        table_names = [r[0] for r in res]
        return table_names

    
    def query_all(self, table_name=None):
        query = self.build_select_all_query(table_name=table_name)
        res = self.curs.execute(query).fetchall()
        return res
    

    def all_table_to_dataframe(self, table_name):
        query = self.build_select_all_query(table_name=table_name)
        df = pd.read_sql(query, self.conn)
        return df
    

    def build_select_all_query(self, table_name):
        return "select * from {}".format(table_name)

    
    def columns_from_table(self, columns=[], table_name=None):
        column_list = ",".join(columns)
        query = "select {} from {};".format(column_list, table_name)
        res = self.curs.execute(query).fetchall()
        return res


    def query_to_dataframe(self, columns=[], table_name=None):
        column_list = ",".join(columns)
        query = "select {} from {};".format(column_list, table_name)
        df = pd.read_sql(query, self.conn)
        return df

        