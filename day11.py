# Declaring a Dictionary
student = {"name": "alex",
           "age": 21,
           "branch": "Machine learning"
           }
print("dictionary:",student)



person = {"name": "alex","age":25,"city":"mumbai"}
print(person.get("name"))
print(person.get("country"))

#keys()
person = {"name": "alex","age":25,"city":"mumbai"}
print(person.keys())

#values()
person = {"name": "alex","age":25,"city":"mumbai"}
print(person.values())

#items()
person = {"name": "alex","age":25,"city":"mumbai"}
print(person.items())

#update
person = {"name": "alex","age":25,"city":"mumbai"}
person.update({"age":26,"country":"india"})
print(person)

#pop()
person = {"name": "alex","age":25,"city":"mumbai"}
removed_value = person.pop("city")
print("removed value:", removed_value)
print(person)

#popitem
person = {"name": "alex","age":25,"city":"mumbai"}
last_item = person.popitem()
print("removed last item:", last_item)
print(person)

#copy
person = {"name": "alex","age":25,"city":"mumbai"}
person_copy = person.copy()
print("copy:", person_copy)


# setdefault()
person = {"name": "alex","age":25,"city":"mumbai"}
value = person.setdefault("country", "India")
print(person)
print(value)

#del()
person = {"name": "alex","age":25,"city":"mumbai"}
del person["age"]
print(person)
del person


#dsa questions
numbers = [1, 2, 2, 3, 3, 3, 4]

count_dict = {}  # empty dictionary

for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

print(count_dict)
max_key = max(count_dict,
              key = count_dict.get)
print(max_key)



dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

dict1.update(dict2)   # merge dict2 into dict1
print(dict1)





my_dict = {'a': 1, 'b': 2, 'c': 3}

# swap keys and values
inverted_dict = {value: key for key, 
                 value in my_dict.items()}

print(inverted_dict)
