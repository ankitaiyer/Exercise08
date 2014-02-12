#!/usr/bin/env python
from itertools import islice
import sys
import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    chain_dict = {}
    for i in range(len(corpus) -2):
        key = (corpus[i], corpus[i+1])
        if not chain_dict.get(key):
            chain_dict[key] = [corpus[i+2]]
        else:
            chain_dict[key].append(corpus[i+2])
    return chain_dict


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    text = " "
    key = random.choice(chains.keys())
    for key in chains.keys():
        temp_text = key[0] + " " + key[1] + " " + chains[key][0] + " "
        key = (key[1],chains[key][0])
        text = text + "\n" + temp_text    
    return text
  

def main():
    args = sys.argv
    script, filename = args


    # Change this to read input_text from a file
    f = open(filename)
    input_text = f.read()

    split_input_text =  input_text.split()
    print "original file text is " , split_input_text

    chain_dict = make_chains(split_input_text)
    print "--- chain dict ---------"
    print chain_dict
    print "------After this -------"
    
    random_text = make_text(chain_dict)
    print random_text


    


if __name__ == "__main__":
    main()


















# get the text file on command line
# open a file
# read a file
# Close a file
# seperate the file into words
# Strip the punctuations from words
# create begrams using Marcov theory
# create dictionary to store bigram as Key and possible words as values
# for random bigram on the left in marov list,
# we will use a possible word in right  and create a text line using,
# the bigrams again ont he left
# print the line.
