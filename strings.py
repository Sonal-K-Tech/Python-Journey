a='Sonal' #Single Quoted String 
b="IOT" #Double Quoted String 
c='''13031424018''' #Triple Quoted String, used to store multiple lines

#INDEX IN STRING 
#  S  O  N  A  L => LENGTH = 5
#  0  1  2  3  4
# -5 -4 -3 -2 -1

#s1=name[index_start: index_end]

a1= a[0:3] #start from index 0 all the way till 3 excluding 3
a3=a[-5:-2] 
print(a1) #Printed Son
print(a3) #same output as a1
#[:5] =[0:5] and [4:]= [4:0]

# Keyboard shortcut:
# Alt + Arrow key -> the line moves in the direction of the arrow

a2=a[2] #character in the index 2
print(a2)

#skip value
value='0123456789'
v1=value[1:8:2] #it starts from the value present in the index 1
#stops before 8th and skips values which are not present at 2 
# value at original index 1 is counted as index 0 
print(v1)

#len() - Gives the length of the string
print(len(a))

#string.endswith("") tells if the word ends with ""
print(a.endswith("al")) 
print(a.endswith("aa"))

#string.capitalize capitalizes the first letter of the string
name= "merry"
print(name.capitalize())

#string.lower
print(b.lower())

#string.upper
print(name.upper())

#string.strip
char='S o n a l'
print(char.strip())

#string.replace
print(a.replace("o","i"))

#string.split
print(a.split("n")) #['So','al']

#string.join
print("".join(['i','n','k'])) #ink

#string.find
print(a.find("a")) #index 3

#string.count
print(a.count("a")) #1

#string.startswith
print(a.startswith("a")) #False