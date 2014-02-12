#!/usr/bin/env python
from itertools import islice
from random import randrange
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

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    # key = random.choice(chains.keys())
    #calling a function to find a capitalized key
    key = find_capitalized_key(chains)
    text = key[0] + " " + key[1]
    while key in chains.keys():
        random_index = randrange(0, len(chains[key]))
        text = text + " " + chains[key][random_index]
        key =  (key[1],chains[key][random_index])
    return text
  
def find_capitalized_key(chains):
    while True:
        key = random.choice(chains.keys()) 
        key_firstletter = key[0][0]
        # print "Key's first letter is ", key_firstletter
        # print "case of first letter is", key_firstletter.isupper()
        if key_firstletter.isupper():
            print "letter is uppercase"
            break    
    return key

def main():
    args = sys.argv
    script, filename = args


    # Change this to read input_text from a file
    f = open(filename)
    input_text = f.read()

    split_input_text =  input_text.split()
    #print split_input_text
    #print "----------------"

    chain_dict = make_chains(split_input_text)
    print chain_dict
    #print "------------"
    
    random_text = make_text(chain_dict)
    print "\n Random text is here: \n" , random_text

    key = find_capitalized_key(chain_dict)
    print "key is",  key
    


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
