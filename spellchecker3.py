from datetime import datetime
from time import process_time_ns
import os.path

with open("EnglishWords.txt") as fileEnglish:
    # create a cache for time optimization; the file will be opened just once, not for each iteration of checkWord(word)
    cachedWordList = fileEnglish.read().splitlines()

def checkWord(word):
    """function that checks if the word is in the EnglishWords.txt file"""
    check = word in cachedWordList
    return check

def cleanWord(word):
    """function that sanitizes the word; the new one is made out of lowercase letters, with no special characters"""
    newWord = [letter.lower() for letter in word if letter.isalpha()]
    return "".join(newWord)


def getOutput(wordList, countCorrect, countIncorrect):
    output = ""
    output += "\n" + "Number of words: " + str(len(wordList))
    output += "\n" + "Number of correctly spelt words: " + str(countCorrect)
    output += "\n" + "Number of incorrectly spelt words: " + str(countIncorrect)
    return output


def checkFile():
    while True:
        """input a file to be spell-checked"""
        # input the name of the file you want to spell-check
        # try catch if the input is wrong DON'T KNOW HOW TRY CATCH WORKS FOR PYTHON - FIGURE IT OUT FOR THE MENU FIRST
        ok = False
        while ok == False:
            fileName = input("Enter the name of the file to spellcheck: ")
            if  os.path.isfile(fileName):
                ok = True
                startTime = process_time_ns()
            else:
                print("File does not exist. Try again.")

        with open(fileName, "r") as fileToCheck:
            wordsToCheck = fileToCheck.read().split()
        # clean all words in wordList
        wordsToCheck = [cleanWord(word) for word in wordsToCheck if cleanWord(word)]
        new = ""
        countCorrect = 0
        countIncorrect = 0

        # create new file to append the checked text, date and time and summary
        newFile = open("checked_" + fileName, "w")
        for word in wordsToCheck:
            if checkWord(word):
                countCorrect += 1
                new += word + " "
            else:
                countIncorrect += 1
                new += "?" + word + "? "

        newFile.write(str(datetime.now().strftime("%d-%m-%Y %H:%M")))
        newFile.write(getOutput(wordsToCheck, countCorrect, countIncorrect) + "\n\n")
        newFile.write(new + "\n")
        newFile.close()
        print(getOutput(wordsToCheck, countCorrect, countIncorrect))
        # elapsed time is the actual time minus the time the process started IN MICROSECONDS !!!
        timeDelta = process_time_ns() - startTime
        print("\nTime elapsed " + str(int(timeDelta/1000)))
        key = input("\nPress q [enter] to quit or any other key [enter] to go again: ")
        if key == 'q':
            break
        else:
            continue


def checkSentence():
    """input a sentence to be spell-checked"""
    while True:
        # open EnglishWords.txt file and remove the white space at the beginning and end of each line
        with open("EnglishWords.txt") as fileEnglish: # TODO should be handled when cachedWordList is created
            for line in fileEnglish:
                line.strip()
        # input a sentence to check its spelling
        sentence = input("Enter sentence to spellcheck: ")
        print("\n")
        # split the sentence into a list of words
        wordList = sentence.split()

        # clean all words in wordList
        wordList = [cleanWord(word) for word in wordList if cleanWord(word)]
        for word in wordList:
            print(word, end=" ")
        print("\n")

        # get output
        countCorrect = 0
        countIncorrect = 0
        for word in wordList:
            if checkWord(word):
                countCorrect += 1
                print(word + " spelt correctly")
            else:
                countIncorrect += 1
                print(word + " not found in dictionary")
        print(getOutput(wordList, countCorrect, countIncorrect))

        key = input("\nPress q [enter] to quit or any other key [enter] to go again: ")
        if key == 'q':
            break
        else:
            continue


def main():
    while True:
        print("S P E L L   C H E C K E R", "\n")
        print("\t1. Check a file", "\t2. Check a sentence\n", "\t0. Quit", sep="\n")
        print("\n")
        choice = input("Enter choice: ")
        try:
            choice = int(choice)
            if choice == 0:
                break
            elif choice == 1:
                checkFile()
            elif choice == 2:
                checkSentence()
            else:
                print("Choose either 0, 1 or 2")
        except ValueError:
            print("Choose either 0, 1 or 2")


if __name__ == "__main__":
    main()

