from db.db import User_MB_Management
from db.db import *
from db.table import *
cur = User_MB_Management()
class crud:
    def All_Users(self):
        result = []
        all_users = cur.Select_All(TABLE_USERS)
        for i in all_users:
            d_dict = dict(zip(COLUMNAME_USERS,i))
            result.append(d_dict)
        return result
    
    def Create_Users(self,dni,name,rol,password,empresa):
        cur.Create_User(TABLE_USERS,dni,name,rol,password,empresa)
        
    def Delete_Users(self,dni):
        cur.Delete_User(TABLE_USERS,dni)
        
    def Edit_Users(self,id,name,password,empresa):
        cur.Update_User(TABLE_USERS,id,name,password,empresa)
    
    def Check_Rol(self,dni):
        result = cur.Select_Rol(TABLE_USERS,dni)
        return result[0][0]
    
    def check_dni(self,dni):
        result = cur.Select_Dni_User(TABLE_USERS,dni)
        return result
