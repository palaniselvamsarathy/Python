# We have to import a module called 're'

import re
str = input("Enter Name:")

matcher = re.finditer('[ab]',str)

for match in matcher:
    print(match.start(),'...',match.end(),'...',match.group())