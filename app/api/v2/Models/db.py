import psycopg2
import os
from .maindb import create_tables, drop_table_if_exists
from instance.config import app_config
env= os.environ['ENV']

url= app_config[env].DATABASE_URI

class DbConnection():
    """handles database connection to the app setting"""
     
    def connection(url):
        """creates conection to the database"""
        return psycopg2.connection(url)

    def db():
        """returns database connection object"""
        return connection(url)

    def create_tables():
        """function to create tables in the database"""
        conn=connection(url)
        cursor=conn.cursor()
        querries=create_queries()
        for query in queries:
            cursor.execute(query)
        conn.commit()

    def destroy_tables():
        """function to destroy tables in the database"""
        conn=connection(url)
        cursor=conn.cursor()
        deletions =create_queries()
        for deletion in deletions:
            cursor.execute(deletion)
        conn.commit()
