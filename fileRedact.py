import re


def fileRedact():
    l = []
    newW = '*'
    i = 0
    while i < 5:
        newW += '*'
        i += 1
    f = str(input("Enter file name:"))
    w = str(input("Enter word you wish to censor (type STOP to end entry mode): "))
    while w != "STOP":
        l.append(w)
        w = str(input("Enter word you wish to censor (type STOP to end entry mode): "))
    fileName = input("Enter the name of the output file: ")
    o = open(fileName, "a")
    for line in open(f):
            for w in l:
                line = line.replace(w,newW)
                o.write(line+"\n")
    o.close()

