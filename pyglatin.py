pyg = 'ay'

#Enter input from user
original = raw_input('Enter a word:')

#Change input to lower case
word = original.lower()

#save first letter in the string
first = word[0]

#create new word
new_word = word[1:] + first + pyg

if len(original) > 0 and original.isalpha():
    print original
    print new_word
else:
    print 'empty'