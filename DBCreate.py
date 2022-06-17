def create_lootDB():
  import sqlite3
  from sqlite3 import Error
  import os

  path = "C:\Projects\Python\LootRoller\loot.db"
  con = sqlite3.connect(path)

  c = con.cursor()

  #Create all of the Tables in the Database
  #WeaponTypes
  c.execute('''CREATE TABLE IF NOT EXISTS `WeaponTypes` (
  `WTypeid` INT NOT NULL,
  `Type` VARCHAR(128) NOT NULL,
  `DamageType` VARCHAR(24) NULL,
  `DamageDie` VARCHAR(24) NULL,
  `Properties` VARCHAR(48) NULL,
  PRIMARY KEY (`WTypeid`))''')

  #MagicWeapons
  c.execute('''CREATE TABLE IF NOT EXISTS `MagicWeapons` (
  `Weapid` INT NOT NULL,
  `Name` VARCHAR(256) NOT NULL,
  `Description` VARCHAR(1024) NULL,
  `WeaponTypes_WTypeid` INT NOT NULL,
  `Rarity` VARCHAR(24) NOT NULL,
  `Attunement` TINYINT NOT NULL,
  `Sentience` TINYINT NOT NULL,
  `AttackBonus` SMALLINT(2) NULL,
  `DamageBonus` VARCHAR(45) NULL,
  `Link` VARCHAR(512) NULL,
  `Picture` BLOB NULL,
  PRIMARY KEY (`Weapid`),
  CONSTRAINT `fk_MagicWeapons_WeaponTypes`
    FOREIGN KEY (`WeaponTypes_WTypeid`)
    REFERENCES `WeaponTypes` (`WTypeid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)''')

  #ArmorTypes
  c.execute('''CREATE TABLE IF NOT EXISTS `ArmorTypes` (
  `ATypeid` INT NOT NULL,
  `Type` VARCHAR(45) NOT NULL,
  `Material` VARCHAR(45) NULL,
  `StrengthReq` TINYINT NOT NULL,
  `Strength` SMALLINT(2) NULL,
  `SteathVantage` VARCHAR(45) NULL,
  `Resistance` VARCHAR(45) NULL,
  PRIMARY KEY (`ATypeid`))''')

  #MagicArmor
  c.execute('''CREATE TABLE IF NOT EXISTS `MagicArmor` (
  `Armorid` INT NOT NULL,
  `Name` VARCHAR(256) NOT NULL,
  `Description` VARCHAR(1024) NULL,
  `ArmorTypes_ATypeid` INT NOT NULL,
  `Rarity` VARCHAR(24) NOT NULL,
  `Attunement` TINYINT NOT NULL,
  `Link` VARCHAR(512) NULL,
  `Picture` BLOB NULL,
  PRIMARY KEY (`Armorid`),
  CONSTRAINT `fk_MagicArmor_ArmorTypes1`
    FOREIGN KEY (`ArmorTypes_ATypeid`)
    REFERENCES `ArmorTypes` (`ATypeid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)''')

  #CastorItems
  c.execute('''CREATE TABLE IF NOT EXISTS `CastorItems` (
  `Castorid` INT NOT NULL,
  `Name` VARCHAR(256) NOT NULL,
  `Description` VARCHAR(1024) NULL,
  `Type` VARCHAR(45) NOT NULL,
  `Rarity` VARCHAR(24) NOT NULL,
  `Attunement` TINYINT NOT NULL,
  `Sentience` TINYINT NOT NULL,
  `AttackBonus` SMALLINT(2) NULL,
  `Damage Bonus` VARCHAR(45) NULL,
  `Link` VARCHAR(512) NULL,
  `Picture` BLOB NULL,
  PRIMARY KEY (`Castorid`))''')

  #WonderousItems
  c.execute('''CREATE TABLE IF NOT EXISTS `WonderousItems` (
  `WItemsid` INT NOT NULL,
  `Name` VARCHAR(256) NULL,
  `Type` VARCHAR(45) NULL,
  `Description` VARCHAR(1024) NULL,
  `Attunement` TINYINT NOT NULL,
  `Bonus` VARCHAR(45) NULL,
  `Rarity` VARCHAR(24) NOT NULL,
  `Link` VARCHAR(512) NULL,
  `Picture` BLOB NULL,
  PRIMARY KEY (`WItemsid`))''')

  #Spells
  c.execute('''CREATE TABLE IF NOT EXISTS `Spells` (
  `Spellid` INT NOT NULL,
  `Name` VARCHAR(256) NOT NULL,
  `Description` VARCHAR(1024) NOT NULL,
  `Level` SMALLINT(2) NOT NULL,
  `School` VARCHAR(45) NOT NULL,
  `Classes` VARCHAR(256) NOT NULL,
  `Components` VARCHAR(256) NOT NULL,
  `Link` VARCHAR(512) NULL,
  `Picture` BLOB NULL,
  PRIMARY KEY (`Spellid`))''')

  #ConsumableItems
  c.execute('''CREATE TABLE IF NOT EXISTS `ConsumableItems` (
  `Consumeid` INT NOT NULL,
  `Name` VARCHAR(256) NOT NULL,
  `Rarity` VARCHAR(24) NOT NULL,
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
  c.execute('''CREATE TABLE IF NOT EXISTS `RollingTable` (
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

