from collections import Counter
import re
dict1 = {'a':2 , 'b': 5}
dict2 = {'a': 4, 'b': 7 , 'c': 3}

# This will not change the dict items you can use it to store it on another dict 
dict_final = dict1 | dict2
print(dict_final)
print(dict1)

# dict 1 is changed  
dict1 |= dict2
print(dict1)


def get_author(record: dict) -> list:
    match record:
        # This will return multiple authors
        case {"type": "book", "api": 2 , 'authors': [*names], **details}:
            return f"Book is {names}, details are : {details}" 
        
        case {"type": "book", "api": 1 , 'author': name , **details}:

            return f"Book is {name}, details are : {details}" 
        case {"type": "book"}:
            raise ValueError(f"Invalid book record {record!r}")
        
        case _:
            raise ValueError("value error")
    
    
b1 = dict(api=1, type="book", author="Gustavo fiang", publish_date=1998)
print(get_author(b1))

b2 = dict(api=2, type="book", authors="Marshal Eminem Isam".split(), publish_date=2019)
print(get_author(b2))


ct = Counter("Afdsgdsbsdewi02sdfsf")
print(ct)
ct.update("A Test") 
print(ct)
print(ct.most_common(5))
# -----------------------------------------
print("-----------------------------------")
words = re.findall(
    r"\w+", open("test.txt").read().lower()
)
freq_words = Counter(words).most_common()
print(freq_words)


l = ["test", "apple", "apple", "bacon", "pineapple"]
print(set(l))

# remove the duplicate values (BUT KEEP THE ORDER)
un_sorted_set = list(dict.fromkeys(l).keys())
print(un_sorted_set)

list2 = ['ali', 'roydel', 'milad', 'khormaee', 'test', 'apple']
list3 = ['ali', 'roydel', 'milad', 'khormaee', 'ps4', 'ps5']

# found = 0
#! Unoptimized way !!!!!!!!!!!!!!
# for n in list2:
#     if n in list3:
#         found += 1

#* Needs to be converted to set first.
found = len(set(list2) & set(list3))
print(found)


d1 = dict(a=2, b=2, c=6)
d2 = dict(a=2, b=5, c=6 , g=2)

d3 = {"a": 2, "b":2 , "f": 5}
# for key , value in d1.items():
#     print(key, value)

#? will print same keys in 2 dicts
print(d1.keys() & d2.keys())

print(d1.keys() & d3)

# you can even merge 2 dicts () but only the keys will remain no value sadly
d1 = d1.keys() | d3
print(d1)