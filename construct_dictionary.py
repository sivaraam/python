# -*- coding: utf-8 -*-
"""
Stores the words in the file as keys in
a dictionary with arbitrary value
"""
def get_dictionary(file):
    words = {}
    initial_value = 1
    line  = file.read()
    while line:
        for word in line.split():
            words[word] = words.get(word, initial_value) + 1
        line  = file.read()

    return words

file = open('/usr/share/dict/words')
words = get_dictionary(file)
# print words # pretty time consuming (makes IDLE hang)

test_words = ["A's", "AI's", "zoos", "étude's"]
for test_word in test_words:
    print "Testing: ", test_word
    assert test_word in words
