import sqlite3
from sqlite3 import Error
import os
from DBCreate import *

path = "C:\Projects\Python\LootRoller\loot.db"
if not os.path.exists(path):
    create_lootDB()

con = sqlite3.connect(path)

c = con.cursor()