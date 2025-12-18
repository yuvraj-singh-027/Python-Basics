# dictionary

name = {"yuvraj":98, "sunny":78, "aditya":56}

# print(name, type(name))
name.pop("sunny")
print(name)
name["yuvraj"]= 87
print(name)
name["anamika"]= 67
print(name)
name.clear()
print(name)
name["aditya"]
print (name)


# practice question 

words = { 
    "help":"madad" ,
    "chair":"kursi",
    "lion":"sher"
} 

word = input("Enter  the  word  which u wanted to meaning of: ")

print(words[word])


n = set()
digit = input("enter the number :")
n.add(int(digit))
digit = input("enter the number :")
n.add(int(digit))
digit = input("enter the number :")
n.add(int(digit))
digit = input("enter the number :")
n.add(int(digit))
digit = input("enter the number :")
n.add(int(digit))
digit = input("enter the number :")
n.add(int(digit))
digit = input("enter the number :")
n.add(int(digit))
digit = input("enter the number :")
n.add(int(digit))

print(n)



s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') 

print(len(s))


dic = { }
name = input("enter the person name: ")
language = input("enter the person's favouraite language")
dic.update({name:language})

name = input("enter the person name: ")
language = input("enter the person's favouraite language")
dic.update({name:language})

name = input("enter the person name: ")
language = input("enter the person's favouraite language")
dic.update({name:language})

name = input("enter the person name: ")
language = input("enter the person's favouraite language")
dic.update({name:language})

print(dic)