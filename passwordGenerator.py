""""
import random

lower_case= "abcdefghijklmnopqrstuvxyz"
upper_case= "ABCDEFGHIJKLMNOPQRSTUVXYZ"
symbols= "!#$%&/()=?¡.,]['*]"
numbres= "0123456789"

def knew_password(longitud):
    all_characters= lower_case+upper_case+symbols+numbres
    password= ""
    for _ in range(longitud):
        password += random.choice(all_characters)
    return password

nueva_password= knew_password(10)
print(nueva_password)
"""


######---------------- Strong Password Generator ---------------##############

import secrets
import string

def crearPassword(longitud):
    todoCaracter= string.ascii_letters + string.digits + string.punctuation
    contra = ""
    for _ in range(longitud):
        contra += secrets.choice(todoCaracter)
    return contra
pass_nuevo = crearPassword(20)
print(pass_nuevo)
