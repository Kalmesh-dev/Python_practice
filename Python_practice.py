#OOPS Concepts
"""1, Classes:"""

# class Person:
#   name = "Kalmesh Latur"
#   age = "25"
#   occupation = "Data Scientist"
#   def info(self):
#     print(f"{self.name} is at age of {self.age} and is a {self.occupation}")

# a = Person()
# print(a.name)
# a.info()

"""when ever we create a function or a constructor in a class, we use self keyword to access the attribuates of the class"""

"""2, Constructors:"""

# class Person:
#   def __init__(self):
#     print("Hey I am a person")


# a=Person()
# b=Person()

# class Person:
#   def __init__(self,n,a,o):
#     self.name = n 
#     self.age = a
#     self.occ = o

#   def info(self):
#     print(f"{self.name} is at age of {self.age} and is a {self.occ}")


# a = Person("Kalmesh", 25, "Data Scientist")
# b = Person("Ruplai", 23, "HR")
# c = Person("Vasant", 45, "Manager")
# print(a.name, a.age)
# a.info()
# b.info()
# c.info()

"""3, Decorators:"""

# def hello():
#   print("Hello World..!")

# hello()


# def greet(fun):
#   print("Good Morning..!, Welcome to the function")
#   fun()
#   print("Thank you for using function, Have a great day")
#   return fun
#   def add(a,b):
#     print(a+b) 
# """Inside a function if you write anything after return it will not be executed. It will be ignored"""
# @greet
# def hello():
#   print("Hello World..!")

# hello()

# def greet(fun):
#   def mfx():  
#     print("Good Morning..!, Welcome to the function")
#     fun()
#     print("Thank you for using function, Have a great day")
#   return mfx
# #@greet
# def hello():
#   print("Hello world")
  
# #hello()
# greet(hello)()
# #Both are same way of calling function.


# def greet(average_fun):
#   def modified_average(a,b):
#     print("The average of two numbers is:", average_fun(a,b))
#     print("Thank you for using the function")
#   return modified_average
    

# @greet
# def average(a,b):
#   return (a+b)/2

# average(2,4)

# def greet(average_func):
#   def wrapper(a, b):
#       print("The average of two numbers is:", average_func(a, b))
#       print("Thank you for using the function")

#   return wrapper

# @greet
# def average(a, b):
#   return (a + b) / 2

# average(2, 4)
 # """Lets see why we use 2 different names for the same function Because if you call the function using the first name it will be in loop where same function name will be invoked from the function hence it will be in infinite loop"""

# def greet(average_func):
# def greet(fx):
#   def mfx(a,b):
#     print("Welcome to the function")
#     print(f" the average of {a} and {b} is:", average(a,b))
#     print("Thanks for using the function")
#   return mfx
# @greet
# def average(a,b):
#   return (a+b)/2

# average(2,5)
## This is practical for above explaination.

# def greet(fx):
#   def mfx(a,b):
#     print("Welcome to the function")
#     print(f" the average of {a} and {b} is:", fx(a,b))
#     print("Thanks for using the function")
#   return mfx
# @greet
# def average(a,b):
#   return (a+b)/2

# average(2,5)

# import logging

# def log_function_call(func):
#     def decorater(*args, **kwargs):
#         logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"{func.__name__} returned {result}")  
#         return result
#     return decorater

# @log_function_call
# def my_function(a, b):
#       return a + b  

# def Bdy_wish(fx):
#   def mfx(name):
#     print("Wish you a very happy birthday")
#     fx(name)
#     print("Thank you for using the function")
#   return mfx
# @Bdy_wish
# def hello(name):
#   print(name)

# @Bdy_wish
# def welcome(name):
#   print(f"Welcome {name}")

# hello("Kalmesh")
# welcome("Kalmesh")

"""4, Getters and Setters:"""

# class Myclass():
#   def __init__(self, value):
#     self.value = value
#   def show(self):
#     print(f"Value is {self.value}")

# @property
# def valuee(value):
#   return value

# obj= Myclass(10)
# print(obj.value)
# obj.show()

# class Myclass:
#   def __init__(self, value):
#     self._value = value
#   def show(self):
#     print(f"Value is {self._value}")

#   @property # this is the getter
#   def value(self):
#     return self._value
    
#   @property # this is a getter 
#   def Ten_value(self):
#     return 10 * self._value

#   @Ten_value.setter # This is a setter of Ten_value getter
#   def Ten_value(self, new_value):
#     self._value = new_value/10
# obj= Myclass(10)
# #obj.self._value = 34 -> We can't do this for this we have to make setters

# obj.show()
# obj.Ten_value = 89
# print(obj.Ten_value)
# print(obj._value)

"""5, Inheritance:"""
# without inheritance 
# class Employe:
#   def __init__(self, name, id):
#     self.name = name
#     self.id = id

#   def showDetails(self):
#     print(f"The name of the employe : {self.name} and id is {self.id}")

# e1 = Employe("Kalmesh", 2199680)
# e2 = Employe("Rupali", 21996801)
# e1.showDetails()
# e2.showDetails()

# with inheritance
# class Employe:
#   def __init__(self, name, id):
#     self.name = name
#     self.id = id

#   def showDetails(self):
#     print(f"The name of the emplye is {self.name} and his employe id is {self.id}")

# class Programmer(Employe):
#   def __init__(self,language, salary):
#     #self.name = name
#     self.language = language
#     self.salary = salary
#   def showMoreDetails(self):
#     print(f"The language of the programmer is {self.language} and his salary is {self.salary}")

# e1 = Employe("kalmesh", 2199680)
# e1.showDetails()
# e2 = Programmer("Python" , 25000)
# e2.showMoreDetails()

