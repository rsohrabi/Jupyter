#define function to read and parse sentence
def count_vowels(sentence:str) -> dict:
    """ Return the number of vowels in the input sentence"""
    vowles = set('aeiou')
    count = {}
    for ch in list(sentence):
        if ch in vowles:
            count.setdefault(ch,0)
            count[ch] += 1
            
    return count
	
	
def find_common_characters(sentence:str, character:str) -> set:
    """ return set of common characters in two inputs"""
    return set(sentence).intersection(set(character))