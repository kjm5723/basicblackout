import re


def multWords():
    l = []
    newW = '\u2588'
    i = 0
    while i < 5:
        newW += '\u2588'
        i += 1
    s = str(input("Enter plaintext:"))
    w = str(input("Enter word you wish to censor (type STOP to end entry mode): "))
    while w != "STOP":
        l.append(w)
        w = str(input("Enter word you wish to censor (type STOP to end entry mode): "))
    for c in l:
        c = re.compile(c, re.IGNORECASE)
        newS = c.sub(newW, s)
        s = newS
    print(newS)
