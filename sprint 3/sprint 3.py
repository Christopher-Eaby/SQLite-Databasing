# -*- coding: utf-8 -*-
"""
       (`-()_.-=-.
       /66  ,  ,  \
     =(o_/=//_(   /======`
         ~"` ~"~~`
Created on Thu Jul 16 10:44:53 2020
@author: Chris
"""

import sqlite3 as sql #SQL for database
import random as ran
import pandas as pd

#creates a connection between the database and the python file
connection = sql.connect("sprintDB.db") 
#allows the python file to execute SQL queries
crsr = connection.cursor() 

def create_tables(): 
    crsr.execute('CREATE TABLE IF NOT EXISTS Chips (ID TEXT  PRIMARY KEY, Item TEXT, Price Real, Stock INTEGER)')
    crsr.execute('CREATE TABLE IF NOT EXISTS Cooldrinks (ID TEXT  PRIMARY KEY, Item TEXT, Price Real, Stock INTEGER)')
    crsr.execute('CREATE TABLE IF NOT EXISTS Chocolate (ID TEXT  PRIMARY KEY, Item TEXT, Price Real, Stock INTEGER)')
    crsr.execute('CREATE TABLE IF NOT EXISTS Pies (ID TEXT  PRIMARY KEY, Item TEXT, Price Real, Stock INTEGER)')
    crsr.execute('CREATE TABLE IF NOT EXISTS Fruit (ID TEXT  PRIMARY KEY, Item TEXT, Price Real, Stock INTEGER)')
    crsr.execute('CREATE TABLE IF NOT EXISTS Cupcakes (ID TEXT  PRIMARY KEY, Item TEXT, Price Real, Stock INTEGER)')
    crsr.execute('CREATE TABLE IF NOT EXISTS Veggies (ID TEXT  PRIMARY KEY, Item TEXT, Price Real, Stock INTEGER)')
create_tables()    
    
def data_entry(table, item, price, stock): 
    id1 = 'S'+ str(ran.randint(10, 100)) + 'T' + str(ran.randint(0,10)) 
    crsr.execute("INSERT INTO " + table + "(ID, Item, Price, Stock) VALUES(?, ?, ?, ?)", (id1 ,item, price, stock))  
    connection.commit() 
    
data = pd.read_csv(r'stock.csv')   
df = pd.DataFrame(data, columns= ['Type','Item','Price','Stock'])
for x in (df.index):
    data_entry(df['Type'][x], df['Item'][x], df['Price'][x], df['Stock'][x])

#function to create a new table if there isn't already one
#to store the rolls and a name for the rolls

def create_table(tablename):
     crsr.execute('CREATE TABLE IF NOT EXISTS ' + tablename +  '(ID TEXT  PRIMARY KEY, Item TEXT, Price Real, Stock INTEGER)')
#creating the tables if they don't already exist

neworold = input("Is it a new type of product or old ? (new/old)\n> ").lower()
if neworold == 'new':
    table = input("New name of table ?\n> ").lower()
    create_table(table)
    thing = input("What do you want to add ?\n> ")
    priceofthing = input("Whats the price ?\n> R")
    stockvalofthing = input("How much is avaiable ?\n> ")
    data_entry(table, thing, priceofthing, stockvalofthing)  
    print("Created the database and added the data.")
elif neworold == 'old':
    table1 = input("Where do you want to add an entry to ?\n> ")
    thing = input("What do you want to add ?\n> ")
    priceofthing = input("Whats the price ?\n> R")
    stockvalofthing = input("How much is avaiable ?\n> ")
    data_entry(table1, thing, priceofthing, stockvalofthing)
    print("Created the database and added the data.")
else:
    print('Exiting program, thank you for using.')
