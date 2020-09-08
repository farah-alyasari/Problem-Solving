'''
Scenario

    Imagine you’ve been given a task to clean up the code of a system developed in Python – the code should be treated as legacy code;
    the system was created by a group of volunteers who worked with no clear “clean coding” rules;
    the system suffers from a problem: we don’t know in which order the classes are created, so it causes multiple dependency problems;
    your task is to prepare a metaclass that is responsible for:
        equipping all newly instantiated classes with time stamps, persisted in a class attribute named instantiation_time;
        equipping all newly instantiated classes with the get_instantiation_time() method. The method should return the value of the class attribute instantiation_time.

* The metaclass should have its own class variable (a list) that contains a list of the names of the classes instantiated by the metaclass (tip: append the class name in the __new__ method).

    Your metaclass should be used to create a few distinct legacy classes;
    create objects based on the classes;
    list the class names that are instantiated by your metaclass.
'''


#my solution
from datetime import datetime

def get_instantiation_time(self):
    self.time_stamp = datetime.now()
    return self.time_stamp

#a metaclass
class order_checker(type):
    #a list of the names of the classes instantiated by the metaclass
    names_list = list()

    def __new__(mcs, name, base, dictionary):
        #equipping all newly instantiated classes with the get_instantiation_time() method
        if 'get_instantiation_time' not in dictionary:
            dictionary['get_instantiation_time'] = get_instantiation_time

        #metaclasses instanitate classes not objects, here's the instanisation
        cls = super().__new__(mcs, name, base, dictionary)
        order_checker.names_list.append(name)

        #equipping all newly instantiated classes with time stamps, persisted in a class attribute named instantiation_time
        cls.instantiation_time = get_instantiation_time

        return cls

class Dog(metaclass=order_checker):
    pass

class Cat(metaclass=order_checker):
    pass

class Rabbit(metaclass=order_checker):
    pass

cat_1 = Cat()
rabbit_1 = Rabbit()
dog_2 = Dog()
rabbit_2 = Rabbit()
rabbit_3 = Rabbit()

print(cat_1.get_instantiation_time())
print(order_checker.names_list)
