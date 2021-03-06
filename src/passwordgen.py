import random
import os
import sys
import time
os.system('cls' if os.name == 'nt' else 'clear')
printing = True
characters = {
    "lowercase": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
    "uppercase": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
    "numbers": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ],
    "characters": ["!", "@", "#", "$", "%", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "<", ">", ",", ".", "/", "?"]
}
if not os.path.isdir("output"):
    os.mkdir('output')
if not os.path.isfile('config.passgen'): chars = characters["lowercase"] + characters["uppercase"] + characters["numbers"] + characters["characters"]
else:
    chars = open('config.passgen').read().splitlines()
    print("Loaded custom config")
file_name = "output/" + str(time.time()) + ".passes"
output = open(file_name, "a")
passwords = []
chars = characters["lowercase"] + characters["uppercase"] + characters["numbers"] + characters["characters"]
count = int(input("Count: "))
length = int(input("Length: "))
doubles = 0

def calculate_size():
    size = count * length
    kb_size = size / 1024
    mb_size = kb_size / 1024
    return str(mb_size) + " MB (" + str(size) + " bytes)"

def generate_password(length):
    letters = []
    for x in range (length):
        letters.append(random.choice(chars))
    password = ''.join(letters)
    return password

def generate_list(count, length, printing):
    for i in range(count):
        password = generate_password(length)
        if password in passwords:
            global doubles
            doubles += 1
            print(str(i + 1) + ": Double detected (" + str(doubles) + " doubles) ('" + password + "')")
            continue
        passwords.append(password)
        output.write(password + "\n")
        if printing == True: print(str(i + 1) + ":  " + password)

        
print("The file will be " + str(calculate_size()))
size_check = input("Do you want to continue? [Default: True] Y/N ")
if size_check == "N": exit()
if size_check == "n": exit()

print_check = input("Do you want to print the passwords(slower) [Default: True] Y/N ")
isPrinting = True
if print_check == "N": isPrinting = False
if print_check == "n": isPrinting = False

print("Generating " + str(count) + " passwords with length " + str(length))
start_time = time.time()

generate_list(count, length, isPrinting)
end_time = time.time()
total_time = end_time - start_time
print("Done")

print("Finished in " + str(total_time * 1000) + " miliseconds")
print("(" + str((total_time / count) * 1000) + " miliseconds per password on avarage)")
print(str(doubles) + " doubles detected")
output.close()
input("Press enter to continue")