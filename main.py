import string
import re
import matplotlib.colors as mc
from collections import Counter

#1
num_lines = print('Number of lines in the text file :',sum(1 for line in open("dickens.txt")))
#2
num_words=0
with open("dickens.txt", 'r') as f: 
    for line in f: 
        words = line.split() 
        num_words += len(words) 
print("Number of words in the text file :", num_words) 

#3
d = {}

with open('dickens.txt') as f:
    for line in f:
        for word in re.findall(r'[\w]+', line.lower().strip()):
            d[word] = d.setdefault(word, 0) + 1
            
count=0
for key in d.keys():
    #for key in list(d.keys()):
        if(d[key]==1):
          count += 1
print("The number of the unique words:", count)


#4
with open("dickens.txt", "r", encoding="utf-8", errors='ignore') as a_file:
    count_line = 0
    max_len_of_sentences = 0
    uniq_count2 = 0
    count_words = 0
    uniqnes = 0
    my_dict = {}
    sum_len_of_sentence = 0
    myfile = a_file.read()
    #print('Total words:   ', len(myfile.split()))

    
    
    total_count_of_sentences = myfile.count('.')
    #print('total sentences:    ', total_count_of_sentences)
    
    all_sentences = myfile.split('.')
    # print ("all_sentences", all_sentences)
    for sentence in all_sentences:
        sum_len_of_sentence += len(sentence)
    avh_len_of_sentences = sum_len_of_sentence / total_count_of_sentences
    print('Total avg len:', avh_len_of_sentences)
    
    for sentence in all_sentences:
        if max_len_of_sentences < len(sentence):
            max_len_of_sentences = len(sentence)
    print('Max length of sentences is: ', max_len_of_sentences)

#5A
counter = Counter(open("dickens.txt").read().split())
array= counter.most_common()
print("The most common word in the text:", array[0][0])


#8
print("The colors in the text and their frequency:")
for key, val in d.items():
    if key in mc.cnames:
      print(key,':',val)
  

#6
with open("dickens.txt", "r", encoding="utf-8", errors='ignore') as a_file:
#with open("dickens.txt", 'r') as a_file:
     words = a_file.read().lower().split(" ")
 
max_count = 0
maxword = []
tempcountwords = []
temp_count_of_non_k_words = 0

for word in words:
    if "k" not in word:
        temp_count_of_non_k_words +=1
        tempcountwords.append(word)
    else:
        if temp_count_of_non_k_words > max_count:
            max_count = temp_count_of_non_k_words
            maxword = tempcountwords
            tempcountwords = []
            temp_count_of_non_k_words = 0
            

print("The longest word sequence without k:", ' '.join(maxword))     
#print("The length of the longest words sequence without k:", max_count)
