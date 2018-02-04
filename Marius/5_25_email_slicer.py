#5_25 email slicer

#donno what he said
word = "supadupamothafuka"

#print 1st letter of word
print(word[0])

#print any other letter from word
print(word[15])

#now a slice: variable name[start:end:step]
print(word[8:17:1])

#slice smtg else + examples
print(word[0:4:1])
#1
print(word[5:])
#2
print(word[3::2])
#3
print(word[:8])
#reverse the word
print(word[::-1])


#new vid
#count in reverse
#last letter in word
print(word[-1])
#-5 letter in word
print(word[-6])
#
print(word[word.index("dupa"):word.index("motha")])
print(word[word.index("moth"):word.index("fuka")])
#this should not work
print(word[word.index("dupa"):word.index("a")])
