import baseconfig as cfg
import csv, re, json
from pathlib import Path
from tweepy import Stream
from tweepy import StreamListener
from tweepy import OAuthHandler
import producer

# base_path = Path(__file__).parent
# file_path = (base_path / './twitterFiles').resolve()
# print(file_path)

#Twitter Authentication
class TwitterAuthentication:
    @classmethod
    def get_twitter_authentication(cls, api_key, api_secret, access_token, access_token_secret):
        try:
            auth = OAuthHandler(api_key, api_secret)
            auth.set_access_token(access_token, access_token_secret)
            return auth
        except ConnectionError:
            return 'Connection Error'
        
#StreamListener
class TwitterStreamListener(StreamListener):    
    def __init__(self, topic):
        self.topic = topic
        self.twitter_topics = []
        self.store_twitter_topics()
    
    def on_connect(self):
        print('Twitter Streaming is Enabled')
    
    def on_disconnect(self):
        print('Twitter Streaming is disabled')
    
    def on_data(self, data): 
        kafka_producer_status = kafka_producer.produce_data(data, self.topic)
        if(kafka_producer_status == 'Kafka Error'):
           print(kafka_producer_status) 
        else:
            return True
      
    def on_error(self, status_code):
        if status_code == 420:
            return False
        
    def store_twitter_topics(self):
        if self.topic not in self.twitter_topics:
            self.twitter_topics.append(self.topic)


if __name__ == "__main__":
    try:
        #Initializing KafkaClient
        kafka_producer = producer.CustomProducerKafka()
        kafka_producer.connect_to_kafka_host()       
        
        if(kafka_producer.connection):
            chosen_topic = input('Enter the topic name: ')
        else:
            print('Could Not Connect - {0}'.format(kafka_producer.connection_status))
        
        #Twitter Authentication
        twitter_auth = TwitterAuthentication.get_twitter_authentication(cfg.twitterconfig['consumer_api_key'], 
                                                                        cfg.twitterconfig['consumer_api_secret'], 
                                                                        cfg.twitterconfig['user_access_token'], 
                                                                        cfg.twitterconfig['user_access_token_secret'])
        if (twitter_auth != 'Connection Error'):
            twitter_stream_listener = TwitterStreamListener(chosen_topic)     
            twitter_stream = Stream(twitter_auth, twitter_stream_listener)  
        else:
            twitter_stream_listener = TwitterStreamListener(chosen_topic)     
        
        #Filtering on certain keywords in Twitter:
        chosen_filter = input('Enter the hashtag filter: ')
        chosen_filters = re.split(', | \n', chosen_filter)
        twitter_stream.filter(track=chosen_filters, is_async=True)

    except Exception as e:
        print(e)
    
