from data import DICTIONARY, LETTER_SCORES

def load_words():
	"""Load dictionary into a list and return list"""
	with open(DICTIONARY) as f:
		words = f.read().split("\n")[:-1]
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
	return max(words, key = lambda x: calc_word_value(x))

if __name__ == "__main__":
    pass # run unittests to validate
