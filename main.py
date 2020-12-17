import tweepy
import webbrowser
from config import consumer_key, consumer_secret, callback

auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback)

redirect_url = auth.get_authorization_url()

print(redirect_url)

webbrowser.open(redirect_url)

user_pin_input = input("Enter your pin ? ")

auth.get_access_token(user_pin_input)

print(auth.access_token, auth.access_token_secret)

api = tweepy.API(auth)

print(api.me())




# api.update_status('hello tweepy')

