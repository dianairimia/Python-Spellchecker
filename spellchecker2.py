with open("EnglishWords.txt") as fileEnglish:
    cachedWordList = fileEnglish.read().splitlines()

def checkWord(word):
    """function that checks if the word is in the EnglishWords.txt file"""
    check = word in cachedWordList
    if check:
        print(word + " spelt correctly")
    else:
        print(word + " not found in dictionary")
    return check

def cleanWord(word):
    """function that sanitizes the word; the new one is made out of lowercase letters, with no special characters"""
    newWord = [letter.lower() for letter in word if letter.isalpha()]
    return "".join(newWord)


def printOutput(wordList, countCorrect, countIncorrect):
    print("\n")
    # number of words
    print("Number of words: " + str(len(wordList)))
    # number of correctly spelt words
    print("Number of correctly spelt words: " + str(countCorrect))
    # number of words that are not found in the dictionary
    print("Number of incorrectly spelt words: " + str(countIncorrect))


def main():
    """input a sentence to be spell-checked"""
    while True:
        # open EnglishWords.txt file and remove the white space at the beginning and end of each line
        with open("EnglishWords.txt") as fileEnglish:
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

        countCorrect = 0
        countIncorrect = 0
        for word in wordList:
            if checkWord(word):
                countCorrect += 1
            else:
                countIncorrect += 1
        printOutput(wordList, countCorrect, countIncorrect)
        key = input("Press q [enter] to quit or any other key [enter] to go again: ")
        if key == 'q':
            break
        else:
            continue


if __name__ == "__main__":
    main()
