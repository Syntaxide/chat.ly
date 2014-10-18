#!/usr/bin/env python3

import nltk

from enum import Enum

class PartOfSpeech(Enum):
    Verb = 1
    Noun = 2
    Adjective = 3
    Adverb = 4
    Conjunction = 5
#    Exclamation = 6
    Article = 7
    UNKNOWN = 8

# from https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
tagMap = {
"CC" : 	PartOfSpeech.Conjunction,
"CD" : 	PartOfSpeech.UNKNOWN,
"DT" : 	PartOfSpeech.Article,
#"EX" : 	PartOfSpeech.Existential there,
#"FW" : 	PartOfSpeech.Foreign word,
#"IN" : 	PartOfSpeech.Preposition or subordinating conjunction,
"JJ" : 	PartOfSpeech.Adjective,
"JJR" : 	PartOfSpeech.Adjective,
"JJS" : 	PartOfSpeech.Adjective,
#"LS" : 	PartOfSpeech.List item marker,
#"MD" : 	PartOfSpeech.Modal,
"NN" : 	PartOfSpeech.Noun,
"NNS" : 	PartOfSpeech.Noun,
"NNP" : 	PartOfSpeech.Noun,
"NNPS" : 	PartOfSpeech.Noun,
#"PDT" : 	PartOfSpeech.Predeterminer,
#"POS" : 	PartOfSpeech.Possessive ending,
"PRP" : 	PartOfSpeech.Noun,
"PRP$" :	PartOfSpeech.Noun,
    "RB" : 	PartOfSpeech.Adverb,
"RBR" : 	PartOfSpeech.Adverb,
"RBS" : 	PartOfSpeech.Adverb,
#"RP" : 	PartOfSpeech.Particle,
#"SYM" : 	PartOfSpeech.Symbol,
#"TO" : 	PartOfSpeech.to,
#"UH" : 	PartOfSpeech.Interjection,
"VB" : 	PartOfSpeech.Verb,
"VBD" : 	PartOfSpeech.Verb,
"VBG" : 	PartOfSpeech.Verb,
"VBN" : 	PartOfSpeech.Verb,
"VBP" : 	PartOfSpeech.Verb,
"VBZ" : 	PartOfSpeech.Verb,
#"WDT" : 	PartOfSpeech.Wh-determiner,
#"WP" : 	PartOfSpeech.Wh-pronoun,
#"WP$" :	PartOfSpeech.Possessive wh-pronoun,
#"WRB" : 	PartOfSpeech.Wh-adverb,
}

class Sentence():
    def __init__(self, subject, predicate):
        """
        subject is a noun, predicate is a Verb expr
        """
        self.subject = subject
        self.predicate = predicate
    def __str__(self):
        return "({0} , {1})".format(str(self.subject), str(self.predicate))
        
class Noun():
    def __init__(self, value, adjectives=[]):
        """
        value is a string
        adjectives is an array of strings
        """
        self.value = value
        self.adjectives = adjectives
    def __str__(self):
        return "({0} : {1})".format(self.value, self.adjectives)

class Verb():
    def __init__(self, value, obj=None):
        """
        value is a string
        object is a noun or None
        """
        self.value = value
        self.obj = obj
    def __str__(self):
        return "({0} -> {1})".format(self.value, str(self.obj)) 

def tagSentence(sentence):
    def readPartOfSpeech(read):
        if read in tagMap:
            return tagMap[read]
        else:
            return PartOfSpeech.UNKNOWN
    words = nltk.word_tokenize(sentence)
    tagged = [(w,readPartOfSpeech(p)) for (w,p) in nltk.pos_tag(words)]
    return tagged


def take(l, pred):
    out = []
    for a in l:
        if(pred(a)):
            out.append(a)
    return out

def listEquals(parts, pattern):
    if(len(parts) != len(pattern)):
        return False
    for i in range(0, len(parts)):
        if parts[i] != pattern[i]:
            return False
    return True

def parse(sentence):
    tagged = tagSentence(sentence)
    tagged = take(tagged, lambda x: x[1] != PartOfSpeech.Article)
    words = [a for (a,b) in tagged]
    parts = tuple([b for (a,b) in tagged])

    print("tagged: " + str(tagged))
    print("words: " + str(words))
    print("parts: " + str(parts))
    patterns = {
        (PartOfSpeech.Noun, PartOfSpeech.Verb, PartOfSpeech.Noun) : 
        (lambda words: Sentence(Noun(words[0]), 
                                Verb(words[1], Noun(words[2])))),

        (PartOfSpeech.Noun, PartOfSpeech.Verb) : 
        (lambda words: Sentence(Noun(words[0]), 
                                Verb(words[1], [])))
    }
    for pattern in patterns:
        print("checking pattern: " + str(pattern))
        if parts == pattern:
            return patterns[pattern](words)
    return 'Could not match pattern' + str(parts)

while True:    
    msg = input(">")
    print(str(parse(msg)))

    