#


# class Employe:
#   def __Init__(self, name, id):
#       self.name = name
#       self.id = id
#       #print("The name of and id is", self.name, self.id)
#   def showDetails(self):
#     return name, id


# d = showDetails("Kalmesh", 34)

# class Employe:
#   def __init__(self):
#     self.__name = "Harry" # This is a private variable because when ever we use double underscore before a variable it is a private variable and it can't be accessed outside the class.
#     self.__id = id    

# a = Employe()
# print(a.__name) # this won't work because the name is decleared as private
# print(a.self.__name)



# class Employee:
#   def __init__(self):
#       self.__name = "Kalmesh"

# # Creating an instance of the Employee class
# a = Employee()

# # Attempting to access the private attribute directly will raise an AttributeError
# # print(a.__name)  # This will raise an AttributeError

# # Accessing the mangled name
# print(a._Employee__name)  # This will print "Kalmesh"

# # The second print statement is incorrect and will raise an AttributeError
# # print(a.Employee.__name)  # This will raise an AttributeError

# class Employe:
#   def __init__(self):
#     self.__name = "Kalemsh"

# a = Employe()
# print(a._Employe__name)

# class Student:
#   def __init__(self):
#     self._name = "Kalmesh"

#   def _funName(self):
#     return "#codewithKalmesh"

# class Subject:

#   pass

# obj = Student()
# obj2 = Subject()
# print(obj._name)
# #print(obj._funName)
# #print(obj._Student__name)
# print(obj._funName())
# 0 and 1 = 1
# 0 and 2 = 2
# 1 and 2 = 1

#Snake Water Gun Game
# import random

# def compare(comp,user):
#   if comp == user:
#     return 0
#   if comp == 0 and user == 1:
#     return -1
#   if comp == 1 and user == 2:
#     return -1
#   if comp == 2 and user == 0:
#     return -1

#   return 1

# comp = random.randint(0,2)
# user = int(input("0 for snake, 1 for water and 2 for gun:"))
# score = compare(comp, user)
# print(f"You choose: {user}")
# print(f"Computer choose: {comp}")
# if (score == 0):
#   print("It's a draw")
# elif(score == -1):
#   print("You Loose")
# else:
#   print("You won")

#STATIC METHOD:

# class Maths:
#   @staticmethod
#   def add(a,g):
#     return a + g

# result = Maths.add(1,3)
# a = Maths()
# print(a.add(9,90))
# print(result)

#Without Static class 
# class Math:
#   def __init__(self, number):
#     self.num = number
#   def addToNum(self, number2):
#     return self.num + number2


# a = Math(5)
# print(a.addToNum(89))

# """Basically Staticmethod means that we can use the class without creating an object of the class. It is used to create a function that doesn't require any object of the class. It is used to create a function that doesn"""

# class Math:
#   def __init__(self, num):
#     self.num = num
#   def addToNum(self, num2):
#     self.num += num2

#   @staticmethod
#   def add(a,b):
#     return a+b

# a = Math(5)
# print(a.num)
# print(a.addToNum(5))

# # in this way we can call static method without creating an object of the class 
# print(Math.add(4,2))
# print(a.add(9,88))

# class Employee:
#   def __init__(self, name):
#     self.name = name 
#     self.increment = 0.08
#   def showDetails(self):
#     print(f"The name of the employe is {self.name} and the increment he got is {self.increment}")

# emp1 = Employee("Kalemsh")
# emp2 = Employee("Ruplai")
# emp1.increment = 0.23
# emp1.showDetails()
# emp2.showDetails()

# """Above class is a normal class and we can use it as a normal class.Here name and increment are the instance variable and we can use it as a normal variable"""

# # Class with class Variables
# class Employee:
#   companyName = "TCS" # This is the class variable
#   def __init__(self, name, empId):
#     self.name = name
#     self.empId = empId
#   def showDetails(self):
#     print(f"The name of the emp id {self.empId} is {self.name}. He currently working in {self.companyName}")

# emp1 = Employee('Kalmesh', 2199680)
# emp1.companyName = "Google" #Here we created an instant varibale for Kalmesh
# emp2 = Employee("Rupali", 219968) # Here we created an instant variable for Rupali But we didn't change compnayName for Ruplai so default name TCS will be used
# Employee.companyName = "Apple" # Here we changed the companyName for all the employees"
# emp2.showDetails()
# emp1.showDetails()

# class Employee:
#   companyName = "TCS" # This is the class variable
#   noOfEmp = 0
#   def __init__(self, name, empId):
#     self.name = name
#     self.empId = empId
#     Employee.noOfEmp += 1
#   def showDetails(self):
#     print(f"The name of the emp id {self.empId} is {self.name}. He currently working in {self.noOfEmp} sized company {self.companyName}")

# emp1 = Employee('Kalmesh', 2199680)
# emp1.companyName = "Google" #Here we created an instant varibale for Kalmesh
# emp2 = Employee("Rupali", 219968) # Here we created an instant variable for Rupali But we didn't change compnayName for Ruplai so default name TCS will be used
# Employee.companyName = "Apple" # Here we changed the companyName for all the employees"
# emp2.showDetails()
# emp1.showDetails()
# print(Employee.companyName)
# print(Employee.noOfEmp)

# class Employee:
#   companyName = "TCS"  # This is the class variable
#   noOfEmp = 0

#   def __init__(self, name, empId):
#       self.name = name
#       self.empId = empId
#       Employee.noOfEmp += 1

#   def showDetails(self):
#       print(f"The name of the emp id {self.empId} is {self.name}. "
#             f"He currently works in a {self.noOfEmp}-sized company named {Employee.companyName}")

