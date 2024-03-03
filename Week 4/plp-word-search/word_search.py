import json
import difflib

def get_word_definition(word):
    with open('data.json', 'r') as file:
        data = json.load(file)
        

    for phrase, definitions in data.items():
        if phrase.lower() == word.lower():
            print(f"word: {phrase}")
            for definition in definitions:
                print(f"Definition: {definition}")
            return
        
    print("Word not found")
    suggest_closest_word(word)

def suggest_closest_word(misspelled_word):
    with open('data.json', 'r') as file:
        data = json.load(file)
    
    words = list(data.keys())
    closest_match = difflib.get_close_matches(misspelled_word,words, n=3, cutoff=0.6)

    if closest_match:
        print("Did you mean: ")
        for match in closest_match:
            print(f"    {match} ?")
            return
    else:
        print("No suggrstions found")
            

word = input("Enter the word: ")
get_word_definition(word)