import random
import os
import sys

os.system('cls' if os.name == 'nt' else 'clear')

f = open("output.txt", "w")
f.write("")
output = open("output.txt", "a")
passwords = []

characters = {
    "lowercase": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
    "uppercase": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
    "numbers": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ],
    "characters": ["!", "@", "#", "$", "%", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "<", ">", ",", ".", "/", "?"]
}

chars = characters["lowercase"] + characters["uppercase"] + characters["numbers"] + characters["characters"]

count = int(input("Count: "))
length = int(input("Length: "))
doubles = 0

def calculate_size():
    size = count * length
    
    if size % 1000 == range:
        content = str(size / 1000) + " KB (" + str(size) + " bytes)"
        return content

    if size % 1000000 == 0:
        content = str(size / 1000000) + " MB (" + str(size) + " bytes)"
        return content
    
    if size % 1000000000 == 0:
        content = str(size / 1000000000) + " GB (" + str(size) + " bytes)"
        return content
    
    if size % 1000000000000 == 0:
        content = str(size / 1000000000000) + " TB (" + str(size) + " bytes)"
        return content
    
    else:
        return str(size) + " bytes"

def generate_pass():
    for i in range(count):
        letters = []
        for x in range(length):
            letters.append(random.choice(chars))
        password = ''.join(letters)
        print(str(i + 1) + ": " + password)
        if password in passwords:
            global doubles
            doubles += 1
            print("Double detected (" + str(doubles) + ")")
        else:
            output.write(password + '\n')
            passwords.append(password)
        
print("The file will be " + str(calculate_size()))
size_check = input("Do you want to continue? Y/N ")
if size_check == "N": exit()
if size_check == "n": exit()
print("Generating " + str(count) + " passwords with length " + str(length))
generate_pass()
print("Done")
print(str(doubles) + " doubles detected")
input("Press enter to continue")