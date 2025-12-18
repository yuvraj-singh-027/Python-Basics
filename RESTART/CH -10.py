# now we are gonna do the  oop(objected oriented programming )



class employee:    # this is class atribute
    name = "Yuvraj singh"
    job = "AI ENGINEER"
    SALARY = 100000
  
    def info(self):
       print(f"hello there, its {self.name} speaking, btw i m a {self.job} and i earn {self.SALARY} per month 😊")  
    @staticmethod
    def greet():    # in this we will not pass the self
      print("good morning")


yuvraj = employee() # this is instance atribute
yuvraj.job = "software engineer"  # instance
yuvraj.info()
# print(yuvraj.name, yuvraj.job, yuvraj.SALARY)

