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

class company:
    name = "yuvaj" # object attribute
    branch = "cse - aiml"
    age = 19
    year = 2 

    def info(self):
        print(f"Hello, its {self.name} speaking and i pursuing b-tech {self.branch} of {self.year} year and by the way i m {self.age} year old ")  # here we use self which is very important part of oops.

    def __init__(self,name,branch,age):
      self.name = name
      self.branch = branch
      self.age = age
    @staticmethod
    def greet():
       print("good evening")

detail = company("YUVRAJ","BCA",19)
# print(detail.name,detail.branch,detail.age,detail.year)

# detail.branch = " cse -ds " # instance attribute
# detail.greet()
# detail.info()  # self function call
print(detail.name,detail.branch,detail.age)