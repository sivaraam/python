string = "Hello world"
search_string = "lo"
search_word = "Hello"

print "Iterate over each 'character'"
for character in string:
    print character

print "\nCheck existence of 'substring'"
print search_string in string

print "\nCheck existence of 'word' (special case of substring)"
print search_word in string
