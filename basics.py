# import sys
# a=[]
# print(sys.getrefcount(a))  # Returns the reference count of the object 'a'

# b=a
# print(sys.getrefcount(b))  # Reference count increases after assigning 'b' to '

# c=b
# print(sys.getrefcount(c))  # Reference count increases after assigning 'c' to 'b'  




# # GARBAGE COLLECTOR

# import gc
# print(gc.enable())  # Enable garbage collection
# print(gc.disable())  # Disable garbage collection
# print(gc.collect()) # Force garbage collection
# print(gc.get_stats())  # Get statistics about the collector
# print(gc.garbage)  # Get a list of all objects tracked by the collector that are unreachable but not yet collected


import gc

from numpy import number 

class Myobj:
    def __init__ (self,name):
        self.name = name
        print(f"the obj name is {self.name}")
    
    def __del__(self):
        print(f"{self.name} is being destroyed")

# THIS IS CALLED CIRCULAR REFERENCE 
obj1 = Myobj("obj1")
obj2 = Myobj("obj2")
obj1.ref = obj2
obj2.ref = obj1

# del obj1
# del obj2
# AFTER THIS BOTH THE OBJECTS WILL BE UNREACHABLE AND THESE WILL NOT BE GARBAGE COLLECTED
# SO WE HAVE TO DO IT MANUALLY

gc.collect()  # Force garbage collection to clean up circular references





#_______________GENERATOR___________________________


def my_generator(n):
    for i in range(n):
        yield i


for value in my_generator(5):
    print(value)
    if value >= 10:
        break