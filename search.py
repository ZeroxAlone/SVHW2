# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 16:43:37 2019

@author: lisa_
"""

def openfile(filename):
    f = open(filename,'r')
    fc = f.read()
    f.close()
    wds = fc.split()
    return wds

def translatetext(text):
    subs = text.maketrans(
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      "abcdefghijklmnopqrstuvwxyz                                          ")
    t = text.translate(subs)
    wds = t.split()
    return wds

def getwords(filename):
    f = open(filename,'r')
    fc = f.read()
    f.close()
    wds = translatetext(fc)
    return wds

def removerep(a):
    l = []
    lastw = None
    for i in a:
        if i != lastw:
            l.append(i)
            lastw=i
    return l

def binary(a, target):
    l = 0
    u = len(a)
    while True:
        if l == u:
           return -1
        mid = (l + u) // 2
        m = a[mid]
        if m == target:
            return mid
        if m < target:
            l = mid + 1
        else:
            u = mid

def unknownwords(vocab, wds):
    inlist = []
    for w in wds:
        if (binary(vocab, w) < 0):
            inlist.append(w)
    return inlist

allwords = getwords('alice_in_wonderland.txt')
vocabl = openfile('vocab.txt')
allwords.sort()
unknows = removerep(unknownwords(vocabl,allwords))
print("There are {0} unknown words.".format(len(unknows)))
