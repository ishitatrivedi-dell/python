# # student_info = {
# #     "name" : "John Doe",
# #     "course" : "Computer Science",
# #     "age" : 20,
# #     "address" : "123 Main St, Anytown, USA"
# # }

# # will not give error (variable can be used as key)
# student_info = {
#     "name" : "John Doe",
#     "course" : "Computer Science",
#     "5" : 20,
#     "7" : "123 Main St, Anytown, USA"
# }
#  print(student_info[5]) # will give the answer as 20
#  print(student_info.get("country", "india")) # it will give output as india 

# print(student_info.setdefault("country", "India")) 
# # this will add the key country with value india in the dictionary if it is not present and return the value of the key country if it is present in the dictionary

# print("country" in student_info) # will give output as True because country is present in the dictionary
# # key does not have any rules to get declared it can be anything 

# # empty dictionary can be created using the dict() constructor
# empty = dict()

# person = dict(name="Alice", age=30, city="New York")

# print(student_info)
# print(person)

# # will give error 
# a = dict(name = "Bob", 5 = "hello" , 6 = 6)

# # will still give error (variable cannot be used as key)
# a = dict(name = "Bob", "5" = "hello" , "6" = 6)


# print(a)


# ## explict type conversion 

# b = [("a", 1), ("b", 2), ("c", 3)]

# b = [(a, 1), (b, 2), (c, 3)]
# # these are varibales when we use them as keys it will give error because they are not defined
# # they are terated as vaibales therefore it will give error 
# ans = dict(b)

# print(ans)



info = {
    "name" : "Alice",
    "age" : 30,
    "city" : "New York"
}

for i , j in info.items():
    print(i, j)


arr = [1,23,4,5,6,7,8,9]

for i in arr : 
    print(i)

for i in range(len(arr)):
    print(arr[i])


print(list(student_info.keys())) 
print(student_info.keys())

