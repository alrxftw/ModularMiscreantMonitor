from twython import Twython

class twitterMon(object):

    thandle = object
    screenName = ''

    def __init__(self, screenName):
        self.screenName = screenName

        # Make check for existing access token
        # for now, instance a new one
        # API Keys, need to be moved out to a config file
        APP_KEY = 'smlE9GDdqG7HXTchIIu3zwXvS'
        APP_SECRET = 'BIFTIv4vaoADpxSzIAtaRuqJZh9IKwYva450LwzOZuLgrBgMO1'
        thandle = Twython(APP_KEY, APP_SECRET, oauth_version=2)
        ACCESS_TOKEN = thandle.obtain_access_token()
        # Get access token, save for later use in DB (with timeout?)
        thandle = Twython(APP_KEY, access_token=ACCESS_TOKEN)

    def getTimeline():
    
        timeline = thandle.get_user_timeline(screen_name=screenName, eclude_replies=True)
        for result in timeline:
            result
            print(result['text'])
            print('URLs in this tweet: ')
            for url in result['entities']['urls']:
                print(url['expanded_url'])