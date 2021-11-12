import string
import re

#msg="Hello world"
#print(msg)

#with open("dickens.txt", "r", encoding="utf-8", errors='ignore') as a_file:
    #file_contents = a_file.read()
#num_lines = print(sum(1 for line in open('text.txt')))
#1
num_lines = print('Number of lengths in the text file :',sum(1 for word in open("dickens.txt")))
#2
num_words = print('Number of words in the text file :',len(open("dickens.txt").read().split(' ')))
#3
#num_unique1 = print('Number of unique1 words in the text file :',len(set(open("text2.txt").read().split())))

#5A
from collections import Counter
counter = Counter(open("dickens.txt").read().split())
array= counter.most_common()
print(array[0][0])

"""
sum_len_of_sentence = 0


total_count_of_sentences = open("dickens.txt").count('.')
print('total sentences:    ', total_count_of_sentences)
all_sentences = open("dickens.txt").split('.')
print ("all_sentences", all_sentences)
for sentence in all_sentences:
   sum_len_of_sentence += len(sentence)
avh_len_of_sentences = sum_len_of_sentence / total_count_of_sentences
print('Total avg len:', avh_len_of_sentences)

for sentence in all_sentences:
  if max_len_of_sentences < len(sentence):
     max_len_of_sentences = len(sentence)
print('Max length of sentences is: ', max_len_of_sentences)

"""
my_dict={}

for line in (open("dickens.txt")):
#def find_uniq_words(line):
    words = line.split()
    line = line.lower().strip().split(" ")
    for word in words:
        cword = re.sub('[-,;:" ".!()' '{-}/?]+', '', word)
        if cword in my_dict:
            my_dict[cword] = my_dict[cword]+ 1
        else:
            my_dict[cword] = 1
print (my_dict)
"""         
uniq_count2 = 2  
for d in list(my_dict.keys()):
         if my_dict.get(d) == 1:
               uniq_count2 += 1

print("find_uniq_words: ", uniq_count2)
"""