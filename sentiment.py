import sys
import time
import re
import nltk
import tweepy
from sklearn.externals import joblib

#Prerocessing Tweets

def preprocessTweets(tweet):
    
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    
    #Convert @username to __HANDLE
    tweet = re.sub('@[^\s]+','__HANDLE',tweet)  
    
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    
    #trim
    tweet = tweet.strip('\'"')
    
    # Repeating words like happyyyyyyyy
    rpt_regex = re.compile(r"(.)\1{1,}", re.IGNORECASE)
    tweet = rpt_regex.sub(r"\1\1", tweet)
    
    #Emoticons
    emoticons = \
    [
     ('__positive__',[ ':-)', ':)', '(:', '(-:', \
                       ':-D', ':D', 'X-D', 'XD', 'xD', \
                       '<3', ':\*', ';-)', ';)', ';-D', ';D', '(;', '(-;', ] ),\
     ('__negative__', [':-(', ':(', '(:', '(-:', ':,(',\
                       ':\'(', ':"(', ':((', ] ),\
    ]

    def replace_parenth(arr):
       return [text.replace(')', '[)}\]]').replace('(', '[({\[]') for text in arr]
    
    def regex_join(arr):
        return '(' + '|'.join( arr ) + ')'

    emoticons_regex = [ (repl, re.compile(regex_join(replace_parenth(regx))) ) \
            for (repl, regx) in emoticons ]
    
    for (repl, regx) in emoticons_regex :
        tweet = re.sub(regx, ' '+repl+' ', tweet)

     #Convert to lower case
    tweet = tweet.lower()
    
    return tweet

#Stemming of Tweets

def stem(tweet):
        stemmer = nltk.stem.PorterStemmer()
        tweet_stem = ''
        words = [word if(word[0:2]=='__') else word.lower() \
                    for word in tweet.split() \
                    if len(word) >= 3]
        words = [stemmer.stem(w) for w in words] 
        tweet_stem = ' '.join(words)
        return tweet_stem


#Predict the sentiment

def predict(tweet,classifier):
    
    tweet_processed = stem(preprocessTweets(tweet))
             
    if ( ('__positive__') in (tweet_processed)):
         sentiment  = 1
         return sentiment
        
    elif ( ('__negative__') in (tweet_processed)):
         sentiment  = 0
         return sentiment       
    else:
        
        X =  [tweet_processed]
        sentiment = classifier.predict(X)
        return (sentiment[0])

def tweets(classifier,auth):
    api = tweepy.API(auth)
    key = input('Enter search term for tweets\n')
    public_tweets = api.search(q=key, lang='en')
    for tweet in public_tweets:
        print(tweet.text)
        print(predict(tweet.text,classifier))
    return

def console(classifier):
    tweet = ' '
    tweet = input('Enter the message to check its sentiment\n')
    print(predict(tweet, classifier))

# Main function

def main():
    print('Loading the Classifier, please wait....')
    classifier = joblib.load('svmClassifier.pkl')
    print('READY')

    while(1):
        print('**MENU**\n1. Type message on the console\n2. Get realtime tweets from Twitter\n3. Exit')
        ch = input('Enter Choice\n')

        if(ch=='1'):
            console(classifier)
            continue

        if(ch=='2'):

            consumer_key = 'EnterYourOwn'
            consumer_secret = 'EnterYourOwn'

            access_token = 'EnterYourOwn'
            access_token_secret = 'EnterYourOwn'

            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            tweets(classifier,auth)
            continue

        if(ch=='3'):
            sys.exit(1)

        else:
            print('Invalid Choice.')
            
            
            
if __name__ == "__main__":
    main()
        

