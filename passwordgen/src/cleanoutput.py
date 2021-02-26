import os

files = os.listdir('output')
for i in files:
    this_path = 'output/' + i
    this_file = open(this_path)
    print(this_path)
    if os.stat(this_path).st_size == 0:
        os.remove(this_path)
        print('deleted')
    else: this_file.close()