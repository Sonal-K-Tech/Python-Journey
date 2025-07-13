a=(1,2,3,4)
print(type(a)) #<class 'tuple'>

b=(1)
print(type(b)) #<class 'int'>

b1=(1,)
print(type(b1)) #<class 'tuple'>

#TUPLE METHODS

#1. tuple.count
c=a.count(3) #counts the number of times the value is present in the tuple
print(c)

#2. tuple.index
c1=a.index(4) #tells the index of the element present 
print(c1)

#3. Concatenation: adding of two tuples
a1=(78, 9.09, 4)
a0=a+a1 #Joined a and a1
print(a0)

#4. Repetition
a2=a*3 #Multiple the number of times you want the elements to be repeated
print(a2)

#4. Membership: Checks if an element exists in the tuple
print(0 in a) #False
print(2 in a) #True

#5. Length
print(len(a2)) #number of elements

#6. Min and Max
print(min(a0))
print(max(a0))

#7. Slicing
print(a2[3:9])

#8. Unpacking: Separating all the elements of a tuple
p,q,r,s=a 
print(p,r,s,q)