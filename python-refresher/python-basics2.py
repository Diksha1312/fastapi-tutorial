"""lists in python - collection of data (my_list = [1, "Harry", 3.14]), 
indexing starts at 0 and index -1 is the last item, index slicing[x:y] from x to y-1,
*** functions for lists:
.append() to add an item, 
remove() to remove an item, 
sort() to sort the list,
reverse() to reverse the list, 
len() to get the length of the list, 
insert() to insert an item at a specific index,
pop() to remove the last item, 
clear() to remove all items, 
copy() to copy the list
"""


"""sets and tuoples in python -
sets - unordered collection of unique items (my_set = {1, 2, 3}),
tuples - ordered collection of items (my_tuple = (1, 2, 3)),
tuples are immutable, sets are mutable
*** functions for sets:
.add() to add an item,
.remove() to remove an item,
.clear() to remove all items,
.union() to combine two sets,
.intersection() to get common items,
.difference() to get items in one set but not the other,
.isdisjoint() to check if two sets have no items in common,
.issubset() to check if one set is a subset of another,
.issuperset() to check if one set is a superset of another,
.copy() to copy the set,
.discard() to remove an item without raising an error if it doesn't exist,
.pop() to remove and return an arbitrary item,
.update() to add items from another set or iterable,
.symmetric_difference() to get items that are in either set but not both,
*** functions for tuples:
.count() to count occurrences of an item,
.index() to find the index of an item,
.slicing to get a sub-tuple (my_tuple[1:3] gets items at index 1 and 2),
len() to get the length of the tuple,
concatenation (+) to combine tuples (my_tuple1 + my_tuple2),
repetition (*) to repeat a tuple (my_tuple * 2),
unpacking to assign tuple items to variables (a, b, c = my_tuple),"""

animals = ["dog", "cat", "tiger", "lion", "elephant"]
print("Animals list:", animals)
animals.pop(2)
print("Animals after deletion:", animals)
animals.append("giraffe")
print("Animals after adding giraffe:", animals)
animals.pop(0)
print("Animals after removing first animal:", animals)
print("First 3 animals:", animals[:3])

""" dictionaries in python - collection of key-value pairs (my_dict = {"name": "Harry", "age": 30}),
*** functions for dictionaries:
.keys() to get all keys,
.values() to get all values,
.items() to get all key-value pairs,
.get() to get a value by key,
.update() to update or add key-value pairs,
.pop() to remove a key-value pair,
.clear() to remove all key-value pairs,
.copy() to copy the dictionary,     
.get() to retrieve a value by key,
len() to get the number of key-value pairs,
del to delete a key-value pair,
"""
my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}
for key,value in my_vehicle.items():
    print(f"{key}: {value}")
vehicle2 = my_vehicle.copy()
vehicle2["number_of_tires"] = 4
del vehicle2["mileage"]
for key,value in vehicle2.items():
    print(f"{key}")
