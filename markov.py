#!/usr/bin/env python
from random import randrange
import sys
import random
import os
import twitter

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    markov_dict = {}
    for i in range(len(corpus) -2):
        key = (corpus[i], corpus[i+1])
        if not markov_dict.get(key):
            markov_dict[key] = [corpus[i+2]]
        else:
            markov_dict[key].append(corpus[i+2])
    return markov_dict

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    # key = random.choice(chains.keys())
    #calling a function to find a capitalized key
    key = isCapital(chains)
    text = key[0] + " " + key[1]
    while key in chains.keys():
        random_index = randrange(0, len(chains[key]))
        text = text + " " + chains[key][random_index]
        key =  (key[1],chains[key][random_index])
    return text
  
def isCapital(chains):
    #check_ascii_code = ord(key[0]) > ord('A') and ord(key[0]) < ord('Z')
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
    #status = api.PostUpdate('I love python-twitter!')
    #status = api.PostUpdate('Testing Python-Twitter API. Pls ignore my tweets.')
    #print status.text
    print some_text
    status = api.PostUpdate(some_text)
    print status.text
    
def insert_newlines(string, every=65):
    #new_text =  '\n'.join(string[i:i+every] for i in range(0, len(string), every))
    # for i in range(0, len(string), every):
    #     new_text ='\n'.join(string[i:i+every]) 
    lines = []
    lines1 = []
    for i in range(0, len(string), every):
        lines.append(string[i:i+every])
        lines1 =  '\n'.join(lines)
    
    return lines1  

def main():
    args = sys.argv
    script, filename, filename2 = args


    # Read input_text from a file
    f = open(filename)
    input_text = f.read()
    f.close()

    f1 = open(filename2)
    new_input_text = f1.read()
    f1.close()

    #Separate file into words by space
    split_input_text = input_text.split() + new_input_text.split()
    

    #Create a dict with bigrams(keys) & following word(value)
    chain_dict = make_chains(split_input_text)
   
    
    # Make text using markov's dict
    random_text = make_text(chain_dict)
    if len(random_text) > 65:
        random_text_list = insert_newlines(random_text)
  
    
    # TODO - If text has punc characters then print it on next line
    for i in range(len(random_text)):
        if random_text[i]
    

    print "\n Random text is here: \n" , random_text_list
    #set the twitter api and tweet the generated message
    # tweet_text(random_text)

    


if __name__ == "__main__":
    main()

