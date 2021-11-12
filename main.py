import string
import re
import matplotlib.colors as mc


#with open("dickens.txt", "r", encoding="utf-8", errors='ignore') as a_file:
    #file_contents = a_file.read()
#num_lines = print(sum(1 for line in open('text.txt')))
#1
num_lines = print('Number of lengths in the text file :',sum(1 for word in open("dickens.txt")))
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
print(count)

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

#5A
from collections import Counter
counter = Counter(open("dickens.txt").read().split())
array= counter.most_common()
print(array[0][0])

  

#8
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
