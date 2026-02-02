name = "beau" 
__name__= "main"
name1 = "beau"

print(type(name))
print(isinstance(name1, str))

age = float(25)
print(isinstance(age, float))
age = 8
age += 2
print(age)
age = 2
print(age)


def is_adult(age):
    if age >= 18:
        return True
    else:
        return False
    
def is_adult2(age):
    return age >= 18   
print(is_adult2(20))

def is_adult2(age):
    return True if age >= 18 else False


num1 = 2+3j
num2 = complex(2,3)
print(num2.real, num2.imag)

from enum import Enum
class State(Enum):
    NEW = 1
    IN_PROGRESS = 2
    COMPLETED = 3
print(State.NEW)
print(State.NEW.name)
print(State.NEW.value)
print(State(1).value)
print(State['NEW'].name)  
