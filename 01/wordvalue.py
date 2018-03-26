from data import DICTIONARY, LETTER_SCORES

def load_words():
	"""Load dictionary into a list and return list"""
	words = open(DICTIONARY).read().split("\n")[:-1]
	return [word.replace("-", "") for word in words]

def calc_word_value(word):
	"""Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
	
	for w in word:
		if w not in "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz":				
			raise ValueError("Can only accept letters, not %s"%(w))
	
	return sum([LETTER_SCORES[w.upper()] for w in word])

def max_word_value(words=load_words()):
	"""Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

	if len(words) == 0:
		raise ValueError("cannot find max value of empty list")
	max_word = None
	max_score = -1

	for word in words:
		word_score = calc_word_value(word)
		if (word_score > max_score):
			max_word = word
			max_score = word_score

	return max_word

if __name__ == "__main__":
    pass # run unittests to validate
