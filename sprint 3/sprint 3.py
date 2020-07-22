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
import tkinter as tk #import for gui tkinter

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
# instantiates all the tables for the program 
    
def data_entry(table, item, price, stock): 
    id1 = 'S'+ str(ran.randint(10, 100)) + 'T' + str(ran.randint(0,10)) 
    crsr.execute("INSERT INTO " + table + "(ID, Item, Price, Stock) VALUES(?, ?, ?, ?)", (id1 ,item, price, stock))  
    connection.commit() 
    tk.messagebox.showinfo("Message", "Added to the database")
    
data = pd.read_csv(r'stock.csv')   
df = pd.DataFrame(data, columns= ['Type','Item','Price','Stock'])
'''
for x in (df.index):
    data_entry(df['Type'][x], df['Item'][x], df['Price'][x], df['Stock'][x])
'''
# function to create a new table if there isn't already one
# to store the rolls and a name for the rolls

def create_table(tablename):
     crsr.execute('CREATE TABLE IF NOT EXISTS ' + tablename +  '(ID TEXT  PRIMARY KEY, Item TEXT, Price Real, Stock INTEGER)')
# creating the tables if they don't already exist
     tk.messagebox.showinfo("Message", "Created a new table")
# function to create a new table

def cleartextfields():
    txt.delete("1.0","end")
    txt1.delete("1.0","end")
    txt2.delete("1.0","end")
    txt3.delete("1.0","end")
    tk.messagebox.showinfo("Message", "Cleared the textfields")
# function to clear the text fields
    
# creates the gui using tkinter frame manager
gui = tk.Tk()
# sets the title 
gui.title("Database manager")
# sets the size
gui.geometry("380x280")

lbl1 = tk.Label(gui, text = "Do you want to add into the database or create a new table? ", justify = tk.CENTER, padx = 30, pady = 10)
lbl1.grid(columnspan = 4)
# label explaining what to do in the program

# creates text field for data input
txt = tk.Text(gui, fg = "white", bg = "purple", height = 1, width = 15)
# griding for the text field
txt.grid(row = 1, column = 1)
lbl2 = tk.Label(gui, text = "Table name", justify = tk.CENTER, padx = 30, pady = 10)
# creates a label to show what the text field is for
lbl2.grid(row = 1, column = 0)
txt1 = tk.Text(gui, fg = "white", bg = "purple", height = 1, width = 15)
txt1.grid(row = 2, column = 1)
lbl3 = tk.Label(gui, text = "Item name", justify = tk.CENTER, padx = 30, pady = 10)
lbl3.grid(row = 2, column = 0)
txt2 = tk.Text(gui, fg = "white", bg = "purple", height = 1, width = 15)
txt2.grid(row = 3, column = 1)
lbl4 = tk.Label(gui, text = "Price", justify = tk.CENTER, padx = 30, pady = 10)
lbl4.grid(row = 3, column = 0)
txt3 = tk.Text(gui, fg = "white", bg = "purple", height = 1, width = 15)
txt3.grid(row = 4, column = 1)
lbl5 = tk.Label(gui, text = "Stock", justify = tk.CENTER, padx = 30, pady = 10)
lbl5.grid(row = 4, column = 0)
b1 = tk.Button(gui, text = "Add", height = 2, width = 13, command = lambda: data_entry(txt.get("1.0","end"), txt1.get("1.0","end"), txt2.get("1.0","end"), txt3.get("1.0","end")) )
b1.grid(row = 5, column = 1) 
# button to add to a table
b2 = tk.Button(gui, text = "Create new table", height = 2, width = 13, command = lambda: create_table(txt.get("1.0","end")))
# button to create a new table
b2.grid(row = 5, column = 0) 
b3 = tk.Button(gui, text = "Clear", height = 2, width = 13, command = lambda: cleartextfields())
# button to clear all of the text fields
b3.grid(row = 5, column = 2) 

#runs the gui
gui.mainloop()
