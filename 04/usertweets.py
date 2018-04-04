from collections import namedtuple
import csv
import os

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100


class UserTweets(object):
	"""TODOs:
	- create a tweepy api interface
	- get all tweets for passed in handle
	- optionally get up until 'max_id' tweet id
	- save tweets to csv file in data/ subdirectory
	- implement len() an getitem() magic (dunder) methods"""

	def __init__(self, handle, max_id=None):
		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
		api = tweepy.API(auth)

		TWEET_COUNT = NUM_TWEETS

		self.recent_tweets = api.user_timeline(handle, count=TWEET_COUNT)
		
		self.output_file = "data/some_handle.csv"	
		
		with open(self.output_file, 'w') as csvfile:
			writer = csv.writer(csvfile)
			for tw in self.recent_tweets:
				writer.writerow([tw.id_str, tw.created_at, tw.text])
			
	def __len__(self):
		return len(self.recent_tweets)

	def __getitem__(self, pos):
		return self.recent_tweets[pos]	

if __name__ == "__main__":

	for handle in ('pybites', 'techmoneykids', 'bbelderbos'):
	    print('--- {} ---'.format(handle))
	    user = UserTweets(handle)
	    for tw in user[:5]:
	        print(tw)
	    print()
