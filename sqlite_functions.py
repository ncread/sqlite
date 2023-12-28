import sqlite3
from datetime import datetime


#################
###Functions

def connect_db(db_file):
    """Creates connection to db_file, or creates a new db file 
        if it doesn't already exist"""
    try:
        global con, cur 
        con = sqlite3.connect(db_file)
        print('Connection Successful.')
        cur = con.cursor()
    except sqlite3.Error as error:
        print(f'There was an sqlite3 connection error :{error}')

def create_table(sql_statement):
    """Creates a table given an input SQL query"""
    try:
        cur.execute(sql_statement)
        print('Table Creation Successful.')
    except sqlite3.Error as error:
        print(f'{error}.')

def get_db_entries(db):
    """Outputs all database entries from inputted db"""
    cur.execute(f'SELECT * FROM {db}')
    res = cur.fetchall()
    if res == []:
        print('Table is empty.')
    else:
        for row in res:
            print(row)

def add_entry_6param(params, table_name):
    """Inserts parameter values into database table. Specifically used
        for situations where there are 6 parameters"""
    try:
        cur.execute('INSERT INTO ', table_name, ' VALUES (?,?,?,?,?,?)', params)
        print('\n')
        print('Insertion successful.', end='\n')
    except sqlite3.Error as error:
        print(error)
