import random
import os

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

def generate_pass():
    for i in range(count):
        letters = []
        for x in range(length):
            letters.append(random.choice(chars))
        password = ''.join(letters)
        if password in passwords:
            global doubles
            doubles += 1
            print("Double detected (" + str(doubles) + ")")
        else:
            output.write(password + '\n')
            passwords.append(password)
        

print("Generating " + str(count) + " passwords with length " + str(length))
print(doubles)
generate_pass()
print(str(doubles) + " doubles detected")