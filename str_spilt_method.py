words = "Hello world".split()
search_word = "Hello"
search_string = "lo"

print "Iterate over each 'word'"
for word in words:
    print word


print "\nCheck existence of 'word'"
print search_word in words


print "\nCheck inexistence of 'substring'"
print search_string not in words
