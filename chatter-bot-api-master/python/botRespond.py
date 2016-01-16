from chatterbotapi import ChatterBotFactory, ChatterBotType
import requests
import twitter
def ask(message):
	s = bot1session.think(message)
	return s
def run_rampant(api):
	
	results= api.GetSearch(term="trump")
	for tweet in results:
		twitter_text = unicode(tweet.text).encode("utf8")
		screen_name = tweet.user.screen_name
		print twitter_text
		reply= ask(twitter_text)
		print "reply: "+reply
		full_reply= "@"+screen_name+" "+reply
		if(len(full_reply)<=140):
			api.PostUpdate("@"+screen_name+" "+reply)

factory = ChatterBotFactory()

bot1 = factory.create(ChatterBotType.CLEVERBOT)
bot1session = bot1.create_session()
api = twitter.Api(consumer_key='',
                      consumer_secret='',
                      access_token_key='',
                      access_token_secret='')
print api.VerifyCredentials()

while(True):
	run_rampant(api)
	sleep(30)

# def send(message):
