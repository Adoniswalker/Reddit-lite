#!/usr/bin/python

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def main():
    """
    Create a database connection cursor and returns it
    :return:
    """
    database = "../reddit_lite.db"

    # create a database connection
    conn = create_connection(database)
    if conn:
        return conn.cursor()


if __name__ == '__main__':
    main()