# # Creating the first employee instance
# emp1 = Employee('Kalmesh', 2199680)
# emp1.companyName = "Google"  # Creating an instance variable for Kalmesh

# # Creating the second employee instance
# emp2 = Employee("Rupali", 219968)  # Default companyName TCS will be used

# # Changing the class variable companyName for all employees
# Employee.companyName = "Apple"

# # Showing details of emp2
# emp1.showDetails()
# # Expected output:
# # The name of the emp id 219968 is Rupali. He currently works in a 2-sized company named Apple

# # Showing details of emp1
# emp2.showDetails()
# # Expected output:
# # The name of the emp id 2199680 is Kalmesh. He currently works in a 2-sized company named Google


#Books Library example

# class Library:
#   def __init__(self):
#     self.totalBooks = 0
#     self.Books = []

#   def addBook(self, book):
#     self.Books.append(book)
#     self.totalBooks = len(self.Books)
#   def showDetails(self):
#     print(f"The total number of books in the library are {self.totalBooks}")
#     for i in self.Books:
#       print(i)
# b1 = Library()
# b1.addBook("Rich Dad poor dad")
# b1.addBook("The Alchemist")
# b1.addBook("The Hobbit")
# b1.showDetails()


# class Method:

# class Employee:
#   Company = "Apple"
#   def __init__(self, name, empid):
#     self.name = name
#     self.empid = empid
#   def show(self):
#     print(f"The name of the employee is {self.name} and his id is {self.empid}")
  
#   def changeCompanyName(cls, NewCompany):
#     cls.Company = NewCompany

# e1 = Employee("Kalmesh", 2199680)
# e1.show()
# e1.changeCompanyName("Tesla")
# e1.show()
# print(Employee.Company)

# # This is Normal example without class method

# class Employee:
#   Company = "Apple"
#   def __init__(self, name, empid):
#     self.name = name
#     self.empid = empid
#   def show(self):
#     print(f"The name of the employee is {self.name} and his id is {self.empid}")
    
#   @classmethod
#   def changeCompanyName(cls, NewCompany):
#     cls.Company = NewCompany

# e1 = Employee("Kalmesh", 2199680)
# e1.show()
# e1.changeCompanyName("Tesla")
# e1.show()
# print(Employee.Company)

# This is example with class method here we use classmethod to change the company name normally here we use cls to change the company name But with help of classmethod we can change the company name without using cls permantly.

#Alternative Constructor:

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
    
#   def show(self):
#     print(f"Hello..! I am {self.name}, I am {self.age} years old")


# e1 = Person("Kalmesh", 22)
# e1.show()
# string = "Kalmesh-24"
# e2 = Person(string.split("-")[0], string.split("-")[1])
# e2.show()

# # We can do like this but since it looks to messy so we use class method to resolve these kind of issues
# # like we don't know in which format we will get the input so we can't use split method to split the string. instead of that we use class method as alternative constructor.

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def show(self):
#     print(f"Hello..! I am {self.name}, I am {self.age} years old")

#   @classmethod
#   def ipFromString(cls, string):
#     return cls(string.split("-")[0],int(string.split("-")[1]))

# e1 = Person("Kalmesh", 22)
# e1.show()
# string = "Rupali-34"
# e2 = Person.ipFromString(string)
# e2.show()

# #ex2:

# class Employee:
#   def __init__(self, name, salary):
#     self.name = name
#     self.salary = salary

#   def show(self):
#     print(f"The name of the employee is {self.name} and his salary is {self.salary}")

#   @classmethod
#   def ipFromString(cls, string):
#     print(string)
#     name , salary = string.split(",")
#     print(name, salary)
#     return cls(name, int(salary))
    

# e1 = Employee("Sheetal", 876873)
# e1.show()
# #string = "Kalmesh,23"
# #nameList = ["Kal ]
# e2 = Employee.ipFromString("Kalmesh,34939")
# #Employee.show(e2)
# e2.show()
# print(e2.name, e2.salary)

# x = [1,2 ,3]
# print(dir(x))
# print(x.__add__)


# #printing dir of any function will give all methods whiich are available for the attribute

# class Person:
#   def __init__(self,name,sex,age):
#     self.name = name
#     self.age = age
#     self.sex = sex

# p = Person("Kalmesh", "Male", 24)
# print(p.name)
# print(p.__dict__)

# # This __dict__ will give all the attributes of the class in the form of dictionary

# print(help(Person))

# # This help function will give all the information about the class and its methods and attributes This help is really amazing we have to use it often.


# class parentClass:
#   def parentMethod(self):
#     print("I am parentMethod of class ParentClass")

# class childClass:
#   def childMethod(self):
#     print("I am childMethod of the class childClass")


# child_class = childClass()
# child_class.childMethod()

# # this is normal Method calling without using super keyword.
# #The super keyword is used to call a method of the parent class 

# class parentClass:
#   def parentMethod(self):
#     print("I am parentMethod of class ParentClass")

# class childClass(parentClass):
#   def childMethod(self):
#     print("I am a childmethod of childClass")
#     super().parentMethod()

# child_class= childClass()
# child_class.childMethod()

# #ex2:

# class parentClass:
#   def parentMethod(self):
#     print("I am parentMethod of class ParentClass")

# class childClass(parentClass):
#   def parentMethod(self):
#     print("I am parentMethos of childClass")
#   def childMethod(self):
#     print("I am a childmethod of childClass")
#     super().parentMethod()

# child_class= childClass()
# child_class.childMethod()
# #child_class.childMethod()

# calling parent class constructor

# without using super keyword we can call the constructor of the parent class

# class Employee:
#   def __init__(self, name, id):
#     self.name = name
#     self.id = id

