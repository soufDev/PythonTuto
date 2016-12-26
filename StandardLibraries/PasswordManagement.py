# -*-coding:Latin-1 -*

import hashlib
from getpass import getpass


password = b"azerty"
encrypted_password = hashlib.sha1(password).hexdigest()

lock = True
while lock:
    enter = getpass("Enter password : ")
    enter = enter.encode()

    encrypted_enter = hashlib.sha1(enter).hexdigest()
    if encrypted_enter == encrypted_password:
        lock = False
    else:
        print("Incorect Password")

print("Password Accepted...")


