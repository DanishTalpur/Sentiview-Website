import tweepy
import pandas as pd
import requests
import time


# Twitter API credentials
consumer_key = 'sIGUXm0uhlqYWYEID7VF1aiJ7'
consumer_secret = 'nQzQPBrTfg6WGpre9CpodKkYRrDVhs7vINvlqMu6dKGzwuJJSs'
access_token = '1256972021210243075-ZeCJJ6hPUgA3RQrmIcl6ei7m8UD12k'
access_token_secret = 'Y6AUJJdfn2g0BDI2clfEqlX7Uur3ndABqqeJkNhDdbO8R'








# Proxy setup (use if Twitter is blocked in your location)
proxy = {
    "http": "http://username:password@38.54.79.150:80",  # Replace with actual proxy
}

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Increase timeout for requests
api.session = requests.Session()
api.session.timeout = (5, 120)
api.session.proxies = proxy  # Add proxy configuration to session

# Fetch tweets function with retries
def fetch_tweets_with_retry(keywords, max_tweets_per_keyword, retries=3):
    tweets_data = []
    for keyword in keywords:
        print(f"Fetching tweets for keyword: {keyword}")
        for attempt in range(retries):
            try:
                for tweet in tweepy.Cursor(
                    api.search_tweets,
                    q=keyword,
                    geocode="30.3753,69.3451,2000km",  # Location for Pakistan
                    lang="en",
                    tweet_mode="extended"
                ).items(max_tweets_per_keyword):
                    if not tweet.retweeted and 'RT @' not in tweet.full_text:
                        tweets_data.append((tweet.id_str, tweet.full_text, keyword))
                break  # Exit retry loop if successful
            except requests.exceptions.ReadTimeout:
                print(f"Timeout occurred. Retrying... ({attempt + 1}/{retries})")
                time.sleep(5)  # Delay before retrying
            except tweepy.errors.TweepyException as e:
                print(f"An error occurred: {e}")
                break
    return tweets_data

# Fetch tweets
keywords = ['happy', 'sad', 'angry', 'depressed', 'excited']
max_tweets_per_keyword = 200  # Adjust as needed
tweets = fetch_tweets_with_retry(keywords, max_tweets_per_keyword)

# Create DataFrame
df = pd.DataFrame(tweets, columns=['Tweet ID', 'Tweet Text', 'Emotion'])
df = df.drop_duplicates(subset=['Tweet Text'])

# Save to CSV
df.to_csv('unique_tweets_emotions.csv', index=False)
print("Data collection completed.")





















# # Authenticate with Twitter
# auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth, wait_on_rate_limit=True)

# # Increase timeout for requests
# api.session = requests.Session()
# api.session.timeout = (5, 120)



# # Fetch tweets function
# def fetch_tweets_with_retry(keywords, max_tweets_per_keyword, retries=3):
#     tweets_data = []
#     for keyword in keywords:
#         print(f"Fetching tweets for keyword: {keyword}")
#         for attempt in range(retries):
#             try:
#                 for tweet in tweepy.Cursor(
#                     api.search_tweets,
#                     q=keyword,
#                     geocode="30.3753,69.3451,2000km",
#                     lang="en",
#                     tweet_mode="extended"
#                 ).items(max_tweets_per_keyword):
#                     if not tweet.retweeted and 'RT @' not in tweet.full_text:
#                         tweets_data.append((tweet.id_str, tweet.full_text, keyword))
#                 break  # Exit retry loop if successful
#             except requests.exceptions.ReadTimeout:
#                 print(f"Timeout occurred. Retrying... ({attempt + 1}/{retries})")
#                 time.sleep(5)  # Delay before retrying
#             except tweepy.errors.TweepyException as e:
#                 print(f"An error occurred: {e}")
#                 break
#     return tweets_data

# # Fetch tweets
# keywords = ['happy', 'sad', 'angry', 'depressed', 'excited']
# max_tweets_per_keyword = 200  # Adjust as needed
# tweets = fetch_tweets_with_retry(keywords, max_tweets_per_keyword)

# # Create DataFrame
# df = pd.DataFrame(tweets, columns=['Tweet ID', 'Tweet Text', 'Emotion'])
# df = df.drop_duplicates(subset=['Tweet Text'])

# # Save to CSV
# df.to_csv('unique_tweets_emotions.csv', index=False)
# print("Data collection completed.")



