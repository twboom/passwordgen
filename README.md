# PasswordGen
Generating passwords...

## How to use PasswordGen
**Currently the only way to use it is running the python file (`passwordgen.py`), this requires you to have python installed.**

1. Download and open the file, it should show a CLI now
2. Enter how many passwords you would like to generate
3. Enter how long the passwords should be
4. Accept if the file size is not too big for you. **Please note: it might not be 100% accurate**
5. Wait until it finished.
6. It now has created an folder in the same directory as your python file, in that folder the output will appear. The highest number is always the latest file.

If you want to use a custom set of characters, create a file name `config.passgen` in the same directory as the python file. In that file you have to specify every single character on a seperate line. When running the script, your custom characters are not added to the built-in list, but override the built-in list.