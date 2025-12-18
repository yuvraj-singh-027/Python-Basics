
# in this we will gonna study about the file handling and file input\output 
st = "there might be too much work to do"
f = open("file.txt","w")
data = f.write(st)



''' readline function '''
f = open("file.txt")
line2 = f.readline()
line3 =  f.readline()
print(line2)
print(line3)


# using open function with different modes - "r" , "w" . " a"
f= open("file.txt",'r')
f2=open("HELLO.txt",'w')
data= f.readlines()
print(data)
f.close()
f.write("\nthis side yuvraj speaking\n")
f.seek(2)
f.write("i m writting the programm")
print("append process successful")
f.close ()

# small programm 
ch = "Y"
f=open("file.txt",'a')
while ch == 'y' or ch == "Y":
    name = input("enter the name: ")
    age= int(input("enter the age: "))
    f.write(name)
    f.write("\n")
    f.write(str(age))
    f.write("\n")
    print("data save successfully")
    ch = input("you wanted to add more data Y/N: ")
f.close()
data = f.read()
f2.write(data)
print("data has been copied successfullyt")
 
#  work with binary file 
import pickle 
data = [ 1,2,3,4]
with open("hello.bin","wb") as fobj:
    pickle.dump(data,fobj)
with open("hello.bin","rb") as fobj:
   data = pickle.load(fobj)

print(fobj)

# using in statement 
with open("file.txt",'r') as f1:
 content = f1.read()
 
if ( " sunny "  in  content ):
    print("yes word - 'sunny' is present in this file")

else :
      print("yes word - 'sunny' is not present in this file")


# lets make a small game 
import random

def game():
    print("THE GAME HAS BEEN START......")
    score = random.randint(1,100)
    with open('hiscore1.txt','r') as  f1:
        HIGH_SCORE = f1.read()
        if (HIGH_SCORE != ""):
            HIGH_SCORE = int(HIGH_SCORE)
        else :
            HIGH_SCORE = 0
    print(f"you score:{score}")
    
    if (HIGH_SCORE < score):
        with open('hiscore1.txt',"w") as  f2:
          f2.write(f"high score ,{str(score)}")
    
    return score

game()


#  this program is used to print the table from 2 to 21.
def genrator (n):
    table = " "
    for i in range (1,11):
        table += f"{n} x {i} = { n * i}\n"
    
    f1 = open(f"Tables2/table_{n}.txt","w")
    f1.write(table)


for i in range(2,21):
    genrator(i)


# replace specific word from another file

with open("HELLO.txt",'r') as f1:
 data = f1.read()

content = data.replace("donkey","####")

with open("HELLO.txt","w") as f2:
  f2.write(content)



# this program is used to sensored bad words from comment section.
words = [ "donkey", "bad", " ganda" , "bure"]
with open("HELLO.txt",'r') as f1:
 data = f1.read()

for word in words:
 data = data.replace(word,"#"* len(word))

with open("HELLO.txt","w") as f2:
  f2.write(data)



# program to cheak that a specific word is in a file or not.

word = " python "

with open ("HELLO.txt", "r") as f1:
    data = f1.read()
    
if word in data:
    print("yes, there is present the word python")

else :
    print("no, there is no present the word python")


# write a program to findout the line no of where a specific word present.

word = " python"
with open("HELLO.txt") as f1:
    data = f1.readlines()
   
    lineno = 1
    for line in data:
        if ( word in line  ):
            print(f"yes, the {word} is present in line no - {lineno}")
            break 
            lineno += 1
    else :
        print("sorry to say but the word is not present in the file ")


# now we gonna copy the data from one file to another file.

with open ("HELLO.txt","r") as f1:
    data = f1.read()
with open ("file.txt", "w") as f2:
    f2.write(data)
print (" data has been successfully copied")