from difflib import SequenceMatcher
import re
from collections import Counter
from itertools import combinations

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87


def get_tags():
	"""Find all tags in RSS_FEED.
	Replace dash with whitespace."""

	with open(RSS_FEED) as f:
		feed = f.read()
	
	tags = re.findall(r'<category>([^<]+)</category>', feed)
	return [tag.replace("-", " ").lower() for tag in tags]

def get_top_tags(tags):
	"""Get the TOP_NUMBER of most common tags"""
	return Counter(tags).most_common(TOP_NUMBER)

def get_similarities(tags):
	"""Find set of tags pairs with similarity ratio of > SIMILAR"""
	pairs = combinations(set(tags), 2)
	return [pair for pair in pairs if _is_similar(pair)]

def _is_similar(pair):
	return SequenceMatcher(a=pair[0], b=pair[1]).ratio() > SIMILAR 

if __name__ == "__main__":
	tags = get_tags()
	top_tags = get_top_tags(tags)
	print('* Top {} tags:'.format(TOP_NUMBER))
	for tag, count in top_tags:
		print('{:<20} {}'.format(tag, count))
	similar_tags = dict(get_similarities(tags))
	print()
	print('* Similar tags:')
	for singular, plural in similar_tags.items():
		print('{:<20} {}'.format(singular, plural))
