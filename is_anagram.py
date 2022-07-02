from collections import Counter
 
def is_anagram(string1, string2):
    return Counter(string1) == Counter(string2)
 
 #You can use sort But I think using collection is better.
