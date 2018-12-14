#John Hedrick
#References:
#https://www.datacamp.com/community/tutorials/functions-python-tutorial
#http://www.endmemo.com/python/lowercase.php

# ordinal of [A, Z] = [65, 90]
# ordinal of [a, z] = [97, 122]

#takes the input of a word with lowercase and/or uppercase letters and rotates
#it a specified number of places

print("Input word:")
message = str(input(" "))
print("How many letters do you wish to rotate by?")
integer = int(input(" "))
print("Rotated word:")
        
def rotate_word(message,integer):
    for i in message:
        num = ord(i)
        num += integer
        for letter in message:
            if letter.isupper():
                while num > 90:
                    num -= 26
                while num < 65:
                    num += 26
            elif letter.islower():
                while num > 122:
                    num -= 26
                while num < 97:
                    num+=26
        print(chr(num), end='')
    return("")
print(rotate_word(message,integer))