# class Programmer(Employee):
#   def __init__(self, name, id, language):
#     self.name = name
#     self.id = id
#     self.language = language
    
# e1 = Employee("Kalmesh", 2199680)
# print(e1.name)
# print(e1.id)
# e2 = Programmer("Rupali", 2199681, "Python")
# print(e2.name)
# print(e2.id)
# print(e2.language)

# ## with using super keyword we can call the constructor of the parent class


# class Employee:
#   def __init__(self, name, id):
#     self.name = name
#     self.id = id

# class Programmer(Employee):
#   def __init__(self, name, id, language):
#     super().__init__(name,id)
#     self.language = language

# e1 = Employee("Kalmesh", 2199680)
# e2 = Programmer("Rupali", 2199681, "Python")
# print(e2.name)
# print(e2.id)
# print(e2.language)

"""Magic/Dunder Methods"""

 # __len__ method
# class Employee:
#   name = "Kalmesh"

#   def __len__(self):
#     sum = 0 
#     for letters in self.name:
#       sum += 1
#     return sum 

# e1 = Employee()
# print(len(e1))

# __str__ method

# class Person:
#   name = "Kalmesh"

# def __str__(self):
#   return f"The name of the person is {self.name}"

# k = Person()
# #print(k.name)
# print(k)
# # This above code won't work Because It is not giving the expected output.

# class Person:
#   def __init__(self, name):
#     self.name = name

#   def __str__(self):
#     return f"The name of the person is {self.name}"

# k = Person("Kalmesh")
# print(k)

# # This is one is okay

# # __repr__ method

# class Person:
#   def __init__(self, name):
#     self.name = name

#   def __str__(self):
#     return f"The name of the person is {self.name} str"

#   def __repr__(self):
#     return f"The name of the person is {self.name} repr"


# k = Person("Kalmesh")
# print(k)
# print(str(k))
# print(repr(k))

# # __call__ Method

# class Employee:
#   def __init__(self, name, id):
#     self.name = name
#     self.id = id

#   def __call__(self):
#     print("I am called")

# e1 = Employee("Kalmesh", 2199680)
# e1()

# Method Overriding:

# class Shape:
#   def __init__(self, x , y):
#     self.x = x
#     self.y = y

#   def area(self):
#     return self.x * self.y

# class circle(Shape):
#   def __init__(self, radious):
#     self.radious = radious
#     super().__init__(radious, radious) # this is the way to call the parent class constructor But here in this condition this not correct because the area of circle not found by multiplying radious * radious So we are getting out put but the answer is not correct.
#     super().area()
# rec = Shape(3,5)
# print(rec.area())
# c = circle(5)
# print(c.area())

# # Correct Example

# class Shape:
#   def __init__(self, x , y):
#     self.x = x
#     self.y = y

#   def area(self):
#     return self.x * self.y

# class circle(Shape):
#   def __init__(self, radious):
#     self.radious = radious
#     super().__init__(radious, radious) # 
#     #super().area()
#   def areaOfCircle(self, radious):
#     #return 3.14 * radious * radious
#     return 3.14 * super().area() 
#     # We can do in both ways
    
# rec = Shape(3,5)
# print(rec.area())
# c = circle(5)
# print(c.area())

# import os
# #os.rename("cluterredfolder/file.txt", "cluterredfolder/file2.txt")

# file = os.listdir("cluterredfolder")
# i = 1
# for file in file:
#   if file.endswith(".png"):
#     os.rename(f"cluterredfolder/{file}",         f"cluterredfolder/{i}.png")
#     print(i)
#     i = i + 1

# import os
# #os.rename("cluterredfolder/file.txt", "cluterredfolder/file2.txt")

# file = os.listdir("cluterredfolder")
# i = 1
# for file in file:
#   if file.endswith(".jpg"):
#     os.rename(f"cluterredfolder/{file}",         f"cluterredfolder/{i}.jpg")
#     print(i)
#     i = i + 1

# """Method Overriding:"""

# class Shape:
#   def __init__(self, x , y):
#     self.x = x
#     self.y = y
#   def area(self):
#     return self.x * self.y
# class Circle(Shape):
#   def __init__(self, radious):
#     self.radious = radious
#     super().__init__(radious, radious)
#   def areaOfCircle(self):
#     #return 3.142 * radious * radious
#      return 3.142 * super().area()
# c1 = Circle(5)
# print(c1.areaOfCircle())

# Example 2:
# class Employee:
#   def __init__(self, name, salary):
#     self.name = name
#     self.salary = salary

#   def getRoleDes(self):
#     return "Data Analyst"
#   def getCompanyName(self):
#     return "SAP"
#   def getAnualSalary(self):
#     return self.salary * 12

# class Manager(Employee):
#   def __init__(self, name, salary, department):
#     super().__init__(name, salary)
#     self.department = department
#   def getRoleDes(self):
#     return f"Manager of {self.department}"
#   def getAnualSalary(self):
#     base_salary = super().getAnualSalary()
#     bonus = base_salary * 0.05
#     return base_salary * bonus
# class Programmer(Employee):
#   def __init__(self,name, salary, language):
#     super().__init__(name, salary)
#     self.language = language
#   def getRoleDes(self):
#     return f"{self.language} Programmer"

# Employee = [Employee("Kalmesh", 230000), Manager("Rohan", 45000,"Business Analyst"), Programmer("Shrey", 34000, "Python")]

# # for e in Employee:
# #   print("Employee Name:", e.name)
# #   print("Employee Salary:", e.salary)
# #   print("Employee Role:", e.getRoleDes())
# #   print("Employee Company:", e.getCompanyName())
# #   print("Employee Anual Salary:", e.getAnualSalary())
# #   print("Employee Department:", e.getDepartment())
# #   print("Employee Language:", e.getLanguage(),"\n")

