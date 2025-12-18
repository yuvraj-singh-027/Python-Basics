# conditional expression.1
# find the greatest element amoung the 4 numbers
# a1 = int(input("enter the first number a1: "))
# a2= int(input("enter the second number a2: "))
# a3 = int(input("enter the third number a3: "))
# a4 = int(input("enter the fourth number a4: "))

# if (a1 > a2 and a1 > a3 and a1 >a4 ):
#     print("a1 is greatest amoung them")
# elif(a2 >a1 and a2>a3 and a2>a4 ):
#     print("a2 is greatest amoung them")
# elif (a3> a1 and a3 >a2 and a3 > a4):
#     print("a3 is greatest  amoung them")
# else:
#     print("a4 is greatest amoung them")
# print(" programm end ")


# pass or  fail programm
# mark1 = int(input("enter the mark:"))
# mark2 = int(input("enter the mark:"))
# mark3 = int(input("enter the mark:"))

# total_percentage = (100*(mark1+mark2+mark3))/300

# if ( total_percentage >= 40 and mark1 >= 33 and mark2 >= 33 and mark3 >= 33):
#     print(" congrats you passed", total_percentage)
# else:
#     print(" try next  year, you failed",total_percentage)


# spam detector

# p1 = "Make a lot of money"
# p2 = "buy now"
# p3 = "subscribe this"
# p4 ="click this"

# comment = input(" enter the  comment")

# if( (p1 in comment) or ( p2 in comment ) or (p3 in comment )or (p4 in comment  )):
#     print(" there are some unwanted thing are persent in your comment ")
# else:
#     print(" there are no restricted word in comment section")



# name = input(" enter your full name: ")

# letters = len(name)

# if ( letters < 10 ):
#     print("your name contain less than 10 characters")
# else:
#     print("your name contain more than 10 characters")



# list = [ "yuvraj", "sunny" , "aditya" , "prithvi"]

# name = input ( "enter  your name")
# if ( name in list):
#     print(" yes, your name is in list\n. you are selected")
# else:
#     print("no, your  name is not in list so thats why u are not selected")

marks = int(input("enter your percentage"))

if ( marks > 90  ):
    print("grade a")
elif ( marks > 80  ):
    print("grade b")
elif ( marks > 70 ):
    print("grade c")
elif ( marks > 60  ):
    print(" grade e")
else:
    print(" fail")
