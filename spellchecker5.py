from datetime import datetime
import time
import os.path
from difflib import SequenceMatcher

with open("EnglishWords.txt") as fileEnglish:
    """create a cache for time optimization; EnglishWords.txt will be opened just once"""
    cachedWordList = fileEnglish.read().splitlines()
    # remove the white space at the beginning and end of each line
    for word in cachedWordList:
        word.strip()

def checkWord(word):
    """function that checks if the word is in the EnglishWords.txt file"""
    check = word in cachedWordList
    return check


def cleanWord(word):
    """function that sanitizes the word; the new one is made out of lowercase letters, with no special characters"""
    newWord = [letter.lower() for letter in word if letter.isalpha()]
    return "".join(newWord)


def getOutput(wordList, countCorrect, countIncorrect, countIgnored, countAdded, countMarked):
    """function that prints the summary of the process; if it is a sentence then the function will not return ignored,
    added or marked words"""
    output = ""
    output += "\n" + "Number of words: " + str(len(wordList))
    output += "\n" + "Number of correctly spelt words: " + str(countCorrect)
    output += "\n" + "Number of incorrectly spelt words: " + str(countIncorrect)
    if countIgnored == 0 or countIgnored:
        output += "\n" + "  Number ignored: " + str(countIgnored)
    if countAdded == 0 or countAdded:
        output += "\n" + "  Number added to dictionary: " + str(countAdded)
    if countMarked == 0 or countMarked:
        output += "\n" + "  Number marked: " + str(countMarked)
    return output


def getWord(word):
    """function that finds the maximum .ratio() of two words; the bigger the ratio, more similar the words are"""
    max = 0
    suggestedWord =""
    for item in cachedWordList:
        if SequenceMatcher(None, word, item).ratio() > max:
            max = SequenceMatcher(None, word, item).ratio()
            suggestedWord = item
    return suggestedWord


def startMenu():
    print(u'\u250F' + u'\u2501' * 40 + u'\u2513')
    print(u'\u2503' + " " * 40 + u'\u2503')
    print(u'\u2503' + " " * 3 + "S P E L L   C H E C K E R" + " " * 12 + u'\u2503')
    print(u'\u2503' + " " * 40 + u'\u2503')
    print(u'\u2503' + " " * 3 + "\t1. Check File" + " " * 20 + u'\u2503')
    print(u'\u2503' + " " * 3 + "\t2. Check Sentence" + " " * 16 + u'\u2503')
    print(u'\u2503' + " " * 40 + u'\u2503')
    print(u'\u2503' + " " * 3 + "\t0. Quit" + " " * 26 + u'\u2503')
    print(u'\u2503' + " " * 40 + u'\u2503')
    print(u'\u2523' + u'\u2501' * 40 + u'\u251B')


def fileMenu():
    print(u'\u250F' + u'\u2501' * 40 + u'\u2513')
    print(u'\u2503' + " " * 40 + u'\u2503')
    print(u'\u2503' + " " * 3 + "L O A D   F I L E" + " " * 20 + u'\u2503')
    print(u'\u2503' + " " * 40 + u'\u2503')
    print(u'\u2503' + " " * 3 + " Enter the file name" + " " * 17 + u'\u2503')
    print(u'\u2503' + " " * 3 + " then press [enter]:" + " " * 17 + u'\u2503')
    print(u'\u2503' + " " * 40 + u'\u2503')
    print(u'\u2503' + " " * 40 + u'\u2503')
    print(u'\u2523' + u'\u2501' * 40 + u'\u251B')


def suggestionMenu(word):
    print(u'\u250F' + u'\u2501' * 40 + u'\u2513')
    print(u'\u2503' + " " * 40 + u'\u2503')
    print(u'\u2503' + " " * 3 + "W O R D   N O T   F O U N D" + " " * 10 + u'\u2503')
    print(u'\u2503' + " " * 40 + u'\u2503')
    length1 = 33 - len(word)
    print(u'\u2503' + " " * 3 + "\t" + word + " " * length1 + u'\u2503')
    print(u'\u2503' + " " * 40 + u'\u2503')
    print(u'\u2503' + " " * 3 + "\tdid you mean" + " " * 21 + u'\u2503')
    print(u'\u2503' + " " * 40 + u'\u2503')
    length2 = 33 - len(getWord(word))
    print(u'\u2503' + " " * 3 + "\t" + getWord(word) + " " * length2 + u'\u2503')
    print(u'\u2503' + " " * 40 + u'\u2503')
    print(u'\u2523' + u'\u2501' * 40 + u'\u251B')


