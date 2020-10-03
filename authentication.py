# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 08:01:47 2020

@author: abhir
"""
import twitter

Consumer_Key = 'uNwhlfwzcM23fgRAtaoXPvU4d'

Consumer_Secret = 'W8fDQ11WBuVr78Fa9J6mvBLzdJRDSz7Q7Y4YZ4D0OHyjzYsUyq'

OAuth_Token = '496808705-hYsursHxOSTbUR1qhYVWwx8LNaLa4X3vB9bsr0TC'

OAuth_Secret = 'UNfLDymCr9E3alXyuiPrGmXQQZCV6BOlC8Jw760toNvOZ'

auth = twitter.oauth.OAuth(OAuth_Token,OAuth_Secret,Consumer_Key,Consumer_Secret)

twitter_api=twitter.Twitter(auth=auth)

print(twitter_api)