# for e in Employee:
#   print(f"{e.name} is a {e.getRoleDes()} in {e.getCompanyName()} and his anual salary is {e.salary} \n")


# from pypdf2 import PdfWriter
# merger = PdfWriter()
# for pdf in ["text1.pdf", "text2.pdf", "text3.pdf"]:
#   merger.append(pdf)
# merger.write("merged-pdf.pdf")
# merger.close()

"""Operator Overloading"""

# class Vector:
#   def __init__(self, i,j,k):
#     self.i = i
#     self.j = j
#     self.k = k
#   def __str__(self):
#     return f"{self.i}i + {self.j}j + {self.k}k"

# v1 = Vector(3,5,2)
# print(v1)
# print(type(v1))

# # Using add function output is string
# class Vector:
#   def __init__(self, i,j,k):
#     self.i = i 
#     self.j = j
#     self.k = k

#   def __str__(self):
#     return f"{self.i}i + {self.j}j + {self.k}k"

#   def __add__(self,x):
#     return f"{self.i + x.i}i + {self.j + x.j}j + {self.k + x.k}k"

# v1 = Vector(78,34,22)
# print(v1)
# v2 = Vector(2,4,1)
# print(v2)
# print(v1+v2)
# print(type(v1+v2))

# # Using add Function but Output will be in vector form

# class Vector:
#   def __init__(self, i,j,k):
#     self.i = i 
#     self.j = j
#     self.k = k

#   def __str__(self):
#     return f"{self.i}i + {self.j}j + {self.k}k"

#   def __add__(self,x):
#     return Vector(self.i + x.i,self.j + x.j,self.k + x.k)
#   def __sub__(self, x):
#     return Vector(self.i - x.i,self.j - x.j,self.k - x.k)
# v1 = Vector(78,34,22)
# print(v1)
# v2 = Vector(2,4,1)
# print(v2)
# print(v1+v2)
# print(type(v1+v2))
# print(v1-v2)
# """we can get the output will be in vector form"""

"""Single Inheritance"""

# class Animal:
#   def __init__(self, name, species):
#     self.name = name
#     self.species = species

#   def makeSound(self):
#     print("Sound made by the animal")

# class Dog(Animal):
#   def __init__(self, name, breed):
#     Animal.__init__(self,name , species = "Dog")
#     self.breed = breed

#   def makeSound(self):
#     print("Bark!!")

# d = Dog("Dog","Asci")
# d.makeSound()
# a = Animal("Dog","Dog")
# a.makeSound()

# class Animal:
#   def __init__(self, name, species, color):
#     self.name = name
#     self.species = species
#     self.color = color

#   def makeSound(self):
#     print("Sound made by the animal")

# class Cat(Animal):
#   def __init__(self,name,breed,color):
#     super().__init__(name,"Cat",color)
#     self.breed = breed

#   def makeSound(self):
#     print("Meow!!")

# c = Cat("Cat","Persian","White")
# c.makeSound()
# c2 = Animal("Cat","Cat","Black")
# c2.makeSound()


# class Animal:
#   def __init__(self, name, species, color):
#       self.name = name
#       self.species = species
#       self.color = color

#   def makeSound(self):
#       print("Sound made by the animal")

# class Cat(Animal):
#   def __init__(self, name, breed, color):
#       super().__init__(name, "Cat", color)
#       self.breed = breed

#   def makeSound(self):
#       print("Meow!!")

# # Creating an instance of Cat
# c = Cat("Whiskers", "Persian", "White")
# c.makeSound()  # Output: Meow!!

# # Creating an instance of Animal
# c2 = Animal("Shadow", "Cat", "Black")
# c2.makeSound()  # Output: Sound made by the animal

# """Multiple Inheritance"""
# """A class which has 2 or more parent class those classes are called as Multiple Inherited classes"""

# from collections.abc import Mapping


# class Employee:
#   pass
# class Dancer:
#   pass

# class DancerEmployee(Dancer, Employee):
#   pass

# This we can call it as a Map, before creating actual content we will add a map may be this is what it is.

# class Emlpoyee:
#   def __init__(self, name):
#     self.name = name

# class Dancer:
#   def __init__(self, dance):
#     self.dance = dance

# class DancerEmployee(Dancer, Employee):
#   def __init__(self, name , dance):
#     self.name = name
#     self.dance = dance

# o = DancerEmployee("Kalmesh", "BreakDance")
# print(o.name)
# print(o.dance)

#same thing we can write with more content
"""Here we will Know about MRO(Method Resolution Order)"""
# class Emlpoyee:
#   def __init__(self, name):
#     self.name = name

#   def show(self):
#     print(f"The name is {self.name}")

# class Dancer:
#   def __init__(self, dance):
#     self.dance = dance

#   def show(self):
#     print(f"The dance is {self.dance}")

# class DancerEmployee(Dancer, Employee):
#   def __init__(self, name , dance):
#     self.name = name
#     self.dance = dance

# o = DancerEmployee("Kalmesh", "BreakDance")
# print(o.name)
# print(o.dance)
# o.show() # Here when I call show method which is in both class, here the method of Dancer class is executing Because while creating the child class in bracket we give class names right, depending which class name is given first it will execute that class object first this is called as MRO(method resolution order)
# o.show()

# class Emlpoyee:
#   def __init__(self, name):
#     self.name = name

#   def show(self):
#     print(f"The name is {self.name}")

# class Dancer:
#   def __init__(self, dance):
#     self.dance = dance

#   def show(self):
#     print(f"The dance is {self.dance}")

