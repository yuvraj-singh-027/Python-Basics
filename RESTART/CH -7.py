# here  we solve the practice question based on loop.

# n = int(input("enter the number: "))

# for i in range(1,11):
#     # print( n ,"x", i , "=",n*i)
#     print(f"{n}x{i}={n*i}")


# l = ["Harry", "Soham", "Sachin", "Rahul"] 
# for i in l:
#     if ( i.startswith("S")):
#       print(f"good morning,{i}\nhave a nice day")
   


# using the while loop.
# n = int(input("enter the number: "))
# i=1
# while(i<11):
#     print(f"{n}x{i}={n*i}")
#     i = i +1


# programm to cheak wether  the given number is prime  or not.
# n=int(input("enter the number: "))

# for i in range(2,n):
#     if(n%i)==0:
#         print("this number is not prime")
#         break
#     else:
#         print("this number is prime")
#         break
# write a program to find first n natural number.

# n = int(input("enter the number: "))
# i = 0
# sum = 0
# while(i<n):
#     sum = sum + i
#     i +=1

# print(sum)

# write a programm for find out the factorial of a specific number.

# n = int(input("enter the number: "))
# factorial = 1
# for i in range ( n , 0 ,-1):
#     factorial *= i

# print(f"the factorial of a {n} is {factorial}")





'''
Write a program to print the following star pattern. 
  * 
 *** 
***** for n = 3

'''
# n = 3
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*(2*i -1 ), end=" ")
#     print()

'''
Write a program to print the following star pattern: 
* 
** 
***      for n = 3
'''
n=3
for i in range(1,n+1):
    print("*"*i)