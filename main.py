import string
import re
import matplotlib.colors as mc
from collections import Counter



#with open("dickens.txt", "r", encoding="utf-8", errors='ignore') as a_file:
    #file_contents = a_file.read()
#1
num_lines = print('Number of lengths in the text file :',sum(1 for line in open("dickens.txt")))
#2
num_words = print('Number of words in the text file :',len(open("dickens.txt").read().split(' ')))
#3
#num_unique1 = print('Number of unique1 words in the text file :',len(set(open("text2.txt").read().split())))

#3
d = {}

with open('dickens.txt') as f:
    for line in f:
        for word in re.findall(r'[\w]+', line.lower()):
            #cword = re.sub('[-,;:" ".!()' '{-}/?]+', '', word)
            d[word] = d.setdefault(word, 0) + 1
            
count=0
for key in d.keys():
    #for key in list(d.keys()):
        if(d[key]==1):
          count += 1
print("The number of the unique words:", count)

#3
# text = open("dickens.txt", "r")
# mis = 0
# d = dict()
  
# # Loop through each line of the file
# for line in text:
#     line = line.strip()
#     line = line.lower()
#     line = line.translate(line.maketrans("", "", string.punctuation))
#     words = line.split(" ")
  
#     for word in words:
#         if word in d:
#             d[word] = d[word] + 1
#         else:
#             d[word] = 1
            
#     for key in list(d.keys()):
#      if(d[key]==1):
#         mis = mis + 1
# print("The amount of unique words in the file:",mis)
# #print(d)

#4
with open("dickens.txt", "r", encoding="utf-8", errors='ignore') as a_file:
    count_line = 0
    max_len_of_sentences = 0
    uniq_count2 = 0
    count_words = 0
    uniqnes = 0
    my_dict = {}
    sum_len_of_sentence = 0
    file_contents = a_file.read()
    #print('Total words:   ', len(file_contents.split()))

    
    
    total_count_of_sentences = file_contents.count('.')
    print('total sentences:    ', total_count_of_sentences)
    
    all_sentences = file_contents.split('.')
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
      
# #6
# max_count = 0
# temp_count_of_non_k_words = 0
# for word in words:
#     if "k" not in word:
#         temp_count_of_non_k_words +=1
#     else:
#         if temp_count_of_non_k_words > max_count:
#             max_count = temp_count_of_non_k_words
#             temp_count_of_non_k_words = 0
# if "k" not in words[-1]:
#     if temp_count_of_non_k_words > max_count:
#        temp_count_of_non_k_words > max_count 
#     else:
#        temp_count_of_non_k_words = 0
        
# print(max_count)
