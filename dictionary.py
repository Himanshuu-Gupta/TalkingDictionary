import os
import json
from difflib import get_close_matches 

# Arguments to decide the similarity index for a word
similarity_index=0.8
max_similar_matches=5


dict_object = json.load(open("dictionary.json")) 

#####################################################
# Function - get_meaning (word)
#            Get the meaning for the word
#####################################################
def get_meaning(word):
    word = word.lower()
    if word in dict_object:
        print("\n Word - ", word)
        print("Meaning - ",dict_object[word])
    elif len(get_close_matches(word, dict_object.keys(), n=max_similar_matches, cutoff=similarity_index))>0:
        get_similar_words(word)
    else:
        print("Couldn't Find word in dictionary.")

#####################################################
# Function - get_similar_words (word)
#            Get a list of similar words
#####################################################
def get_similar_words(word):
    similar_word_list = get_close_matches(word, dict_object.keys(), n=max_similar_matches, cutoff=similarity_index)
    print(f"Words similar to {word} are {similar_word_list}")
    for word in similar_word_list:
        get_meaning(word)


word = input ("Enter the word :") 
get_meaning(word)
    