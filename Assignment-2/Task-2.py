#Task 2: Sum of Integers from 1 to 50 Using a Loop

'''
#using while loop
count=1
add=0
while (count<=50):
    add=add+count
    count=count+1
print("The Sum of numbers between 1 and 50 is: ",add)
'''

#using for loop
add=0
for i in range(1,51):
    add=add+i
print("The Sum of numbers between 1 and 50 is: ",add)
