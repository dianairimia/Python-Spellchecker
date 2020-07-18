from datetime import datetime
import os.path

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
    output = ""
    output += "\n" + "Number of words: " + str(len(wordList))
    output += "\n" + "Number of correctly spelt words: " + str(countCorrect)
    output += "\n" + "Number of incorrectly spelt words: " + str(countIncorrect)
    if countIgnored:
        output += "\n" + "  Number ignored: " + str(countIgnored)
    if countAdded:
        output += "\n" + "  Number added to dictionary: " + str(countAdded)
    if countMarked:
        output += "\n" + "  Number marked: " + str(countMarked)
    return output


def checkFile():
    """input a file to be spell-checked"""
    while True:
        # input the correct name of the file; if the file is not found (might be misspelled), enter the name again
        ok = False
        while not ok:
            fileName = input("Enter the name of the file to spellcheck: ")
            if os.path.isfile(fileName):
                ok = True
                startTime = datetime.now()
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
                print("\n" + word + " not found \n")
                print("1. Ignore the word", "2. Mark the word as incorrect", "3. Add word to dictionary", sep="\n")
                # check if the input is either 1, 2 or 3
                while True:
                    choice = input("\nEnter choice: ")
                    try:
                        choice = int(choice)
                        if choice == 1:
                            new += "!" + word + "! "
                            countIgnored += 1
                            break
                        elif choice == 2:
                            new += "?" + word + "? "
                            countMarked += 1
                            break
                        elif choice == 3:
                            dictFile = open("EnglishWords.txt", "a")
                            # update dictionary at each iteration
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

        newFile.write(str(datetime.now().strftime("%d-%m-%Y %H:%M")))
        newFile.write(getOutput(wordsToCheck, countCorrect, countIncorrect, countIgnored, countAdded, countMarked) + "\n\n")
        newFile.write(new + "\n")
        newFile.close()
        print(getOutput(wordsToCheck, countCorrect, countIncorrect, countIgnored, countAdded, countMarked))
        timeDelta = datetime.now() - startTime
        print("\nTime elapsed " + str(timeDelta.microseconds) + " microseconds")
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
        print("S P E L L   C H E C K E R", "\n")
        print("\t1. Check a file", "\t2. Check a sentence\n", "\t0. Quit", sep="\n")
        print("\n")
        choice = input("Enter choice: ")
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

