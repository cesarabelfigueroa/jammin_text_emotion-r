#!/usr/bin/env python

import tweepy
from Classifier import Classifier

classifier = Classifier()
consumer_key = 'f16Yamwnbm1qu1uzw7Uyy9tor'
consumer_secret = 'gUjCPgvGzUCadA8wMw045cR4uSCZVJoOEgRpWKtTuYbTp1brvX'
access_token = '720053855203909632-CKpSoH74zkvPaVyp2etBmaw0mSIAsXw'
access_token_secret = 'mqC7xdBgNcJD44LY71GoQ5gPUvTdhZykmcuswBhUHSrr1'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
tweet = api.user_timeline('720053855203909632')[0]

print(classifier.evaluate(tweet.text))
