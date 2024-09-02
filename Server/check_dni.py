from crud import crud
check_dni={0:"T",1:"R",2:"W",3:"A",4:"G",5:"M",6:"Y",7:"F",8:"P",9:"D",10:"X",11:"B",12:"N",13:"J",14:"Z",15:"S",16:"Q",17:"V",18:"H",19:"L",20:"C",21:"K",22:"E"}
class check:
    def __init__(self):
        self.__crud = crud()
        
    def check_dni(self,dni):
        if self.__crud.check_dni(dni)==None:
            print('x')
            letter = dni[-1]
            if len(dni) == 9 and check_dni.get(int(dni.replace(dni[-1],""))%23)!=None:
                number = int(dni.replace(dni[-1],""))%23
                if letter == check_dni.get(number):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False