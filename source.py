class TypeCheck:
    
    """(descripter) Checks whether the type to be evaluated matches the required one."""
    
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if( 
            isinstance(value, instance.__annotations__[self.name][0]) or\
            isinstance(value, instance.__annotations__[self.name][1])\
        ):
            instance.__dict__[self.name] = value
        else:
            if (\
                    instance.__annotations__[self.name][0].__name__ == \
                    instance.__annotations__[self.name][0].__name__
                ):
                raise ValueError(f'this "{value}" is not appropriate for this "{self.name}" variable because, it is of `{instance.__annotations__[self.name][1].__name__}` type ')
            else:
                raise ValueError(f'this "{value}" is not appropriate for this "{self.name}" variable because, it is of `{instance.__annotations__[self.name][0].__name__} or {instance.__annotations__[self.name][1].__name__}` type ')


class Person:
    
    """A class of people"""
    
    age:(int, int)
    height:(int, int) 
    name:(str, str)
    tags:(list, tuple)
    favorite_foods:(list, tuple)

    age = TypeCheck()
    height = TypeCheck()
    name = TypeCheck()
    tags = TypeCheck()
    favorite_foods = TypeCheck()



    def __init__(self, age, height, name, tags, favorite_foods):
        self.age = age
        self.height = height
        self.name = name
        self.tags = tags
        self.favorite_foods = favorite_foods
try:
    person1 = Person(22, 10, True, [1, 2, 3], ['1', '2'])
except ValueError as err:
    print(str(err))
try:
    person2 = Person(22, 10, "ddd", False, ['1', '2'])
except ValueError as err:
    print(str(err))
try:
    person3 = Person("Hello", 10, "ddd", (1, 2), ['1', '2'])
except ValueError as err:
    print(str(err))

