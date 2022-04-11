# sum of two numbers in most simple way in python

# a = 12 
# b = 34

# print("The sum of a and b is : ", a+b)

# sum of two numbers by using Oops concept, use of class and objects

class Number():
    def sum(self):
        return self.a + self.b 

num = Number()
num.a = 12
num.b = 34
s = num.sum()
print(s)

'''
PascalCase -->  EmployeeName, StudentId...etc  (har word ki first letter capital hogi, space se matlab nahi hoga)

camelCase  -->  isNumeric, isFloat...etc   (har name ka second word ka first letter hi capital hoga)

'''