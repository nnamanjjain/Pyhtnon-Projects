#Task 1: Create a Dictionary of Student Marks

result={'John':83,'Mickey':76,'Alice':85,'Seldon':99,'Penny':100}

name=input("Enter the student's name: ")

marks=result.get(name,'Student Not Found!')

print("{}'s Marks: ".format(name),marks)
