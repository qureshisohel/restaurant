import csv
import sqlite3
# Connecting to the geeks database
connection = sqlite3.connect('d1.db')
 
# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()

# Table Definition
create_table = '''CREATE TABLE IF NOT EXISTS restaurants_small (
    id INTEGER,
    name TEXT,
    location TEXT,
    items TEXT,
    lat_long TEXT,
    full_details TEXT
);
'''
 
# Creating the table into our
# database
cursor.execute(create_table)
 
# Opening the person-records.csv file
file = open('restaurants_small.csv')
 
# Reading the contents of the
# person-records.csv file
contents = csv.reader(file)
 
# SQL query to insert data into the
# person table
insert_records = "INSERT INTO restaurants_small(id,name,location,items,lat_long,full_details) VALUES(?,?,?,?,?,?)"
 
# Importing the contents of the file
# into our person table
cursor.executemany(insert_records, contents)
 
# SQL query to retrieve all data from
# the person table To verify that the
# data of the csv file has been successfully
# inserted into the table
select_all = "SELECT * FROM restaurants_small"
rows = cursor.execute(select_all).fetchall()
 
# Output to the console screen
for r in rows:
    print(r)
 
# Committing the changes
connection.commit()
 
# closing the database connection
connection.close()
"""
import csv
from search_app.models import Dish

with open('restaurants_small.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dish = Dish(name=row['<actual_column_name_for_dish_name>'], description=row['<actual_column_name_for_dish_description>'])
        dish.save()

        """