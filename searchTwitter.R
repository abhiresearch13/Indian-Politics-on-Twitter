install.packages("twitteR")
library("twitteR")

setup_twitter_oauth(consumer_key = ConsumerKey, consumer_secret = ConsumerSecret,access_token = OAuthToken,access_secret = OAuthSecret)


twitter_nathuram_1 = twListToDF(searchTwitter("#नाथूराम_गोडसे_जिंदाबाद",since = "2020-10-01",n=100000))


twitter_sudarshan = twListToDF(searchTwitter("##सुदर्शन_की_हार_हिंदुओ_की_हार",since = "2020-10-01",n=30000))

userOpindia=getUser("OpIndia_com")
location(userOpindia)
opindia_followers=userOpindia$getFollowerIDs(retryOnRateLimit=180)

test_df=as.data.frame(opindia_followers)
