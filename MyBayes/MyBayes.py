#/usr/bin/env python
#coding:utf-8

import copy
def loadDataSet():
    postingList = [["my", "dog", "has", "flea", \
                   "problems", "help", "please"],
                   ["maybe", "not", "take", "him", \
                    "to", "dog", "park", "stupid"],
                   ["my", "dalmation", "is", "so", "cute", \
                    "I", "love", "him"],
                   ["stop", "posting", "stupid", "worthless", "garbage"],
                   ["mr", "licks", "ate", "my", "steak", "how", \
                    "to", "stop", "him"],
                   ["quit", "buying", "worthless", "dog", "food", "stupid"],
                   ]

    classVec = [0, 1, 0, 1, 0, 1]
    return postingList, classVec
p ,c = loadDataSet()

def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

pl = createVocabList(p)
sd = {}

for w in pl:
  sd.setdefault(w, 1)

pp = {"0": sd, "1": copy.deepcopy(sd)}

cb0 , cb1 = 0, 0
for a, b in zip(p, c):
  for pw in a:
    pp[str(b)][pw] += 1
    if b == 0:
      cb0 += 1
    else:
      cb1 += 1
print "++++++++++++++++"

ps0 = 0.5
ps1 = 0.5

ta = ["love", "my", "dalmation"]
tb = ["stupid", "garbage"]



# print sd
# print "pp is", pp
# print cb0, cb1

for k, v in pp["0"].items():
  pp["0"][k] = float(v) / (cb0+2)

for k, v in pp["1"].items():
  pp["1"][k] = float(v) / (cb1+2)

print pp

p0, p1 = 1, 1
for word in ta:
  p0 = p0 *pp["0"][word]

for word in ta:
  p1 = p1 *pp["1"][word]

print "the words ta in p0 is", p0 * ps0 
print "the words ta in p0 is", p1 * ps1