# class DancerEmployee(Employee,Dancer):
#   def __init__(self, name, dance):
#     self.name = name
#     self.dance = dance

# o = DancerEmployee("Kalmesh", "BreakDance")
# print(o.name)
# print(o.dance)
# o.show() # Here when I call show method which is in both class, here the method of Dancer class is executing Because while creating the child class in bracket we give class names right, depending which class name is given first it will execute that class object first this is called as MRO(method resolution order)
# o.show()
# print(DancerEmployee.mro())

# class Employee:
#   def __init__(self, name):
#     self.name= name
#   def show(self):
#     print(f"The name is {self.name}")

# class Singer:
#   def __init__(self, genre):
#     self.genre = genre

#   def show(self):
#     print(f"The genre is {self.genre}")

# class SingerEmployee(Singer, Employee):
#   def __init__(self, name, genre):
#     self.name = name
#     self.genre = genre

# e1 = SingerEmployee("Kalmesh", "pop")
# e1.show()

# class Employee:
#   def __init__(self, name):
#     self.name= name
#   def show(self):
#     print(f"The name is {self.name}")

# class Singer:
#   def __init__(self, genre):
#     self.genre = genre

#   def show(self):
#     print(f"The genre is {self.genre}")

# class SingerEmployee(Employee, Singer):
#   def __init__(self, name, genre):
#     self.name = name
#     self.genre = genre

# e1 = SingerEmployee("Kalmesh", "pop")
# e1.show()

"""Multilevel Inheritance"""

# class Animal:
#   def __init__(self, name, species):
#     self.name = name
#     self.species = species
    
#   def showDetails(self):
#     print(f"The name is {self.name}")
#     print(f"The species is {self.species}")

# class Dog(Animal):
#   def __init__(self,name, breed):
#     Animal.__init__(self,name,species = "Dog")
#     self.breed = breed

#   def showDetails(self):
#     super().showDetails()
#     #Animal.showDetails(self) #both lines are same
#     print(f"The breed is {self.breed}")

# class GoldenRetreiver(Dog):
#   def __init__(self,name, color):
#     Dog.__init__(self, name, breed = "GoldenRetreiver")
#     self.color = color

#   def showDetails(self):
#     Dog.showDetails(self)
#     print(f"The color is {self.color}")

# o = GoldenRetreiver("Tommy", "Black")
# o.showDetails()
# print(GoldenRetreiver.mro())


"""Hybrid Inheritance"""

# class Animal:
#   def __init__(self, name):
#     self.name = name

#   def showDetails(self):
#     print(f"Name : {self.name}")

# class Mammel(Animal):
#   def __init__(self, name, has_fur):
#     Animal.__init__(self,name)
#     self.has_fur = has_fur

#   def showDetails(self):
#     super().showDetails()
#     print(f"Has Fur : {self.has_fur}")

# class Bird(Animal):
#   def __init__(self, name, can_fly):
#     Animal.__init__(self,name)
#     self.can_fly = can_fly

#   def showDetails(self):
#     super().showDetails()
#     print(f"Can Fly : {self.can_fly}")

# class Bat(Mammel, Bird):
#   def __init__(self, name, has_fur, can_fly, nocturnal):
#     Mammel.__init__(self,name,has_fur)
#     Bird.__init__(self,name,can_fly)
#     self.nocturnal = nocturnal

#   def showDetails(self):
#     Mammel.showDetails(self)
#     Bird.showDetails(self)
#     print(f"Nocutural : {self.nocturnal}")

# o = Bat("Bat", True, True, True)
# o.showDetails()

# class Animal:
#   def __init__(self, name):
#       self.name = name

#   def show_details(self):
#       print(f"Name: {self.name}")

# class Mammal(Animal):
#   def __init__(self, name, has_fur):
#       super().__init__(name)
#       self.has_fur = has_fur

#   def show_details(self):
#       super().show_details()
#       print(f"Has fur: {self.has_fur}")

# class Bird(Animal):
#   def __init__(self, name, can_fly):
#       super().__init__(name)
#       self.can_fly = can_fly

#   def show_details(self):
#       super().show_details()
#       print(f"Can fly: {self.can_fly}")

# class Bat(Mammal, Bird):
#   def __init__(self, name, has_fur, can_fly, nocturnal):
#       Mammal.__init__(self, name, has_fur)
#       Bird.__init__(self, name, can_fly)
#       self.nocturnal = nocturnal

#   def show_details(self):
#       Mammal.show_details(self)
#       Bird.show_details(self)
#       print(f"Nocturnal: {self.nocturnal}")

# # Create an instance of Bat
# bat = Bat("Bruce", True, True, True)

# # Call the show_details method
# bat.show_details()

# """Time Module"""

# import time

# def usingwhile():
#   i = 0 
#   while i < 50000:
#     i += 1
#     print(i)
# def usingfor():
#   for i in range(50000):
#     print(i)

# init = time.time()
# usingwhile()
# t = print(time.time()-init)
# usingfor()
# print(time.time()-init)
# print(t)
# import time
# print(5)
# time.sleep(4)
# print("This is printed after 4 seconds")

# t = time.localtime()
# localTime = time.strftime("%Y-%m-%d", t)
# print(localTime)

# t = time.localtime()
# formatted_time = time.strftime("%d-%m-%Y %H:%M:%S", t)
# print(formatted_time)
# t = time.localtime()


"""Creating command line utility"""
# import argparse
# import requests

# def DownloadFile(url)
#     local_filename = url.split('/')[-1]
#     r = requests.get(url)
#     f = open(local_filename, 'wb')
#     for chunk in r.iter_content(chunk_size=512 * 1024): 
#         if chunk: # filter out keep-alive new chunks
#             f.write(chunk)
#     f.close()
#     return 

