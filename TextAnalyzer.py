import re
from tabulate import tabulate
import task_template

strText = ""
strKey = ""
intWords = 0
intTitlecase = 0
intLowercase = 0
intNumeric = 0
intSum = 0
dictLen = {}

for Try in range(5):
    strInput = input("Vložte číslo textu (1 - " + str(len(list(task_template.TEXTS))) + ") k analýze: ")
    if strInput.isnumeric():
        if int(strInput) <= 3:
            strText = list(task_template.TEXTS)[int(strInput) - 1].strip()
            print(40 * "-", "Vybral jsi tento text:", strText, 40 * "-", sep="\n")
            break
        else:
            print('"' + strInput + '" není číslo z rozsahu 1 - 3, zkus to prosím znovu!')
    else:
        print('"' + strInput + '" není číslo, zkus to prosím znovu!')

    if int(Try) == 4:
        print("Byli vyčerpány všechny pokusy o výběr!")

if strText != "":
    intWords = len(strText.split())
    for word in strText.split():
        if len(re.sub('[^a-zA-Z0-9]', '', word)) < 10:
            strKey = "0"
        else:
            strKey = ""
        strKey = "Char" + strKey + str(len(re.sub('[^a-zA-Z0-9]', '', word)))
        if strKey in dictLen.keys():
            dictLen[strKey] = dictLen[strKey] + 1
        else:
            dictLen[strKey] = 1
        if sum(1 for x in word if x.isupper()) == 1:
            intTitlecase = intTitlecase + 1
            continue
        if sum(1 for x in word if x.islower()) == len(re.sub('[^a-zA-Z0-9]', '', word)):
            intLowercase = intLowercase + 1
            continue
        if word.isnumeric():
            intNumeric = intNumeric + 1
            intSum = intSum + int(word)
            continue
    print("V textu je " + str(intWords) + " slov, z toho:",
          str(intTitlecase) + " slov začínajících velkým písmenem,",
          str(intWords - intTitlecase - intLowercase - intNumeric) + " slov psaných velkými písmeny,",
          str(intLowercase) + " slov psaných malými písmeny,",
          str(intNumeric) + " čísla, a jejich součet je: " + str(intSum) + ".",
          40*"-",
          sep="\n")
    dictLen = dict(sorted(dictLen.items()))
    head = ["LEN", "OCCURENCES", "NR."]
    mydata = []
    for x in dictLen:
        mydata.append([list(dictLen).index(x) + 1, dictLen[x]*"*", dictLen[x]])
    print(tabulate(mydata, colalign=("right", "left", "left"), headers=head, tablefmt="presto"))
