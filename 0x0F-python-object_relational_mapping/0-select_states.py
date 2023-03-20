#!/usr/bin/python3
"""
Lists all states from the database
It takes 3 arguments: mysql username, mysql password and database name
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    num_rows = cursor.execute("SELECT * FROM states ORDER BY states.id")
    for i in range(num_rows):
        print(cursor.fetchone())
