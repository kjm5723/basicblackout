import re
def nameTitles():
    l = []
    newW = '\u2588'
    i = 0
    while i < 5:
        newW += '\u2588'
        i += 1
    s = str(input("Enter plaintext:"))
    for w in s.split():
        if w[0].isupper():
            l.append(w)
    for w in l:
        newS = s.replace(w, newW)
        s = newS
    print(newS)