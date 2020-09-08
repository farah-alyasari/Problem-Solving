'''
Scenario

    Create a class representing a luxury watch;
    The class should allow you to hold a number of watches created in the watches_created class variable. The number could be fetched using a class method named get_number_of_watches_created;
    the class may allow you to create a watch with a dedicated engraving (text). As this is an extra option, the watch with the engraving should be created using an alternative constructor (a class method), as a regular __init__ method should not allow ordering engravings;
    the regular __init__ method should only increase the value of the appropriate class variable;

The text intended to be engraved should follow some restrictions:

    it should not be longer than 40 characters;
    it should consist of alphanumerical characters, so no space characters are allowed;
    if the text does not comply with restrictions, an exception should be raised;

before engraving the desired text, the text should be validated against restrictions using a dedicated static method.

    Create a watch with no engraving
    Create a watch with correct text for engraving
    Try to create a watch with incorrect text, like 'foo@baz.com'. Handle the exception
    After each watch is created, call class method to see if the counter variable was increased

'''

class luxury_watch:
    __number_of_watches_made = 0

    def __init__(self):
        luxury_watch.__number_of_watches_made += 1

    #hold the number of watches created
    @classmethod
    def get_number_of_watches_made(cls):
        return cls.__number_of_watches_made

    #checks the validity of the text before it's engraved
    @staticmethod
    def check_txt(text):
        if not text.isalnum() or not len(text) > 0 or not len(text) <= 40:
            return False
        return True

    #new luxuary watch with engraved text
    @classmethod
    def new_engraved_watch(cls, text):
        if luxury_watch.check_txt(text):
            _watch = cls()
            _watch.engraved = text
            return _watch
        else:
            raise ValueError("Text requirments are not met")

wtch1 = luxury_watch()
wtch2 = luxury_watch.new_engraved_watch("Hi")
print(luxury_watch.get_number_of_watches_made())

try:
    wtch3 = luxury_watch.new_engraved_watch("foo@baz.com")
except Exception as e:
    print(e)
