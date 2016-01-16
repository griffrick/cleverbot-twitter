from chatterbotapi import ChatterBotFactory, ChatterBotType
import requests
import twitter
import time

def ask(message):
	s = bot1session.think(message)
	return s
def run_rampant(api):
	since=None
	while(True):
		results= api.GetSearch(term="trump",since_id=since)
		for tweet in results:
			twitter_text = unicode(tweet.text).encode("utf8")
			screen_name = tweet.user.screen_name
			print twitter_text
			
			reply= ask(twitter_text)
			print "reply: "+reply
			full_reply= "@"+screen_name+" "+reply
			if(len(full_reply)<=140):
				try:
					api.PostUpdate("@"+screen_name+" "+reply)
				except:
					print "error"
		since=tweet.id
		time.sleep(900)

factory = ChatterBotFactory()

bot1 = factory.create(ChatterBotType.CLEVERBOT)
bot1session = bot1.create_session()
api = twitter.Api(consumer_key='',
                      consumer_secret='',
                      access_token_key='',
                      access_token_secret='')
print api.VerifyCredentials()
run_rampant(api)


# def send(message):