# parser = argparse.ArgumentParser()

# parser.add_argument("url", help="Url of the file to download")
# parser.add_argument("output", help="By which name do you want to save the file")

# args = parser.parse_args()


# print(args.url)
# print(args.output)
"""Above code is not working"""

"""Warlus Operator"""
"""New to python 3.8
Basicaly it is used to assign the value of a variable in the expression"""

# a = True
# print(a = False) # This will give error this is not done in python to make this work we use warlus operator (:=)

# a = True
# print(a := False)
# #print(a)


# numbers = [1,2,3,4,5,6]
# while(len(numbers) > 0):
#   print(numbers.pop())
# print("")
# numbers = [1,2,3,4,5,6]
# while(n := len(numbers) > 0):
#   print(numbers.pop())

# happy = True
# print(happy)
# print(happy := False)

#Without warlus opertor

# while True:
#   food = input("Enter the food you like most:")
#   if food == "quit":
#     break

# foods = list()
# while True:
#   food = input("Enter the food you like most:")
#   if food == "over":
#     break
#   foods.append(food)
# print(foods)
# foods = list()
# while(food == input("Enter the food you like most:")) != "quit":
#   foods.append(food)
# print(foods)
"""For more details check the error of above code"""

# With Warlus Operator

# foods = list()
# while(food := input("Enter the food you like most:")) != "quit":
#   foods.append(food)
# print(foods)

"""Shutil Module"""

import shutil
import os

# shutil.copy("text1.pdf", "text4.pdf")
# shutil.copy2("text4.pdf","text5.pdf")
# shutil.copy2("file2.txt", "file3.txt")
# shutil.copytree("junk","junk3")
#shutil.move("junk/text1.pdf", "text1.pdf")
#shutil.move("junk/file12.txt","file12.txt")
#os.remove("file12.txt")
#os.removedirs("junk3")
#os.removedirs("junk")
#shutil.rmtree("junk", ignore_errors=True)
#shutil.rmtree("junk2")
#os.removedirs("junk3")
#shutil.rmtree("junk3")#, ignore_errors=True)
#os.remove("text1.pdf")

"""Generators in Python"""
"""Generators are used to generate a sequence of values over time. They are a special type of iterators that allow you to iterate over a sequence of values without loading the entire sequence into memory at once"""

# def Generators():
#   for i in range(30000):
#     yield i

# gen = Generators()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# for i in gen:
#   print(i)

"""Function Caching"""
"""Function caching is a technique used to improve the performance of a program by storing the results of a function call so that you do not have to recalculate them every time you need them. This can be particularly useful when a function is computationally expensive or when the results are dependent on external factors such as time of the day or weather."""
"""to use function caching we have to use @functools.cache decorator"""

# from functools import lru_cache
# import time

# @lru_cache(maxsize = None)

# def fun(n):
#   time.sleep(1)
#   return (n*3)+7


# print(fun(20))
# print(fun(3))
# print(fun(9))
# print(fun(12))
# print(fun(20))
# print(fun(20))
# print(fun(3))
# print(fun(9))
# print(fun(12))
# print(fun(20))
# print(fun(34))
# print(fun(92))


#""""""
#package@latest
# import requests
# import json

# query = input("What type of news are you interesred now?")
# # url = f"https://newsapi.org/v2/everything?q={query}tesla&from=2024-05-13&sortBy=publishedAt&apiKey=API_KEY=d0ad2e7c8b194b1b837332847057d33f"
# url = f"https://newsapi.org/v2/everything?q={query}&from=2023-01-28&sortBy=publishedAt&apiKey=d0ad2e7c8b194b1b837332847057d33f"
# r = requests.get(url)
# print(r.text)


# import requests
# import json

# query = input("What type of news are you intersted?? :")
# url = f"https://newsapi.org/v2/everything?q={query}&from=2024-05-14&sortBy=publishedAt&apiKey=d0ad2e7c8b194b1b837332847057d33f"
# r = requests.get(url)
# news = json.loads(r.text)
# print(news, type(news))
# for article in news["articles"]:
#   print(article["title"])
#   print(article["description"])
#   print(article["publishedAt"])
#   print("______________________________________________________________________________________________")


"""Water Drinking remainder"""

# from plyer import notification
# import time

# if __name__=="__main__":
#     while True:
#         notification.notify(title ='Please drink water',app_name="Drinking water" ,message='Please drink water for your own safety',timeout=5 )
#         time.sleep(3600)

"""Code doesn't work"""

"""AsynIO module"""

"""Aynchrounous programming is a programming pattern that allows for high performance I/O operations by offloading I/O-intensive tasks to background threads or processess. This allows for faster response time and improved responsiveness of the application."""

"""Asyncio module is used to write asynchronous code in python. It provides a set of tools for working with asynchronous"""

#without asyncio module

# import time 

# def function1():
#     time.sleep(3)
#     print("function 1")
  
# def function2():
#     time.sleep(3)
#     print("function 2")
  
# def function3():
#     time.sleep(3)
#     print("function 3")

# function1()
# function2()
# function3()

"""Async function means if we have async function it means that we can run these function parallely one after one. """

"""Async function with Create_task method"""

#import time
# import asyncio
# import requests

# async def function1():
#   URL = "https://stock.adobe.com/in/images/4k-hd-ultra-high-quality-visual-delight/668109847"
#   response = requests.get(URL)
#   open("4K_Image", "wb").write(response.content)
#   await asyncio.sleep(1)
#   print("function 1")

