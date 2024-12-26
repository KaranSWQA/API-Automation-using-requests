import configparser
import mysql.connector
from mysql.connector import Error

def getConfig():
    config = configparser.ConfigParser()
    config.read('Utilities/properties.ini')
    return config

connect_config={'user':getConfig()['SQL']['user'],'password':getConfig()['SQL']['password'],'host':getConfig()['SQL']['host'],'database':getConfig()['SQL']['database']}
def getPassword():
    return "Apr@1404"

def getConnection():
    try:
        conn = mysql.connector.connect(**connect_config)  # authenticate the user
        if conn.is_connected():
            print("Connection Successful")
            return conn
    except Error as e:
        print(e)

def getQuery(query):
    conn=getConnection()
    cursor=conn.cursor()
    cursor.execute(query)
    row=cursor.fetchone()
    conn.close()
    return row
