#!/usr/bin/env python

# Argparse will handle the commandline for us.
import argparse
# Used for sorting the dictionary for pretty output.
import operator

def initParse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="The input file. Normally a prose document.")
    parser.add_argument("-o", "--output", help="The output file name, without file extension.")
    parser.add_argument("-wl", "--word-list", help="Define your own list of words to ignore. Seperate with spaces.")
    parser.add_argument("-cl", "--character-list", help="Define your own list of formatting characters to ignore. Seperate with spaces.")
    cliArgs = parser.parse_args()
    return cliArgs

# Escape characters that might occur that we don't care about.
# Current Issue: Doesn't ignore the '#' symbol, because escaping it is a pain in the butt in Python.
def charIgnoreList(cliArgs):
    if cliArgs.character_list:
        characterIgnoreList = fileList(cliArgs.character_list)
    else:
        characterIgnoreList = ['"','.',',',';',':','(',')','{','}','[',']','/','\\','!','-','_','+','=','*','&','^','%','$','@']
    return characterIgnoreList

# A list of common English words to ignore.
def wordIgnoreList(cliArgs):
    if cliArgs.word_list:
        ignoredWordsList = fileList(cliArgs.word_list)
    else:
        ignoredWordsList = ["the","be","to","of","and","a","in","that","have","I","it","for","not","on","with","he","as","you","do","at","this","but","his","by","from","they","we","say","her","she","or","an","will","my","one","all","would","there","their","what","so","up","out","if","about","who","get","which","go","me","when","make","can","like","time","no","just","him","know","take","people","into","year","your","good","some","could","them","see","other","than","then","now","look","only","come","its","over","think","also","back","after","use","two","how","our","work","first","well","way","even","new","want","because","any","these","give","day","most","us"]
    return ignoredWordsList

def buildDict(cliArgs, characterIgnoreList, wordedIgnoreList):
    # Initialise dict
    dictList = {}
    # Open file
    openFile = open(cliArgs.input,'r')
    # Read file, line by lines
    for line in openFile:
        # Read line by word
        words = line.split()
        for word in words:
            # Ignore all upper case
            word = word.lower()
            # If word contains formatting character, remove them.
            for char in characterIgnoreList:
                word = word.replace(char, "")
                # Try and convert to unicode characters
                try:
                    word = unicode(word, 'ascii', 'ignore')
                # Ignore if it's already unicode.
                except TypeError:
                    pass
            # If word in ignore list, skip it.
            if word in wordedIgnoreList:
                pass
            else:
                # If word in dict, increment value by 1
                if word in dictList:
                    dictList[word] = dictList[word] + 1
                # If word not in dict, add to dict
                else:
                    dictList[word] = 1
    # Close file
    openFile.close()
    # Sort dict by most frequently occurring.
    sortedDict = sorted(dictList.items(), key=operator.itemgetter(1),reverse=True)
    # Convert it back to a list
    sortedDict = list(sortedDict)
    # Return dict.
    return sortedDict

def outputList(cliArgs, finalWordList):
    # Print to the console, or an output file.
    if cliArgs.output:
        outFile = open(cliArgs.output, 'w+')
        for word in finalWordList:
            # Because the list is actually a tuple:
            for key in word:
                outFile.write(str(key) + "\n")
        outFile.close()
    else:
        for word in finalWordList:
            # Because the list is actually a tuple:
            for key in word:
                print(key)

def main():
    cliArgs = initParse()
    characterIgnoreList = charIgnoreList(cliArgs)
    wordedIgnoreList = wordIgnoreList(cliArgs)
    wordCountList = buildDict(cliArgs, characterIgnoreList, wordedIgnoreList)
    outputList(cliArgs, wordCountList)

if __name__ == '__main__':
    main()
