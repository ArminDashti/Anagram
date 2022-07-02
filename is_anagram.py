from collections import Counter
 
def is_anagram(string1, string2):
    return Counter(string1) == Counter(string2)