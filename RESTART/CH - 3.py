# using input function and put the input value into print without write it into the print.
name = input("enter  the  name ")
print("🙌 GOOD MORNING,", name )


# using replace function to change  the specific word.
letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 
print(letter.replace("<|Name|>","YUVRAJ").replace("<|Date|> ","26 NOV 2025"))

# FIND THE DOUBLE SPACE BETWEEN THE  SENTENCE.

name = " there are many peoples over   there"
print(name.replace("  ",""))


# using the escape sequence
letter = "Dear Harry\t, \nthis python course is nice\n. Thanks!"
print(letter)
