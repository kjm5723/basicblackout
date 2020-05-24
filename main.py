import fileRedact
import multWords
import nameTitles

if __name__ == "__main__":
    print("Welcome to Basic Blackout, a censoring software.")
    mode = input(
        "What mode would you like to use? \n [A] Manual Word Entry \n [B] Names and Titles\n [C] File \n Mode: ")
    if mode == 'A':
        multWords.multWords()
    elif mode == 'B':
        nameTitles.nameTitles()
    elif mode == 'C':
        fileRedact.fileRedact()
