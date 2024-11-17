import tweepy

def fetch_twitter_data():
    API_KEY = "your_api_key"
    API_SECRET_KEY = "your_api_secret_key"
    ACCESS_TOKEN = "your_access_token"
    ACCESS_SECRET = "your_access_secret" # todo: use .env file instead

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    tweets = api.search_tweets(q="2024 election", lang="en", count=100)
    data = [{"id": tweet.id, "text": tweet.text, "created_at": tweet.created_at} for tweet in tweets]
    
    print("Fetched Tweets:", data)
    # Save data for further processing

if __name__ == "__main__":
    fetch_twitter_data()