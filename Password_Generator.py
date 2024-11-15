import random
import string

def gen_password(length, complexity):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    symbols = string.punctuation

    if complexity == 1:
         character = lower
    elif complexity == 2:
         character = lower + upper    
    elif complexity == 3:
         character = lower + upper + digit 
    elif complexity == 4:
         character = lower + upper + digit + symbols
    else:
         return("Invalid Complexity level")    
    
    password = "".join(random.choice (character) for _ in range(length))
    return password

length = int(input("Enter the length of the password :"))
print("Complexity LEvel \n1: lowercase only \n2: lowercase + upper \n3: lowercase + uppercase + digit  \n4: lowercase + uppercase + digit + symbols")
complexity = int(input("Enter the complexity level(1-4):"))
password = gen_password(length, complexity)
print("Generated password : ", password)