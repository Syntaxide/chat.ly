#!/usr/bin/env python3

import nltk
import re

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


# from http://en.wikipedia.org/wiki/Brown_Corpus#Part-of-speech_tags_used
brownTagMap = {
#"." : 	sentence closer (. ; ? *)
#"(" : 	left paren
#    ")":	right paren
#"*"	not, n't
#"--"	dash
#","	comma
#":"	colon
"ABL":	PartOfSpeech.Adjective, #pre-qualifier (quite, rather)
"ABN":	PartOfSpeech.Adjective, #pre-quantifier (half, all)
"ABX":	PartOfSpeech.Adjective, #pre-quantifier (both)
"AP":	PartOfSpeech.Adjective, #post-determiner (many, several, next)
"AT":	PartOfSpeech.Article, #(a, the, no)
"BE":	PartOfSpeech.Verb, #be
"BED":	PartOfSpeech.Verb,#were
"BEDZ":	PartOfSpeech.Verb,#was
"BEG":	PartOfSpeech.Verb,#being
"BEM":	PartOfSpeech.Verb,#am
"BEN":	PartOfSpeech.Verb,#been
"BER":	PartOfSpeech.Verb,#are, art
"BEZ":	PartOfSpeech.Verb,#is
"CC":	PartOfSpeech.Conjunction,#coordinating conjunction (and, #or)
"CD":	PartOfSpeech.Adjective,#cardinal numeral (one, two, 2, etc.)
#"CS"	PartOfSpeech.subordinating, conjunction (if, although)
"DO":	PartOfSpeech.Verb,#do
"DOD":	PartOfSpeech.Verb,#did
"DOZ":	PartOfSpeech.Verb,#does
#"DT"	PartOfSpeech.singular determiner/quantifier (this, that)
#"DTI"	PartOfSpeech.singular or plural determiner/quantifier (some, any)
#"DTS"	PartOfSpeech.plural determiner (these, those)
#"DTX"	PartOfSpeech.determiner/double conjunction (either)
#"EX"	PartOfSpeech.existential there
#"FW"	PartOfSpeech.foreign word (hyphenated before regular tag)
#"HV"	PartOfSpeech.have
#"HVD"	PartOfSpeech.had (past tense)
#"HVG"	PartOfSpeech.having
#"HVN"	PartOfSpeech.had (past participle)
#"IN"	PartOfSpeech.preposition
"JJ":	PartOfSpeech.Adjective,
"JJR":	PartOfSpeech.Adjective,
#"JJS"	PartOfSpeech.semantically superlative adjective (chief, top)
#"JJT"	PartOfSpeech.morphologically superlative adjective (biggest)
#"MD"	PartOfSpeech.modal auxiliary (can, should, will)
"NC":	PartOfSpeech.Noun,#cited word (hyphenated after regular #tag)
"NN":	PartOfSpeech.Noun,#singular or mass #noun
"NN$":	PartOfSpeech.Noun,#possessive singular #noun
"NNS":	PartOfSpeech.Noun,#plural #noun
"NNS$":	PartOfSpeech.Noun,#possessive plural noun
"NP":	PartOfSpeech.Noun,#proper noun or part of name phrase
"NP$":	PartOfSpeech.Noun,#possessive proper noun
"NPS":	PartOfSpeech.Noun,#plural proper noun
"NPS$":	PartOfSpeech.Noun,#possessive plural proper noun
"NR":	PartOfSpeech.Noun,#adverbial noun (home, today, west)
#"OD"	PartOfSpeech.ordinal numeral (first, 2nd)
#"PN"	PartOfSpeech.nominal pronoun (everybody, nothing)
#"PN$"	PartOfSpeech.possessive nominal pronoun
#"PP$"	PartOfSpeech.possessive personal pronoun (my, our)
#"PP$$"	PartOfSpeech.second (nominal) possessive pronoun (mine, ours)
#"PPL"	PartOfSpeech.singular reflexive/intensive personal pronoun (myself)
#"PPLS"	PartOfSpeech.plural reflexive/intensive personal pronoun (ourselves)
#"PPO"	PartOfSpeech.objective personal pronoun (me, him, it, them)
#"PPS"	PartOfSpeech.3rd. singular nominative pronoun (he, she, it, one)
#"PPSS"	PartOfSpeech.other nominative personal pronoun (I, we, they, you)
#"PRP"	PartOfSpeech.Personal pronoun
#"PRP$"	PartOfSpeech.Possessive pronoun
#"QL"	PartOfSpeech.qualifier (very, fairly)
#"QLP"	PartOfSpeech.post-qualifier (enough, indeed)
"RB":	PartOfSpeech.Adverb,
"RBR":	PartOfSpeech.Adverb,
"RBT":	PartOfSpeech.Adverb,
"RN":	PartOfSpeech.Adverb, #(here, then, indoors)
"RP":	PartOfSpeech.Adverb,#/particle (about, off, up)
#"TO"	PartOfSpeech.infinitive marker to
#"UH"	PartOfSpeech.interjection, exclamation
"VB":	PartOfSpeech.Verb,#, base form
"VBD":	PartOfSpeech.Verb,#, past tense
"VBG":	PartOfSpeech.Verb,#, present participle/gerund
"VBN":	PartOfSpeech.Verb,#, past participle
"VBP":	PartOfSpeech.Verb,#, non 3rd person, singular, present
"VBZ":	PartOfSpeech.Verb,#, 3rd. singular present
#"WDT"	PartOfSpeech.wh- determiner (what, which)
#"WP$"	PartOfSpeech.possessive wh- pronoun (whose)
#"WPO"	PartOfSpeech.objective wh- pronoun (whom, which, that)
#"WPS"	PartOfSpeech.nominative wh- pronoun (who, which, that)
#"WQL"	PartOfSpeech.wh- qualifier (how)
#"WRB"	PartOfSpeech.wh- adverb (how, where, when)
}

