# -*- coding: utf-8 -*-

"""
Stores the words in the file as keys in
a dictionary with value as the numer of
occurence of the words.
"""
def get_dictionary(file):
    words = {}
    words.setdefault(str, 0)
    line  = file.read()
    while line:
        for word in line.split():
            # words[word] = words.get(word, 0) + 1
            words[word] += 1
        line  = file.read()

    return words

##
##"""
##Given a dictionary 'd' and value 'v', return the
##first key 'k' that corresponds to 'v'.
##
##If there's no such key raise ValueError
##"""
##def reverse_lookup(d, v):
##    for k in d:
##        if d[k] == v:
##            return k
##
##    raise ValueError, 'value does not appear in the dictionary'


"""
Given a dictionary 'd' and value 'v', return the
first key 'k' that corresponds to 'v'.

If there's no such key return None
"""
def reverse_lookup_quiet(d, v):
    for k in d:
        if d[k] == v:
            return k

    return None


"""
Given a dictionary 'd' which has structure as that given by
get_dictionary(), check if it is a valid lexicographic
dictionary i.e., every key has value only of exactly 1. Return
'True if it's the case else return False.
"""
def valid_lexicographic_dictionary(d):
    for k in d:
        if d[k] > 1:
            return False
    return True

##
##"""
##Given a dictionary 'd' which has structure as that given by
##get_dictionary(), print those keys which have value(occurence)
##greater than 1 thus being invalid.
##"""
##def print_invalid(d):
##    for k in d:
##        if d[k] > 1:
##            print k, d[k]
##



""" Given a dictionary 'd' which has structure as that given by
get_dictionary(), check if there exists at least on key with
value 1
"""
def valid_language(d):
    if reverse_lookup_quiet(d, 1) != None:
        return True
    else:
        return False

    
file = open('/usr/share/dict/words')
words = get_dictionary(file)

# print words # pretty time consuming (makes IDLE hang)

# Test if the dictionary has been constructed with all
# words by testing out the existence of a few of them
# chosen at random from the file
test_words = ["A's", "AI's", "zoos", "étude's"]
for test_word in test_words:
    if test_word in words:
        status = "Success"
    else:
        status = "FAIL!"

    print "Test: ", test_word, "\t", "Status: ", status

# print_invalid(words)

# Ensure all words have an occurence of 1
assert valid_lexicographic_dictionary(words)

# Considering 'l' to be language which has 'words' as it's
# dictionary, it is valid if there exists at least one word
# with occurence of 1 (considering word s with occurence greater
# than 1 to mean that they are ambiguous)
assert valid_language(words)
