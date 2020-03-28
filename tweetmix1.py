
import tweepy
import json

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
# Create API object
api = tweepy.API(auth)
print(api)
i=0
with open('sarcasm_user_embedding_tweets.ids', 'r') as f:
	data=f.readlines()
	f1=open("retweeter2.jsonstream","a")
	for d in data:
		print(d.split("\n")[0])
		va=d.split("\n")[0]
		try:
			status = api.retweeters(d.split("\n")[0])
			print(status)
			x={va:status}
			y=json.dumps(x)
			f1.writelines(y+'\n')
		except:
			print("Error for{}".format(va))
			
	f1.close()	

	