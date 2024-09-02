import mariadb
import sys
from db.confing_db import *
class User_MB_Management:
    def Connect_db(self):
        try:
            self.__conn = mariadb.connect(user=USER,password =PASSWORD,
                                   host=HOST,port =PORT,
                                   database=DATABASE)
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
        return self.__conn.cursor()
        
    def Select_User_Login(self,table,name,password):
        db = self.Connect_db()
        sql = 'SELECT * FROM t WHERE Name = %s AND Password = %s'.replace('t',table)
        db.execute(sql,(name, password,))
        result = db.fetchone()
        self.Close_Connection()
        return result
    
    def Select_All(self,table):
        db = self.Connect_db()
        sql = 'SELECT * FROM t' .replace('t',table)
        db.execute(sql)
        result = db.fetchall()
        self.Close_Connection()
        return result
    
    def Create_User(self,table,dni,name,rol,password,empresa):
        db = self.Connect_db()
        sql = 'INSERT INTO t (Dni,Name,Rol,Password,Empresa) Values (%s, %s, %s, %s, %s)'.replace('t',table)
        val = (dni,name,rol,password,empresa)
        db.execute(sql,val)
        self.__conn.commit()
        self.Close_Connection()
    
    def Delete_User(self,table,dni):
        db = self.Connect_db()
        sql = "DELETE FROM t WHERE Dni = %s".replace('t',table)
        db.execute(sql,(dni,))
        self.__conn.commit()
        self.Close_Connection()

    def Update_User(self,table,id,name,password,empresa):
        db = self.Connect_db()
        sql = "UPDATE t SET Name = %s, Password = %s, Empresa = %s Where Id  = %s".replace('t',table)
        data = (name,password,empresa,id)
        db.execute(sql,data)
        self.__conn.commit()
        self.Close_Connection()
    
    def Select_All_Backup(self,table,dni):
        db = self.Connect_db()
        sql = 'SELECT * FROM t WHERE dni =%s' .replace('t',table)
        db.execute(sql,(dni,))
        result = db.fetchall()
        self.Close_Connection()
        return result
    
    def Select_Enterprise(self,table,name,password):
        db = self.Connect_db()
        sql = "SELECT Empresa FROM t WHERE Name =%s AND Password=%s".replace('t',table)
        db.execute(sql,(name,password,))
        result = db.fetchall()
        self.Close_Connection()
        return result
    
    def Select_Dni_Password(self,table,password):
        db = self.Connect_db()
        sql = "SELECT Dni FROM t WHERE Password=%s".replace('t',table)
        db.execute(sql,(password,))
        result = db.fetchall()
        self.Close_Connection()
        return result
    
    def Select_Dni_Name_Password(self,table,name,password):
        db = self.Connect_db()
        sql = "SELECT Dni FROM t WHERE Name=%s AND Password=%s".replace('t',table)
        db.execute(sql,(name,password,))
        result = db.fetchall()
        self.Close_Connection()
        return result
        
    def Select_Dni_User(self,table,dni):
        db = self.Connect_db()
        sql = "SELECT Dni FROM t WHERE Dni=%s".replace('t',table)
        db.execute(sql,(dni,))
        result = db.fetchone()
        self.Close_Connection()
        return result
    
    def Count_Backup(self,table,dni):
        db = self.Connect_db()
        sql ="SELECT COUNT(DNI) FROM t WHERE Dni=%s".replace('t',table)
        db.execute(sql,(dni,))
        result = db.fetchall()
        self.Close_Connection()
        return result
    
    def Select_Rol(self,table,dni):
        db = self.Connect_db()
        sql ="SELECT ROL FROM t WHERE Dni=%s".replace('t',table)
        db.execute(sql,(dni,))
        result = db.fetchall()
        self.Close_Connection()
        return result 
           
    def Close_Connection(self):
        self.__conn.close()