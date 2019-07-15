import os
import re

os.getcwd()
filepath1 = os.path.join('raw_data', 'paragraph_1.txt')
file1 = open(filepath1, 'r')
fileread1 = file1.read()

print('Paragraph Analysis\n' '-----------------\n' 'Paragraph 1\n' '-----------------')
print(fileread1)
print('-----------------')
#word count loop
wordcount = []
for word in fileread1.split():
    wordcount.append(word)
print(f'Approximate Word Count: {len(wordcount)}')

#sentence count
sent_count = re.split("(?<=[.!?]) +", fileread1)
print(f'Approximate Sentence Count: {len(sent_count)}')

#average letters per word
spaces = 0
specials = 0
letters = 0
for i in fileread1:
    if i == " ":
        spaces +=1
    elif i == "(" or i == "?" or i == "<" or i == "=" or i == "." or i == "!" or i == "-" or i == ")" or i == ">":
        specials += 1
    else:
        letters += 1
avgLetter = letters/len(wordcount)
print(f'Average Letter Count: {round(avgLetter,2)}')

#average words in sentences
avgsent = len(wordcount)/len(sent_count)
print(f'Average Sentence Length: {round(avgsent,2)}\n' '-----------------')

file1.close()

print('Paragraph 2\n' '-----------------')
filepath2 = os.path.join('raw_data', 'paragraph_2.txt')
file2 = open(filepath2, 'r')
fileread2 = file2.read()
print(fileread2)
print('-----------------')

#word count loop
wordcount = []
for word in fileread2.split():
    wordcount.append(word)
print(f'Approximate Word Count: {len(wordcount)}')

#sentence count
sent_count = re.split('\n', fileread2)
sent_count = [x for x in sent_count if x != '']
print(f'Approximate Sentence Count: {len(sent_count)}')

#average letters per word
spaces = 0
specials = 0
letters = 0
for i in fileread2:
    if i == " ":
        spaces +=1
    elif i == "(" or i == "?" or i == "<" or i == "=" or i == "." or i == "!" or i == "-" or i == ")" or i == ">":
        specials += 1
    else:
        letters += 1
avgLetter = letters/len(wordcount)
print(f'Average Letter Count: {round(avgLetter,2)}')

#average words in sentences
avgsent = len(wordcount)/len(sent_count)
print(f'Average Sentence Length: {round(avgsent,2)}\n' '-----------------')

file2.close()