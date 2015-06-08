#!/usr/bin/env python

# Argparse will handle the commandline for us.
import argparse

def init_parse():
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
        ignoredWordsList = ["be","to","of","and","a","in","that","have","I","it","for","not","on","with","he","as","you","do","at","this","but","his","by","from","they","we","say","her","she","or","an","will","my","one","all","would","there","their","what","so","up","out","if","about","who","get","which","go","me","when","make","can","like","time","no","just","him","know","take","people","into","year","your","good","some","could","them","see","other","than","then","now","look","only","come","its","over","think","also","back","after","use","two","how","our","work","first","well","way","even","new","want","because","any","these","give","day","most","us"]
    return ignoredWordsList

def fileList(fileInput):
    openFile = open(fileInput, 'r')
    # Initiate the word list that we'll be building from the input file.
    wordList = []
    # Iterate through the file we opened earlier.
    for line in openFile:
    # Let's split each word apart into a list.
        words=line.split()
        for word in words:
            word = word.lower()
            wordList.append(word)
    # Close the file once everything is in memory.
    openFile.close()
    # Remove all duplicate words.
    wordList = list(set(wordList))
    # Alphabetise the list naively.
    wordList.sort()
    return wordList

# This function will output our final list for us.
def outputList(cliArgs, finalWordList):
    # Alphabetise our final list.
    finalWordList.sort()
    # Print to an output file.
    if cliArgs.output:
        outFile = open(cliArgs.output, 'w+')
        for word in finalWordList:
            outFile.write(word + "\n\n")
        outFile.close()
    else:
        # Or to the console.
        for word in finalWordList:
            print(word)

# This function strips out the formatting characters for us.
def removeFormat(wordList, formatCharsList):
    newWordList = []
    for word in wordList:
        for char in formatCharsList:
            word = word.replace(char, "")
            try:
                # Try and encode it to unicode
                word = unicode(word, 'ascii', 'ignore')
            except TypeError:
                # But don't particularly care if it fails.
                pass
        newWordList.append(word)
    return newWordList

def removeCommon(wordList, wordIgnoreList):
    wordList = list(set(wordList).difference(wordIgnoreList))
    return wordList

def main():
    cliArgs = init_parse()
    characterIgnoreList = charIgnoreList(cliArgs)
    wordedIgnoreList = wordIgnoreList(cliArgs)
    basicWordList = fileList(cliArgs.input)
    formattedWordList = removeFormat(basicWordList, characterIgnoreList)
    removedCommonWordsList = removeCommon(formattedWordList, wordedIgnoreList)
    finalWordList = removedCommonWordsList
    outputList(cliArgs, finalWordList)

if __name__ == '__main__':
    main()
