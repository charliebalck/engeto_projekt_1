"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Karel Černý
email: karel.cerny@t-mobile.cz
discord: charliebalck
"""
import subprocess
import task_template

name = input("Přihlašovací jméno: ")
password = input("Heslo: ")
users = {"bob": "123", "aaa": "pass123", "mike": "password123 ", "liz": "pass123"}
print("Username: " + name, "Password: " + password, sep="\n")
if name in users:
    if password == users[name]:
        print(40 * "-",
              "Ahoj " + name + ",",
              "program se hned spustí.",
              "Počet textů k analýze: " + str(len(list(task_template.TEXTS))),
              40 * "-", sep="\n"
              )
        subprocess.run(["python", "TextAnalyzer.py"])
    else:
        print("Ahoj " + name + ", zadal jsi špatné heslo, program se ukončí.")
else:
    print("Nejste registrovaný uživatel, program se ukončí.")
