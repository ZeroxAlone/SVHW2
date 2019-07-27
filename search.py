# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 07:59:02 2019

@author: translucky
"""

b_words=open('alice_in_wonderland.txt',mode='r')
vocab_list=open('vocab.txt',mode='r')
'''
def search_linear(xs, target):
    for (i, v) in enumerate(xs):
       if v == target:
           return i
    return -1

def find_unknown_words(vocab, wds):
    result = []
    for w in wds:
        if (search_linear(vocab, w) < 0):
            result.append(w)
    return result

missing_words = find_unknown_words(vocab_list, book_words)
print("There are {0} unknown words.".format(len(missing_words)))

o=[]
for i in book_words:
    o.append(i)
    print(o)
'''
book_words=str(b_words.copy())
words=[]
words=book_words.split()

def search_linear(vcb, target):
    for (i, v) in enumerate(vcb):
       if v == target:
           return i
    return -1

def find_unknown_words(vcb, wds):
    result = []
    for w in wds:
        if search_linear(vcb, w) < 0:
            result.append(w)
    return result

missing_words = find_unknown_words(vocab_list, words)
print("There are {0} unknown words.".format(len(missing_words)))
