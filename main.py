import sqlite3
from sqlite3 import Error
import os
from DBCreate import *
import random

path = "C:\Projects\Python\LootRoller\loot.db"
if not os.path.exists(path):
    create_lootDB()

con = sqlite3.connect(path)

c = con.cursor()

roll = random.randint(1,39)
sql = "SELECT * FROM WeaponTypes WHERE WTypeid = " + str(roll)
print(sql)
gotten = c.execute(sql)
data = c.fetchall()
print(data)