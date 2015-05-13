# coding=utf-8
import codecs
import sys
import os
import zipfile
import cx_Oracle
import os.path
import time
from core.Router import Router
from core.ModuleExtractor import ModuleExtractor

USE_JYTHON = 0

TABLES_ONLY = 0

_CONN = None

DB_ENCODINGS = ('cp1250', 'iso8859_2', 'utf8')


class GetSchema():


    def init_db_conn(self,connection, user, password):
        """initializes database connection"""
        connect_string = connection
        username = user 
        passwd = password
        exec connect_string

        global _CONN
        if not _CONN:
            dbinfo = connect_string
            try:
                if USE_JYTHON:
                    dbinfo = 'JDBC: %s, user: %s' % (connect_string, username)
                    print('--%s' % (dbinfo))
                    _CONN = zxJDBC.connect(connect_string, username, passwd, 'oracle.jdbc.driver.OracleDriver')
                else:
                    dbinfo = 'db: %s@%s' % (username, connect_string)
                    print('--%s' % (dbinfo))
                    _CONN = cx_Oracle.connect(username, passwd, connect_string)
            except:
                ex = sys.exc_info()
                serr = 'Exception: %s: %s\n%s' % (ex[0], ex[1], dbinfo)
                print_err(serr)
                return None
        return _CONN


    def db_conn(self):
        """returns global database connection"""
        return _CONN 


