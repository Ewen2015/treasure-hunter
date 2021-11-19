import pandas as pd
import tweepy
import time
import datetime

def get_friends_df(api, screen_name):

    df = pd.DataFrame()
    friend_name = []
    description = []
    followers_count = []
    url = []
    location = []
    i, j = 1, 1

    for user in tweepy.Cursor(api.get_friends, screen_name=screen_name).items():

        print('{}: {}'.format(i, user.screen_name))
        friend_name.append(user.screen_name)
        description.append(user.description)
        followers_count.append(user.followers_count)
        url.append(user.url)
        location.append(user.location)
        if i % 300 == 0:
            
            df['friend_name'] = friend_name
            df['description'] = description
            df['followers_count'] = followers_count
            df['url'] = url
            df['location'] = location
            
            df.sort_values(by='followers_count', ascending=False, inplace=True)
            df.to_csv('friend_list_{}_{}_{}.csv'.format(screen_name,
                                                        datetime.datetime.now().strftime('%Y-%m-%d'),
                                                        j), index=False)
            j += 1
            print('sleeping...')
            time.sleep(60*15)
        i += 1

    return None

def main():
    # fill following info
    consumer_key = 
    consumer_secret = 
    access_token = 
    access_token_secret = 
    
    screen_name = 
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    get_friends_df(api, screen_name)


if __name__ == '__main__':
    main()