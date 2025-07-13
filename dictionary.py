marks={
    "Priti":90,
    "Rohan":78,
    "Mohan":67,
    "Rishi":88
}

d={} #Empty Dictionary

print(marks,type(marks)) #class 'dict'
print(marks["Rishi"])

#DICTIONARY METHODS

#1. dict.items
print(marks.items())
print(type(marks.items())) #class 'dict_items'

#2. dict.keys & dict.values
print(marks.keys()) #dict_keys(['Priti', 'Rohan', 'Mohan', 'Rishi'])
print(marks.values()) #dict_values([90, 78, 67, 88])

#3. dict.update
marks.update({"Priti":89,"Millie":73})
print(marks)

#4. dict.get(...)
print(marks.get("Millie")) #gives the value of (...)

'''Difference between print(marks.get("Micky")) and print(marks["Micky"]) is:
the former will give None as output because key Micky is not present
but the later one will give KeyError'''

#5. dict.copy() : creates a shallow copy of the original 
marks2=marks.copy()
print(marks2)

#6. dict.clear() : Removes everything inside the dictionary
marks2.clear()
print(marks2)

#7. dict.pop(..) : Removes the pop value
marks.pop("Millie")
print(marks)