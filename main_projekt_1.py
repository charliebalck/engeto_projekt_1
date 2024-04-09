"""
main_projekt_1.py: první projekt do Engeto Online Python Akademie

author: Karel Černý
email: karel.cerny@t-mobile.cz
discord: charliebalck
"""
import subprocess
from task_template import TEXTS

dict_users = {"bob": "123", "aaa": "pass123", "mike": "password123 ", "liz": "pass123"}

str_name = input("Přihlašovací jméno: ")
str_password = input("Heslo: ")
print(f"Username: {str_name}\nPassword: {str_password}")
if str_password != dict_users.get(str_name, "N/A"):
    print("Nejste registrovaný uživatel, nebo jste zadali špatné heslo. Program se ukončí.")
else:
    print(
        f"{40 * "-"}"
        f"\nAhoj {str_name},"
        f"\nprogram se hned spustí."
        f"\nPočet textů k analýze: {len(list(TEXTS))}"
        f"\n{40 * "-"}"
    )
    subprocess.run(["python", "text_analyzer.py"])
