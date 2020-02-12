
'''
Print numbers from 1 to 100
Functionality : Print numbers
Input Data : 1 to 100
# Loops
'''
num = 1
while num <= 10:
    print(num)
    num += 1
print("Hello world")
'''
list1 = [[100,'Madhu',10000,3], [101,'Ram',25000,6]]
1 to 2 - 10%
2 to 5 - 20%
5+     - 30%
'''

# Print even numbers betweeen 1 to 100
# Functionality : Print even numbers
# Input data    : 1 to 100
num = 1
while num <= 100:
    if num % 2 == 0:
        print(num)
    num += 1

#Print numbers which are divisible by 3 or 5 between 1 to 100

#functionality : which are divisible by 3 or 5
# Input data   : 1 to 10
print("----------------------")
num = 1
while num <= 100:
    if num % 3 == 0 and num % 5 == 0:
        print("Divisible by 3 and 5 :", num)
    elif num % 3 == 0:
        print("Divisible by 3 :",num)
    elif num % 5 == 0:
        print("Divisible by 5 :",num)
    num += 1
print("Hello world")

# For loop
'''
Print all the elements of below list
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Functionality : Print all the elements
Input data    : list1
'''
print("---------------")
# <sequence> : String List tuple range
# String
print("------------String with for  loop")
for i in 'Hello World':
    print(i)
print("------------List with for  loop")
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
for i in list1:
    print(i)
print("End of for loop")
print("------------Tuple with for  loop")
for i in (1,2,3,4,5):
    print(i)
print("------------Range with for  loop")
for i in range(5,100):
    print(i)
