#!/usr/bin/env python

# Argparse will handle the commandline for us.
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="The input file. Normally a prose document.")
parser.add_argument("-o", "--output", help="The output file name, without file extension.")
cliArgs = parser.parse_args()

# Open the file the user asked us to.
openFile = open(cliArgs.input, 'r')
# Initiate the word list that we'll be building from the input file.
wordList = []

# Escape characters that might occur that we don't care about.
# Current Issue: Doesn't ignore the '#' symbol, because escaping it is a pain in the butt in Python.
characterIgnoreList = ['"','.',',',';',':','(',')','{','}','[',']','/','\\','!','-','_','+','=','*','&','^','%','$','@']

# A list of common English words to ignore.
ignoredWordsList = ["be","to","of","and","a","in","that","have","I","it","for","not","on","with","he","as","you","do","at","this","but","his","by","from","they","we","say","her","she","or","an","will","my","one","all","would","there","their","what","so","up","out","if","about","who","get","which","go","me","when","make","can","like","time","no","just","him","know","take","people","into","year","your","good","some","could","them","see","other","than","then","now","look","only","come","its","over","think","also","back","after","use","two","how","our","work","first","well","way","even","new","want","because","any","these","give","day","most","us"]

# Iterate through the file we opened earlier.
for line in openFile:
    # Let's split each word apart into a list.
    words=line.split()
    # Let's iterate through this new list.
    for word in words:
        # Use our ignore list to get rid of formatting characters.
        for char in characterIgnoreList:
            word = word.replace(char,"")
        word = unicode(word, 'ascii', 'ignore')
        wordList.append(word)

# Remove all duplicate words.
wordList = list(set(wordList))

# Remove all words using our ignore list as a basis.
finalWordList = list(set(wordList).difference(ignoredWordsList))

# Alphabetise the list naively.
finalWordList.sort()

# Print to the console, or an output file.
if cliArgs.output:
    outFile = open(cliArgs.output, 'w+')
    for word in finalWordList:
        outFile.write(word + "\n")
else:
    for word in finalWordList:
        print word
