'''
Scenario

You already know how split() works. Now we want you to prove it.

Your task is to write your own function, which behaves almost exactly like the original split() method, i.e.:

    it should accept exactly one argument - a string;
    it should return a list of words created from the string, divided in the places where the string contains whitespaces;
    if the string is empty, the function should return an empty list;
    its name should be mysplit()

'''

def mysplit(myString):
    myList = []
    #check if the string is empty of characters
    if not myString or myString.isspace():
        return myList
    #strip leading and rear white spaces
    myString = myString.strip()
    oneString = ''
    for element in myString:
        if element.isspace():
            myList.append(oneString)
            del oneString
            oneString = ''
        oneString = oneString + element

    #add the last string
    myList.append(oneString)
    return myList

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
