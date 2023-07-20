class TypeCheck:
    
    """(descripter) Checks whether the type to be evaluated matches the required one."""
    
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if(isinstance(value, instance.__annotations__[self.name])):
            instance.__dict__[self.name] = value
        else:
            raise TypeError(f'this "{value}" is not appropriate for this "{self.name}" variable because, it is of `{instance.__annotations__[self.name].__name__}` type ')

class Person:
    
    """A class of people"""
    
    name:str
    age:int
    email:str
    
    name = TypeCheck()
    age = TypeCheck()
    email = TypeCheck()

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

try:
    person1 = Person('Poxos', 'Hello', 'poxos@poxosyan@gmail.com')
except TypeError as err:
    print(str(err))
try:
    person2 = Person('Poxos', 23, 'poxos@poxosyan@gmail.com')
except TypeError as err:
    print(str(err))
try:
    person3 = Person(True, 'Hello', 'poxos@poxosyan@gmail.com')
except TypeError as err:
    print(str(err))

