import sys
from usertweets import UserTweets

def similar_tweeters(user1, user2):
	
def _gen_n_grams(tweets, n):
	pass

def _tokenize_tweets(tweets):
	pass

def _cosine_similarity(v1, v2):
	pass

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
        sys.exit(1)

    user1, user2 = sys.argv[1:3]
    similar_tweeters(user1, user2)
