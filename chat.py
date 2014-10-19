#!/usr/bin/env python3

import nltk
import re
import tagmaps
from core import *

#corp = nltk.corpus.treebank.tagged_sents()
def setup():
    global corp, tagger
    print("training hmm...")
    corp = nltk.corpus.brown.tagged_sents()
    tagger = nltk.HiddenMarkovModelTagger.train(corp)#[(tag,word) for (word,tag) in corp])
setup()
#dist = nltk.ConditionalFreqDist(corp)#[(tag,word) for (word,tag) in corp])
def tagSentence(sentence):
    def readPartOfSpeech(read):
        print("reading: "+str(read))
        if read in tagmaps.brown:
            return tagmaps.brown[read]
        else:
            print("could not read tag type: "+str(read))
            return PartOfSpeech.UNKNOWN
    def tagWord(w):
#        pos = ""
#        if not w in dist:
#            print("word not in dist: "+str(w))
#            pos = None
#        elif len(dist[w].most_common()) == 0:
#            print("word entries empty: " +str(w))
#            pos = None
#        else:
#            pos = dist[w].most_common()[0][0]
#            print("pos: "+str(pos))
#        return pos
        tag = tagger.tag([w])
        print("tagged as: "+str(tag))
        return tagger.tag(w)[0]
    words = nltk.word_tokenize(sentence)
    print("words: "+ str(words))
    tagged = tagger.tag(words)
    for i in range(0, len(tagged)):
        tagged[i] = (tagged[i][0], readPartOfSpeech(tagged[i][1]))
    return tagged

def take(l, pred):
    out = []
    for a in l:
        if(pred(a)):
            out.append(a)
    return out

def partsToString(parts):
    typeMap = {
        PartOfSpeech.Verb : 'v',
        PartOfSpeech.Noun : 'n',
        PartOfSpeech.Adjective : 'a',
        PartOfSpeech.Adverb : 'b',
        PartOfSpeech.Article : 'r',
        PartOfSpeech.Preposition : 'p',
    }
    out = ""
    for part in parts:
        if part in typeMap:
            out += typeMap[part]
        else:
            return "Could not convert type: "+str(part)
    return out
    
def parse(sentence):
    def selectAroundGroup(string, m, start, groupid):
        end = start + len(m.group(groupid))
        print("start:{0}.end{1}".format(start, end))
        return string[start:start+len(m.group(groupid))], end
    def parseANVPAN(words, parts, m):
        adj1,end = selectAroundGroup(words, m, 0, 1)
        subj = words[end]; end += 1
        verb = words[end]; end += 1
        prep,end = selectAroundGroup(words, m, end, 2)
        adj2,end = selectAroundGroup(words, m, end, 3)
        obj = words[end]
        if(len(prep) == 0):
            return Sentence(Noun(subj, adj1),
                            Verb(verb, Noun(obj, adj2)))
        else:
            return Sentence(Noun(subj, adj1),
                            Verb(verb, Preposition(prep,
                                                   Noun(obj, adj2))))
    tagged = tagSentence(sentence)
    tagged = take(tagged, lambda x: x[1] != PartOfSpeech.Article)
    words = [a for (a,b) in tagged]
    parts = tuple([b for (a,b) in tagged])
    flatParts = partsToString(parts)
    print("tagged: " + str(tagged))
    print("words: " + str(words))
    print("parts: " + str(parts))
    patterns = [
        ("nvn",
        (lambda words, parts, m: Sentence(Noun(words[0]), 
                                          Verb(words[1], Noun(words[2]))))),

        ("(a+)nv(p?)(a+)n", parseANVPAN),
         

        ("nv",
        (lambda words, parts, m: Sentence(Noun(words[0]), 
                                          Verb(words[1], [])))),

    ]
    for (pattern, fun) in patterns:
        print("checking pattern: " + str(pattern))
        m = re.match(pattern, flatParts)
        if m:
            return fun(words, parts, m)
    return 'Could not match pattern' + str(parts)

if __name__ == "__main__":
    data = []
    while True:    
        msg = input(">")
        data.append(parse(msg))
        print(str(data[-1]))
