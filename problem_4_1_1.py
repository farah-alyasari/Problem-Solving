#
''' object presistance
Scenario - part 1

Imagine you have been hired to help run a candy warehouse.
The task

    Your task is to write a code that will prepare a proposal of reduced prices for the candies whose total weight exceeds 300 units of weight (we don’t care whether those are kilograms or pounds)
    Your input is a list of dictionaries; each dictionary represents one type of candy. Each type of candy contains a key entitled 'weight', which should lead you to the total weight details of the given delicacy. The input is presented in the editor;
    Prepare a copy of the source list (this should be done with a one-liner) and then iterate over it to reduce the price of each delicacy by 20% if its weight exceeds the value of 300;
    Present an original list of candies and a list that contains the proposals;
    Check if your code works correctly when copying and modifying the candy item details.

Scenario - part 2

The previous task was a very easy one. Now let's rework the code a bit:

    introduce the Delicacy class to represent a generic delicacy. The objects of this class will replace the old school dictionaries. Suggested attribute names: name, price, weight;
    your class should implement the __str__() method to represent each object state;
    experiment with the copy.copy() and deepcopy.copy() methods to see the difference in how each method copies objects
'''
import copy

class Delicacy:
    def __init__(self,name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        return 'name: {}, price: {}, weight: {}'.format(self.name, self.price, self.weight)

d1 = Delicacy('Lolly Pop', 0.4, 133)
d2 = Delicacy('Licorice', 0.1, 251)
d3 = Delicacy('Chocoloate', 1, 601)
d4 = Delicacy('Sours', 0.01, 133)
d5 = Delicacy('Hard Candies', 0.3, 433)


warehouse = list()
warehouse.extend([d1,d2,d3,d4,d5])

print('Source list of candies')
for item in warehouse:
    print(item)

print('******************')
#deep copy warehouse
#shallow copy would use copy.copy(warehouse)
discounted_warehouse = copy.deepcopy(warehouse)

for item in discounted_warehouse:
    if(item.weight>300):
        item.price = item.price * 0.8
    print(item)
