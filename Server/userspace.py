from db.db import User_MB_Management
from db.db import *
from db.table import *
cur = User_MB_Management()
class userspace:
    def Select_buisness(self,name,password):
        result = cur.Select_Enterprise(TABLE_USERS,name,password)
        return result[0][0]
    
    def Select_Backup(self,dni):
        result = []
        r = cur.Select_All_Backup(TABLE_BACKUPS,dni)
        for i in r:
            d_dict = dict(zip(COLUMNAME_BACKUPS,i))
            result.append(d_dict)
        return result
    
    def Delete_Backup_Table(self,dni):
        cur.Delete_User(TABLE_BACKUPS,dni)
        
    def Count_Backup_table(self,dni):
        result = cur.Count_Backup(TABLE_BACKUPS,dni)
        return int(result[0][0])
    
    def Select_Dni(self,name,password):
        result = cur.Select_Dni_Name_Password(TABLE_USERS,name,password)
        return result[0][0]
