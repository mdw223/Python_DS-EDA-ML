
class Student:
    def __init__(self, name: str = '', id: str = '0000000'):
        self.__name: str  = name
        self.__id: str = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, sname) -> None:
        self.__name = sname.upper()

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, studID)-> None:
        if len(studID) <= 7:
            self.__id = studID
        else: 
            self.__id = studID[-7:]
            
    @name.deleter
    def name(self):
        print(f'{self.__name} is deleted.')
        del self.__name



cs_student1 = Student('Joe Schmoe')
cs_student1.id = '3920244'
print('ID: ', cs_student1.id)
print('Name: ', cs_student1.name)
cs_student1.id = '0001234567'
print('ID: ', cs_student1.id)
del cs_student1.name

#print(cs_student1.name)

print(cs_student1.__dict__)