'''
Topic: Custom usage of special Python methods: dunders
Scenario

    Create a class representing a time interval;
    the class should implement its own method for addition, subtraction on time interval class objects;
    the class should implement its own method for multiplication of time interval class objects by an integer-type value;
    the __init__ method should be based on keywords to allow accurate and convenient object initialization, but limit it to hours, minutes, and seconds parameters;
    the __str__ method should return an HH:MM:SS string, where HH represents hours, MM represents minutes and SS represents the seconds attributes of the time interval object;
    check the argument type, and in case of a mismatch, raise a TypeError exception.
'''

class Time_Interval:

    def __init__(self, hrs=0, min=0, sec=0):
        self.hours = hrs
        self.minutes = min
        self.seconds = sec

    def __add__(self, other):
        if(not isinstance(self, Time_Interval) or not isinstance(other, Time_Interval)):
            raise ValueError("ValueError exception thrown")

        # calculate added time in seconds
        own = self.hours * 3600 + self.minutes * 60 + self.seconds
        the_other = other.hours * 3600 + other.minutes * 60 + other.seconds

        # form the return object properties
        new_time = own + the_other
        new_hours = new_time // 3600
        new_minutes = (new_time % 3600) // 60
        new_seconds = new_time % 60
        res = Time_Interval(hrs=new_hours,min=new_minutes, sec=new_seconds)
        return res

    def __sub__(self, other):
        if(not isinstance(self, Time_Interval) or not isinstance(other, Time_Interval)):
            raise ValueError("ValueError exception thrown")

        # calculate added time in seconds
        own = self.hours * 3600 + self.minutes * 60 + self.seconds
        the_other = other.hours * 3600 + other.minutes * 60 + other.seconds

        # form the return object properties
        new_time = own - the_other
        new_hours = new_time // 3600
        new_minutes = (new_time % 3600) // 60
        new_seconds = new_time % 60
        res = Time_Interval(hrs=new_hours,min=new_minutes, sec=new_seconds)
        return res

    def __mul__(self, num):
        if(not isinstance(self, Time_Interval) or not isinstance(num, int)):
            raise ValueError("ValueError exception thrown")
        new_hours = self.hours * num
        new_minutes = self.minutes * num
        new_seconds = self.seconds * num
        res = Time_Interval(hrs=new_hours, min=new_minutes, sec=new_seconds)
        return res

    def __str__(self):
        return "{}:{}:{}".format(self.hours, self.minutes, self.seconds)

ti1 = Time_Interval(21,58,50)
ti2 = Time_Interval(1,45,22)

print(ti1 * 2)
