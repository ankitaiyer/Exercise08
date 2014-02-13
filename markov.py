#!/usr/bin/env python
from random import randrange
import sys
import random
import os
import twitter

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    marcov_dict = {}
    for i in range(len(corpus) -2):
        key = (corpus[i], corpus[i+1])
        if not marcov_dict.get(key):
            marcov_dict[key] = [corpus[i+2]]
        else:
            marcov_dict[key].append(corpus[i+2])
    return marcov_dict

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
            break    
    return key


def tweet_text(some_text):
    twitter_key = os.environ.get("TWITTER_API_KEY")
    twitter_secret_key = os.environ.get("TWITTER_SECRET_KEY")
    access_token = os.environ.get("ACCESS_TOKEN_KEY")
    access_token_secret = os.environ.get("ACCES_TOKEN_SECRET")

    api = twitter.Api(consumer_key=twitter_key,
                      consumer_secret=twitter_secret_key,
                      access_token_key=access_token,
                      access_token_secret=access_token_secret)

    #print api.VerifyCredentials()
    status = api.PostUpdate('I love python-twitter!')
    print status.text
    # api.PostUpdate(twitter_key , some_text)
    
 

def main():
    args = sys.argv
    script, filename = args


    # Read input_text from a file
    f = open(filename)
    input_text = f.read()
    f.close()

    #Separate file into words by space
    split_input_text =  input_text.split()
    #print split_input_text
    #print "----------------"

    #Create a dict with bigrams(keys) & following word(value)
    chain_dict = make_chains(split_input_text)
    print chain_dict
    #print "------------"
    
    # Make text using marcov's dict
    random_text = make_text(chain_dict)
    print "\n Random text is here: \n" , random_text
    
    #set the twitter api key
    
    tweet_text(random_text)
    

    






    # #Find a capitalzed word in random text
    # word_list = random_text.split()
    # print type(word_list)
    # print word_list

    # x = 0
    # for word in word_list:
    #     if not word[0].isupper():
    #         print x
    #         word_list.insert(x,"abc")
    #         print word
    #     x += 1
    # print word_list



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
