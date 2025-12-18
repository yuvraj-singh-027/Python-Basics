# using list methods so we can modify it as per need. 
list = [ "yuvraj", 667, False, 45.67]

print(list)
print(list[0])
list.append(78)
list.remove("yuvraj")
print(list)
list2 = ["sunny", "hagimuti"]
list.extend(list2)
print(list)

# tuple

tuble = ()
tuple = ("sunny",)
print(type(tuple))
print(type(tuble))

tuple2 = ("yuvraj", "sunny" ,"aditya","neerav")

tuple2.append("sheryash")
print(tuple2)


# practice question.

list1= []
item1 = int(input("enter the item name"))
list1.append(item1)
item2 = int(input("enter the item name"))
list1.append(item2)
item3 = int(input("enter the item name"))
list1.append(item3)
item4 = int(input("enter the item name"))
list1.append(item4)
item5 = int(input("enter the item name"))
list1.append(item5)
item6 = int(input("enter the item name"))
list1.append(item6)
item7 = int(input("enter the item name"))
list1.append(item7)

list1.sort()

print(list1)
print(sum(list1))



tuple1 = ( " yuvraj" , "sunny")
tuple1[1] = "hagu"
print(tuple1)

a = (7, 0, 8, 0, 0, 9) 
print(a.count(0))