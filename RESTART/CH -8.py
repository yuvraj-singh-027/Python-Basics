# this chapter about the functions 

# def greet():
#     name = ("enter the user name")
#     print(f"Good morning,{name}")
# greet()

# factorial program
# def factorial(n):
#     if( n == 0  or n ==1):
#         return 1
#     return n * factorial(n-1)

# num = int(("enter the number"))
# print(f"the factorial of n is:{factorial(num)}")

# find greatesr number using function

# def greatest():
#     a = int(("enter the a number"))
#     b = int(("enter the b number"))
#     c = int(("enter the c number"))

#     if( a > b and a>c):
#         print("a is greatest  amoung them")
#     elif(b>a and b>c):
#         print ("b is greatest amoung them")
#     else:
#         print("c is greatest amoung them")


# greatest()


# def bigger(a,b,c):
#     if( a > b and a>c):
#         return a 
#     elif(b>a and b>c):
#         return b
#     else:
#         return c

# print(bigger(6,7,3))

# convert celcuis to farenhite.

# def conversion():
#     c = 5 * (f-32 ) / 9
#     return c

# f = int((" enter the tempreture in farhenite: "))

# print(round(conversion(),2)) #here we use the round built in function which helps to print the value 2digit after point.

# write a programm to find first n natural number

# def natural_num():
#     n  = int(("enter the number"))
#     sum = 0
#     for i in range(1,11):
#        sum = sum + (n+i)
#     return sum    
 

# sum2 = natural_num()
# print(sum2)

# def sum_of_n(n):
#     if(n == 1):
#         return 1
#     return sum_of_n(n-1)+n

# n = int(("enter the number"))5

# print(sum_of_n(n))
    
# write the program to print the star pattern
# def pattern(n):
#     if (n ==0):
#         return 
#     print("*"*n)
#     pattern(n-1)

# n = int( (" enter the number: "))
# pattern(n)

# def converter(inch):
#     return 2.54 * inch

# inch = int(input("ENTER THE NUMBER: "))
# CM =converter(inch)
# print(CM)


def remove(l, word):
    n = [ ]
    for item in l:
        if not(item == "word"):
            l.append(item.strip("word"))
    
    return n

l = [ "yuvraj", "sunny","ajay", "amy"]
word = "y"
print(remove(l,word))