# from https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
pennTagMap = {
"CC" : 	PartOfSpeech.Conjunction,
"CD" : 	PartOfSpeech.UNKNOWN,
"DT" : 	PartOfSpeech.Article,
#"EX" : 	PartOfSpeech.Existential there,
#"FW" : 	PartOfSpeech.Foreign word,
"IN" : 	PartOfSpeech.Article, #preposition
"JJ" : 	PartOfSpeech.Adjective,
"JJR" : 	PartOfSpeech.Adjective,
"JJS" : 	PartOfSpeech.Adjective,
#"LS" : 	PartOfSpeech.List item marker,
#"MD" : 	PartOfSpeech.Modal,
"NN" : 	PartOfSpeech.Noun,
"NNS" : 	PartOfSpeech.Noun,
"NNP" : 	PartOfSpeech.Noun,
"NNPS" : 	PartOfSpeech.Noun,
#"PDT" : 	PartOfSpeech.Predeterminer,the 
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
        if read in brownTagMap:
            return brownTagMap[read]
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

def listEquals(parts, pattern):
    if(len(parts) != len(pattern)):
        return False
    for i in range(0, len(parts)):
        if parts[i] != pattern[i]:
            return False
    return True

def partsToString(parts):
    typeMap = {
        PartOfSpeech.Verb : 'v',
        PartOfSpeech.Noun : 'n',
        PartOfSpeech.Adjective : 'a',
        PartOfSpeech.Adverb : 'b',
        PartOfSpeech.Article : 'r',
    }
    out = ""
    for part in parts:
        if part in typeMap:
            out += typeMap[part]
        else:
            return "Could not convert type: "+str(part)
    return out
    
def parse(sentence):
    def parseANVN(words, parts, m):
        adjectives = words[0:len(m.group(1))]
        subj = words[len(m.group(1))]
        verb = words[len(m.group(1))+1]
        obj = words[len(m.group(1))+2]
        return Sentence(Noun(subj, adjectives),
                        Verb(verb, Noun(obj)))

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

        ("(a+)nvn", parseANVN),
         

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
