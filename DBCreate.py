def create_MoneyBagsDB():
  import sqlite3
  from sqlite3 import Error
  import os

  path = "C:\Projects\Python\LootRoller\loot.db"
  con = sqlite3.connect(path)

  cursor = con.cursor()

  #Create all of the Tables in the Database
  #Information Table
  cursor.execute('''CREATE TABLE IF NOT EXISTS `ApplicationInformation` (
    `Author` VARCHAR(64) NOT NULL,
    `AppVersion` FLOAT NOT NULL,
    `DatabaseVersion` FLOAT NOT NULL)''')

  #WeaponTypes
  cursor.execute('''CREATE TABLE IF NOT EXISTS `WeaponTypes` (
  `WTypeid` INT NOT NULL,
  `Type` VARCHAR(64) NOT NULL,
  `Class` VARCHAR(32) NOT NULL,
  `DamageType` VARCHAR(32) NULL,
  `DamageDie` VARCHAR(32) NULL,
  `Properties` VARCHAR(64) NULL,
  `Ranged` SMALLINT(2) NOT NULL,
  PRIMARY KEY (`WTypeid`))''')

  #MagicWeapons
  cursor.execute('''CREATE TABLE IF NOT EXISTS `MagicWeapons` (
  `Weapid` INT NOT NULL,
  `Name` VARCHAR(256) NOT NULL,
  `Description` VARCHAR(1024) NULL,
  `WeaponTypes_WTypeid` INT NOT NULL,
  `Rarity` VARCHAR(32) NOT NULL,
  `Attunement` TINYINT NOT NULL,
  `Sentience` TINYINT NOT NULL,
  `AttackBonus` SMALLINT(2) NULL,
  `DamageBonus` VARCHAR(64) NULL,
  `CustomProps` VARCHAR(64) NULL,
  `Link` VARCHAR(512) NULL,
  `Picture` BLOB NULL,
  PRIMARY KEY (`Weapid`),
  CONSTRAINT `fk_MagicWeapons_WeaponTypes`
    FOREIGN KEY (`WeaponTypes_WTypeid`)
    REFERENCES `WeaponTypes` (`WTypeid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)''')

  #ArmorTypes
  cursor.execute('''CREATE TABLE IF NOT EXISTS `ArmorTypes` (
  `ATypeid` INT NOT NULL,
  `Type` VARCHAR(64) NOT NULL,
  `Material` VARCHAR(32) NULL,
  `StrengthReq` TINYINT NOT NULL,
  `Strength` SMALLINT(2) NULL,
  `SteathVantage` VARCHAR(32) NULL,
  `Resistance` VARCHAR(64) NULL,
  PRIMARY KEY (`ATypeid`))''')

  #MagicArmor
  cursor.execute('''CREATE TABLE IF NOT EXISTS `MagicArmor` (
  `Armorid` INT NOT NULL,
  `Name` VARCHAR(256) NOT NULL,
  `Description` VARCHAR(1024) NULL,
  `ArmorTypes_ATypeid` INT NOT NULL,
  `Rarity` VARCHAR(32) NOT NULL,
  `Attunement` TINYINT NOT NULL,
  `CustomProps` VARCHAR(64) NULL,
  `Link` VARCHAR(512) NULL,
  `Picture` BLOB NULL,
  PRIMARY KEY (`Armorid`),
  CONSTRAINT `fk_MagicArmor_ArmorTypes1`
    FOREIGN KEY (`ArmorTypes_ATypeid`)
    REFERENCES `ArmorTypes` (`ATypeid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)''')

  #CastorItems
  cursor.execute('''CREATE TABLE IF NOT EXISTS `CastorItems` (
  `Castorid` INT NOT NULL,
  `Name` VARCHAR(256) NOT NULL,
  `Description` VARCHAR(1024) NULL,
  `Type` VARCHAR(64) NOT NULL,
  `Rarity` VARCHAR(32) NOT NULL,
  `Attunement` TINYINT NOT NULL,
  `Sentience` TINYINT NOT NULL,
  `AttackBonus` SMALLINT(2) NULL,
  `Damage Bonus` VARCHAR(64) NULL,
  `Link` VARCHAR(512) NULL,
  `Picture` BLOB NULL,
  PRIMARY KEY (`Castorid`))''')

  #WonderousItems
  cursor.execute('''CREATE TABLE IF NOT EXISTS `WonderousItems` (
  `WItemsid` INT NOT NULL,
  `Name` VARCHAR(256) NULL,
  `Type` VARCHAR(64) NULL,
  `Description` VARCHAR(1024) NULL,
  `Attunement` TINYINT NOT NULL,
  `Bonus` VARCHAR(64) NULL,
  `Rarity` VARCHAR(32) NOT NULL,
  `Link` VARCHAR(512) NULL,
  `Picture` BLOB NULL,
  PRIMARY KEY (`WItemsid`))''')

  #Spells
  cursor.execute('''CREATE TABLE IF NOT EXISTS `Spells` (
  `Spellid` INT NOT NULL,
  `Name` VARCHAR(256) NOT NULL,
  `Description` VARCHAR(1024) NOT NULL,
  `Level` SMALLINT(2) NOT NULL,
  `School` VARCHAR(64) NOT NULL,
  `Classes` VARCHAR(256) NOT NULL,
  `Components` VARCHAR(256) NOT NULL,
  `Link` VARCHAR(512) NULL,
  `Picture` BLOB NULL,
  PRIMARY KEY (`Spellid`))''')

  #ConsumableItems
  cursor.execute('''CREATE TABLE IF NOT EXISTS `ConsumableItems` (
  `Consumeid` INT NOT NULL,
  `Name` VARCHAR(256) NOT NULL,
  `Rarity` VARCHAR(32) NOT NULL,
  `Description` VARCHAR(1024) NULL,
  `Link` VARCHAR(512) NULL,
  `Picture` BLOB NULL,
  `Spells_Spellid` INT NULL,
  PRIMARY KEY (`Consumeid`),
  CONSTRAINT `fk_ConsumableItems_Spells1`
    FOREIGN KEY (`Spells_Spellid`)
    REFERENCES `Spells` (`Spellid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)''')

  #MasterRollingTable
  cursor.execute('''CREATE TABLE IF NOT EXISTS `RollingTable` (
  `RollableID` INT NOT NULL,
  `MagicWeapons_Weapid` INT NOT NULL,
  `MagicArmor_Armorid` INT NOT NULL,
  `CastorItems_Castorid` INT NOT NULL,
  `WonderousItems_WItemsid` INT NOT NULL,
  `ConsumableItems_Consumeid` INT NOT NULL,
  `TableName` TINYINT NOT NULL,
  PRIMARY KEY (`RollableID`),
  CONSTRAINT `fk_RollingTable_MagicWeapons1`
    FOREIGN KEY (`MagicWeapons_Weapid`)
    REFERENCES `MagicWeapons` (`Weapid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_RollingTable_MagicArmor1`
    FOREIGN KEY (`MagicArmor_Armorid`)
    REFERENCES `MagicArmor` (`Armorid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_RollingTable_CastorItems1`
    FOREIGN KEY (`CastorItems_Castorid`)
    REFERENCES `CastorItems` (`Castorid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_RollingTable_WonderousItems1`
    FOREIGN KEY (`WonderousItems_WItemsid`)
    REFERENCES `WonderousItems` (`WItemsid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_RollingTable_ConsumableItems1`
    FOREIGN KEY (`ConsumableItems_Consumeid`)
    REFERENCES `ConsumableItems` (`Consumeid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)''')


  #Set versioning info
  cursor.execute("INSERT INTO ApplicationInformation (Author, AppVersion, DatabaseVersion) VALUES ('Tyler A. Hinrichs', .01, .2)")


  #Adding Defaults to type tables
  #Simple Weapons
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('1','Club', 'Simple', 'Bludgeoning', '1d4','Light', 0)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('2','Dagger', 'Simple', 'Piercing', '1d4','Finesse, Light, Thrown(range10/60)', 0)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('3','Greatclub', 'Simple', 'Bludgeoning', '1d8','Two-Handed', 0)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('4','Handaxe', 'Simple', 'Slashing', '1d6','Light, Thrown(range 20/60', 0)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('5','Javelin', 'Simple', 'Piercing', '1d6','Thrown(range 30/120)', 0)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('6','Light Hammer', 'Simple', 'Bludgeoning', '1d4','Light, Thrown(range 20/60', 0)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('7','Mace', 'Simple', 'Bludgeoning', '1d6', ?, 0)''', (None,))
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('8','Quarterstaff', 'Simple', 'Bludgeoning', '1d6','Versatile(1d8)', 0)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('9','Sickle', 'Simple', 'Slashing', '1d4','Light', 0)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('10','Spear', 'Simple', 'Piercing', '1d6','Thrown (range 20/60), Versatile(1d8)', 0)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('11','Crossbow, Light', 'Simple', 'Piercing', '1d8','Ammunition(range 80/320, Loading, Two-handed', 1)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('12','Dart', 'Simple', 'Piercing', '1d4','Finesse, Thrown (range 20/60', 1)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('13','Shortbow', 'Simple', 'Piercing', '1d6','Ammunition (range 80/320), Two-handed', 1)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('14','Sling', 'Simple', 'Bludgeoning', '1d4','Ammunition (range 30/120)', 1)''')
  
  #Martial Weapons
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('15','Battleaxe', 'Martial', 'Slashing', '1d8','Versatile(1d10)', 0)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('16','Flail', 'Martial', 'Bludgeoning', '1d8', ?, 0)''', (None,))
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('17','Glaive', 'Martial', 'Slashing', '1d10','Heavy, Reach, Two-handed', 0)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('18','Greataxe', 'Martial', 'Slashing', '1d12','Heavy, Two-handed', 0)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('19','Halberd', 'Martial', 'Slashing', '1d10','Heavy, Reach, Two-handed', 0)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('20','Lance', 'Martial', 'Piercing', '1d12','Reach, Special', 0)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('21','Longsword', 'Martial', 'Slashing', '1d8','Versatile(1d10)', 0)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('22','Maul', 'Martial', 'Bludgeoning', '2d6','Heavy, Two-handed', 0)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('23','Morningstar', 'Martial', 'Piercing', '1d8', ?, 0)''', (None,))
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('24','Pike', 'Martial', 'Piercing', '1d10','Heavy, Reach, Two-handed', 0)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('25','Rapier', 'Martial', 'Piercing', '1d8','Finesse', 0)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('26','Scimitar', 'Martial', 'Slashing', '1d6','Finesse, Light', 0)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('27','Shortsword', 'Martial', 'Slashing', '1d6','Finesse, Light', 0)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('28','Trident', 'Martial', 'Piercing', '1d6','Thrown (range 20/60), Versatile (1d8)', 0)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('29','War Pick', 'Martial', 'Piercing', '1d8', ?, 0)''', (None,))
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('30','Warhammer', 'Martial', 'Bludgeoning', '1d8','Versatile(1d10)', 0)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('31','Whip', 'Martial', 'Slashing', '1d4','Finesse, Reach', 0)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('32','Blowgun', 'Martial', 'Piercing', '1','Ammunition (range 25/100), Loading', 1)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('33','Crossbow, Hand', 'Martial', 'Piercing', '1d6','Ammunition (range 30/120), Light, Loading', 0)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('34','Crossbow, Heavy', 'Martial', 'Piercing', '1d10','Ammunition (range 100/400), Heavy, Loading, Two-handed', 0)''')
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('35','Longbow', 'Martial', 'Piercing', '1d8','Ammunition (range 100/400), Heavy, Two-handed', 0)''')
  
  #Ammunition
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('36','Arrow', 'Ammunition', ?, ?, ?, 0)''', (None,None,None))
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('37','Blowgun Needle', 'Ammunition', ?, ?, ?, 0)''', (None,None,None))
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('38','Crossbow Bolt', 'Ammunition', ?, ?, ?, 0)''', (None,None,None))
  cursor.execute('''INSERT INTO WeaponTypes (WTypeid, Type, Class, DamageType, DamageDie, Properties, Ranged) VALUES ('39','Sling Bullets', 'Ammunition', ?, ?, ?, 0)''', (None,None,None))

  con.commit()