def incorrectMenu(word):
    print(u'\u250F' + u'\u2501' * 40 + u'\u2513')
    print(u'\u2503' + " " * 40 + u'\u2503')
    print(u'\u2503' + " " * 3 + "W O R D   N O T   F O U N D" + " " * 10 + u'\u2503')
    print(u'\u2503' + " " * 40 + u'\u2503')
    length1 = 33 - len(word)
    print(u'\u2503' + " " * 3 + "\t" + word + " " * length1 + u'\u2503')
    print(u'\u2503' + " " * 40 + u'\u2503')
    print(u'\u2503' + " " * 3 + "\t1. Ignore the word." + " " * 14 + u'\u2503')
    print(u'\u2503' + " " * 3 + "\t2. Mark the word as incorrect." + " " * 3 + u'\u2503')
    print(u'\u2503' + " " * 3 + "\t3. Add word to dictionary" + " " * 8 + u'\u2503')
    print(u'\u2503' + " " * 40 + u'\u2503')
    print(u'\u2523' + u'\u2501' * 40 + u'\u251B')


def checkFile():
    """input a file to be spell-checked"""
    while True:
        # input the correct name of the file; if the file is not found (might be misspelled or doesn't exist), enter the name again
        ok = False
        while not ok:
            fileMenu()
            fileName = input("\u2517\u2501\u2501\u2501 Filename: ")
            if os.path.isfile(fileName):
                ok = True
                startTime = time.time()
            else:
                print("File does not exist. Try again.")

        # open the file to spell-check; clean all words in the list (wordsToCheck)
        with open(fileName, "r") as fileToCheck:
            wordsToCheck = fileToCheck.read().split()
        wordsToCheck = [cleanWord(word) for word in wordsToCheck if cleanWord(word)]

        new = ""
        countCorrect = 0
        countIncorrect = 0
        countIgnored = 0
        countAdded = 0
        countMarked = 0

        # create new file to append the checked text, date and time and summary
        newFile = open("checked_" + fileName, "w")
        for word in wordsToCheck:
            if checkWord(word):
                countCorrect += 1
                new += word + " "
            else:
                countIncorrect += 1
                suggestionMenu(word)
                # if you change the word, the corrected word is added to the new file
                ok = False
                while not ok:
                    change = input("\u2517\u2501\u2501\u2501 Change the word? [y] or [n]: ")
                    if change != "y" and change != "n":
                        print("Choose either [y] or [n]")
                    elif change == "y":
                        countIncorrect -= 1
                        countCorrect += 1
                        new += getWord(word) + " "
                        ok = True
                    # if you don't change the word, you can choose from three different options
                    elif change == "n":
                        incorrectMenu(word)
                        # check if the input is either 1, 2 or 3
                        while True:
                            choice = input("\u2517\u2501\u2501\u2501 Enter choice: ")
                            try:
                                choice = int(choice)
                                if choice == 1:
                                    # ignore the word
                                    new += "!" + word + "! "
                                    countIgnored += 1
                                    break
                                elif choice == 2:
                                    # mark the word
                                    new += "?" + word + "? "
                                    countMarked += 1
                                    break
                                elif choice == 3:
                                    # add the word to the EnglishWords.txt file
                                    dictFile = open("EnglishWords.txt", "a")
                                    # update dictionary at each iteration (so that the spell-checker works even if you don't exit the program)
                                    cachedWordList.append(word)
                                    dictFile.write("\n" + word)
                                    new += "*" + word + "* "
                                    countAdded += 1
                                    dictFile.close()
                                    break
                                else:
                                    print("Choose either 1, 2 or 3: ")
                            except ValueError:
                                print("Choose either 1, 2 or 3: ")
                        ok = True

        newFile.write(str(datetime.now().strftime("%d-%m-%Y %H:%M")))
        newFile.write(getOutput(wordsToCheck, countCorrect, countIncorrect, countIgnored, countAdded, countMarked) + "\n\n")
        newFile.write(new + "\n")
        newFile.close()
        print(getOutput(wordsToCheck, countCorrect, countIncorrect, countIgnored, countAdded, countMarked))
        timeDelta = time.time() - startTime
        print("\nTime elapsed " + str(timeDelta) + " seconds")
        key = input("\nPress q [enter] to quit or any other key [enter] to go again: ")
        if key == 'q':
            break
        else:
            continue


def checkSentence():
    """input a sentence to be spell-checked"""
    while True:
        # input a sentence to check its spelling
        sentence = input("Enter sentence to spellcheck: ")
        print("\n")

        # put words in a a list and then clean the list (wordList)
        wordList = sentence.split()
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
        print(getOutput(wordList, countCorrect, countIncorrect, None, None, None))

        key = input("\nPress q [enter] to quit or any other key [enter] to go again: ")
        if key == 'q':
            break
        else:
            continue


def main():
    while True:
        # print the choice menu using Unicode
        startMenu()
        choice = input("\u2517\u2501\u2501\u2501 Enter choice: ")
        # check if the input is either 0, 1 or 2
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
