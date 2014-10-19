# tagmaps
from core import PartOfSpeech

# from http://en.wikipedia.org/wiki/Brown_Corpus#Part-of-speech_tags_used
brown = {
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
"IN":	PartOfSpeech.Preposition,
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
penn = {
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
