# -*-coding:Latin-1 -*

import re

search = re.search(r"abc", "abcdef")
search1 = re.search(r"abc*", "abdef")

number = ""
regex = r"^0[1-9](-[0-9]{2}){4}$"

#while re.match(regex, number) is None:
#    number = input("Entrez un Numero Valide: ")

text = """
nom='Task1, id=8
nom='TAsk2', id=31
nom='Task3', id=127"""

print(re.sub(r"id=(?P<id>[0-9]+)", r"id[\g<id>]", text))

password_regex = r"^([A-Za-z0-9]){6,}$"
password = ""

# compil regex

chn_pwd = r"^([A-Za-z0-9]){6,}$"
exp_pwd = re.compile(chn_pwd)

while exp_pwd.search(password) is None:
    password = input("Password :")



