# now we are gonna do the  oop(objected oriented programming )



# class employee:    # this is class atribute
#     name = "Yuvraj singh"
#     job = "AI ENGINEER"
#     SALARY = 100000
  
#     def info(self):
#        print(f"hello there, its {self.name} speaking, btw i m a {self.job} and i earn {self.SALARY} per month 😊")  
#     @staticmethod
#     def greet():    # in this we will not pass the self
#       print("good morning")


# yuvraj = employee() # this is instance atribute
# yuvraj.job = "software engineer"  # instance
# yuvraj.info()
# print(yuvraj.name, yuvraj.job, yuvraj.SALARY)

# class company:
#     name = input("enter your name: ") # object attribute
#     branch = input("enter your branch: ")
#     age = int (input("enter your age: "))
#     year = int (input("enter your current year: "))
   
   
#     def info(self):
#         print(f"Hello, its {self.name} speaking and i pursuing b-tech {self.branch} of {self.year} year and by the way i m {self.age} year old ")  # here we use self which is very important part of oops.

#     def __init__(self,name,branch,age):
#       self.name = name
#       self.branch = branch
#       self.age = age
#     @staticmethod
#     def greet():
#        print("good evening")

# detail = company()
# print(detail.name,detail.branch,detail.age,detail.year)

# detail.branch = " cse -ds " # instance attribute
# detail.greet()
# detail.info()  # self function call





# now let's do some practice question on object oriented programming.



# problem 1 
# class programmer:
#    company = "MICROSOFT"
#    def __init__ (self, name, salary , pincode):
#       self.name = name 
#       self.salary = salary
#       self.pincode = pincode


# Y = programmer("YUVRAJ", 300000, 201301)
# print(Y.name,Y.salary,Y.pincode)


# problem 2 
# class calculator:
#    def __init__(self,n):
#       self.n = n

#    def square(self):
#       print(f"the square  is {self.n*self.n }")
#    def cube(self):
#       print(f"the cube of is {self.n*self.n*self.n }")
#    def square_root(self):
#       print(f"the square rot of is {self.n**1/2}")
#    @staticmethod
#    def greet():
#       print("hello there, good morning !")

# y = calculator(4)
# y.greet()
# y.square()
# y.cube()
# y.square_root()



# problem 3 
from random import randint

class train:
   
   def __init__(self, train_no):
      self.train_no = train_no
   def book(self,fro, to):
      print(f"your seat will be booked and your train no is {self.train_no} and your train departure from {fro} and destination is {to}")
   def getstatus(self):
      print(f"your train {self.train_no} is  running on time")
   def getfare(self,fro, to):
      print(f"your seat will be booked and your train no is {self.train_no} and your train departure from {fro} and destination is {to}\n you paid {randint(180,370)}")

t = train(20347)
t.book("delhi","bihar")
t.getstatus()
t.getfare("delhi","bihar")