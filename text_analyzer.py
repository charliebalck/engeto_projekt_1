import re
from tabulate import tabulate
from task_template import TEXTS

str_text = ""
int_words = 0
int_titlecase = 0
int_lowercase = 0
int_numeric = 0
int_sum = 0
dict_len = {}

for Try in range(6):
    if Try == 5:
        print("Byli vyčerpány všechny pokusy o výběr!")
        break
    elif (str_input := input(f"Vložte číslo textu (1 - {len(list(TEXTS))}) k analýze: ")).isdigit():
        if int(str_input) <= 3:
            str_text = list(TEXTS)[int(str_input) - 1].strip()
            print(
                f"{40 * "-"}"
                f"\nVybral jsi tento text:"
                f"\n{str_text}"
                f"\n{40 * "-"}"
            )
            break
        else:
            print(f"'{str_input}' není číslo z rozsahu 1 - 3, zkus to prosím znovu!")
    else:
        print(f"'{str_input}' není číslo, zkus to prosím znovu!")

if str_text != "":
    int_words = len(str_text.split())
    for word in str_text.split():
        str_word = re.sub('[^a-zA-Z0-9]', '', word)
        dict_len[len(str_word)] = dict_len.get(len(str_word), 0) + 1
        if str_word.isdigit():
            int_numeric = int_numeric + 1
            int_sum = int_sum + int(str_word)
            continue
        elif str_word.islower():
            int_lowercase = int_lowercase + 1
            continue
        elif (str_word[:1].isupper() and str_word[1:].islower()) or str_word[:1].isdigit():
            int_titlecase = int_titlecase + 1
            continue
    print(
        f"V textu je {int_words} slov, z toho:"
        f"\n{int_titlecase} slov začínajících velkým písmenem,"
        f"\n{int_words - int_titlecase - int_lowercase - int_numeric} slov psaných velkými písmeny,"
        f"\n{int_lowercase} slov psaných malými písmeny,"
        f"\n{int_numeric} čísla, a jejich součet je: {int_sum}."
        f"\n{40*"-"}"
    )
    dict_len = dict(sorted(dict_len.items()))
    head = ["LEN", "OCCURENCES", "NR."]
    mydata = []
    for x in dict_len:
        mydata.append([x, dict_len[x] * "*", dict_len[x]])
    print(tabulate(mydata, colalign=("right", "left", "left"), headers=head, tablefmt="presto"))
