import sqlite3
from sqlite3 import Error
import os
from DBCreate import *

path = "C:\Projects\Python\LootRoller\loot.db"
if not os.path.exists(path):
    create_lootDB()

con = sqlite3.connect(path)

c = con.cursor()

c.execute('''INSERT INTO WeaponTypes (WTypeid, Type, DamageType, DamageDie, Properties) VALUES ('1','Battleaxe', 'Slashing', '1d8','Versatile(1d10)')''')
con.commit()