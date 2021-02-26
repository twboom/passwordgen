import os
import sys
import time
os.system('cls' if os.name == 'nt' else 'clear')
if not os.path.isdir('output'):
    os.mkdir('output')
if not os.path.isdir('combinedfiles'):
    os.mkdir('combinedfiles')
files = os.listdir('output')
path = 'combinedfiles/' + str(time.time()) + ".passes"
combined = open(path, "a")
passwords = []
duplicates = 0
start_time = time.time()

def duplicatesCounter(password):
    global duplicates
    duplicates += 1
    print("Duplicate found: " + str(password))
    print(str(duplicates) + " duplicates")

print('Starting merging ' + str(len(files)) + ' files')

for single in files:
    this_path = 'output/' + single
    this_file = open(this_path)
    lines = this_file.read().splitlines()
    for line in lines:
        if line not in passwords:
            passwords.append(line)
            combined.write(line + '\n')
        else:
            duplicatesCounter(line)
            continue
    print('Finished "' + single + '"')

print('Done')
print('Merged ' + str(len(files)) + ' files in ' + str(time.time() - start_time) + ' seconds')
input('Press enter to exit')