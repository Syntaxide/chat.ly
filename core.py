from enum import Enum

class PartOfSpeech(Enum):
    Verb = 1
    Noun = 2
    Adjective = 3
    Adverb = 4
    Conjunction = 5
#   Exclamation = 6
    Article = 7
    Preposition = 8
    UNKNOWN = 9

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
class Preposition():
    def __init__(self, value, obj):
        """
        value is a string
        obj is a noun
        """
        self.value = value
        self.obj = obj
    def __str__(self):
        return "({0} -> {1})".format(self.value, str(self.obj)) 