# async def function2():
#   URL = "https://instagram.com/favicon.ico"
#   response = requests.get(URL)
#   open("instagram7.ico", "wb").write(response.content)
#   await asyncio.sleep(1)
#   print("function 2")

# async def function3():
#   URL = "https://instagram.com/favicon.ico"
#   response = requests.get(URL)
#   open("instagram8.ico", "wb").write(response.content)
#   await asyncio.sleep(3)
#   print("function 3")

# async def main():
#   task = asyncio.create_task(function1())
#   #await function1()
#   await function2()
#   await function3()
# asyncio.run(main())

"""Gather syntex"""
# import time
# import asyncio

# async def function1():
#   await asyncio.sleep(1)
#   print("function 1")

# async def function2():
#   await asyncio.sleep(1)
#   print("function 2")

# async def function3():
#   await asyncio.sleep(3)
#   print("function 3")

# async def main():
#   l = await asyncio.gather(
#        function1(),
#        function2(),
#        function3(),)
#   print(l)
# asyncio.run(main())

# import asyncio

# async def function1():
#     await asyncio.sleep(1)
#     print("function 1")
#     #return "Result from function 1"

# async def function2():
#     await asyncio.sleep(1)
#     print("function 2")
#     #return "Result from function 2"

# async def function3():
#     await asyncio.sleep(3)
#     print("function 3")
#     #return "Result from function 3"

# async def main():
#     l = await asyncio.gather(
#         function1(),
#         function2(),
#         function3(),
#     )
#     print(l)

# # Run the main function
# asyncio.run(main())

import os

# os.remove("instagram.ico")
# os.remove("instagram2.ico")
# os.remove("instagram3.ico")
# os.remove("4K_Image")

"""Multithreading"""

"""Multithreading means that we can run multiple threads at the same time. This can be useful for performing complex tasks that would otherwise take too long to complete the program"""

# import threading
# import time

# def function(seconds):
#   print(f"Sleeping for {seconds} seconds")
#   time.sleep(seconds)

# # time1 = time.perf_counter()
# # #Normal code
# # function(2)
# # function(3)
# # function(4)
# # time2 = time.perf_counter()
# # print(time2 - time1)
# def main2():
# #Using Multithreading
#   time4 = time.perf_counter()
#   t1 = threading.Thread(target=function, args=[2])
#   t2 = threading.Thread(target=function, args=[3])
#   t3 = threading.Thread(target=function, args=[4])
#   t1.start()
#   t2.start()
#   t3.start()
  
#   time3 = time.perf_counter()
#   print(time3 - time4)

"""why it is taking only zero seconds it should take atleast 4 sec??

Here is the answer Once it start the thread it will run the function and then it will move to next line and it will run the next function and so on. It won't wait to complete the steps of the function. For starting all function it takes 0 sec and then it comes to to last line of the code """

"""To over come this we use join"""
# import threading
# import time
# from concurrent.futures import ThreadPoolExecutor

# def function(seconds):
#   print(f"Sleeping for {seconds} seconds")
#   time.sleep(seconds)
#   return seconds
  
# def main():
#   # time1 = time.perf_counter()
#   # #Normal code
#   # function(2)
#   # function(3)
#   # function(4)
#   # time2 = time.perf_counter()
#   # print(time2 - time1)
  
#   #Using Multithreading
#   time4 = time.perf_counter()
#   t1 = threading.Thread(target=function, args=[2])
#   t2 = threading.Thread(target=function, args=[3])
#   t3 = threading.Thread(target=function, args=[4])
#   t1.start()
#   t2.start()
#   t3.start()
  
#   t1.join()
#   t2.join()
#   t3.join()
  
#   time3 = time.perf_counter()
#   print(time3 - time4)
  
# def PoolExecutor():
#    with ThreadPoolExecutor() as executor:
#   #   future1 = executor.submit(function, 3)
#   #   future2 = executor.submit(function, 6)
#   #   future3 = executor.submit(function, 2)
#   #   print(future1.result())
#   #   print(future2.result())
#   #   print(future3.result())
#     l = [1,4,2,3,4,6]
#     results = executor.map(function, l)
#     for result in results:
#       print(result)


# PoolExecutor()

# import os
# for i in range(20):
#   os.remove(f"file/landscape{i}.jpg")

"""Multiprocessing"""

# import multiprocessing
# import requests

# def downloadFile(url, name):
#   response = requests.get(url)
#   open(f"file/landscape{name}.jpg", "wb").write(response.content)



# url ="https://picsum.photos/4500/3000"
# for i in range(20):
#   downloadFile(url, i)

"""Above example is without multiprocessing"""
"""When we give high level processing task without using multiprocessing then it will work little slow. To over come this we use multiprocessing"""

# import multiprocessing
# import requests

# def downloadFile(url, name):
#   print(f"Starting downloading {name}")
#   response = requests.get(url)
#   open(f"file2/landscape{name}.jpg", "wb").write(response.content)
#   print(f"Finishing downloading {name}")

# url ="https://picsum.photos/5000/3000"
# pros = []
# for i in range(50):
#   p = multiprocessing.Process(target=downloadFile , args=[url, i])
#   p.start()
#   pros.append(i)

# for p in pros:
#   p.join()

"""Example using concurrent.futures"""

import concurrent.futures
import requests

def downloadFile(url, name):
  print(f"Starting downloading {name}")
  response = requests.get(url)
  open(f"file5/landscape{name}.jpg", "wb").write(response.content)
  print(f"Finishing downloading {name}")

url ="https://picsum.photos/6000/4500"

with concurrent.futures.ProcessPoolExecutor() as executer:
  l1 =[url for i in range(60)]
  l2 =[i for i in range(60)]
  result = executer.map(downloadFile, l1, l2)
for r in result:
  print(r)
