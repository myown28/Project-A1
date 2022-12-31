#~~~ Pratham-code ~~~
#~~~ IMPORT ~~~
from getpass import getpass
import time
import os

#~~~ DEF ~~~


#~~~ MAIN-CODE ~~~
os.system("cls")
print("MAIN-CODE")
login1 = input("login-user\n")
if login1 == 'Pratham':
    time.sleep(2)
    login2 = getpass("password\n")
    if login2 == '2006':
        time.sleep(2)
        print("all program\n")
        print("""
        
        """)

    else:
        print("ERROR\n")
else:
    print("ERROR\n")