def checkWord(word):
    """function that checks if the word is in the EnglishWords.txt file"""
    with open("EnglishWords.txt") as fileEnglish:
        if word in fileEnglish.read().splitlines():
            print(word + " spelt correctly")
        else:
            print(word + " not found in dictionary")

def main():
    """input a sentence to be spell-checked"""
    # open EnglishWords.txt file and remove the white space at the beginning and end of each line
    with open("EnglishWords.txt") as fileEnglish:
        for line in fileEnglish:
            line.strip()

    # input a sentence to check its spelling
    sentence = input ("Enter sentence to spellcheck: ")

    # split the sentence into a list of words
    wordList = sentence.split()

    print("\n")
    for word in wordList:
        checkWord(word)


if __name__ == "__main__":
    main()
