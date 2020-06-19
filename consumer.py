from pykafka import KafkaClient
from pykafka.common import OffsetType
from pykafka import exceptions
from pykafka.utils import serialize_utf8, deserialize_utf8
import baseconfig as cfg
import twitterDataModel


class CustomConsumer:
    def __init__(self):
        self.connection = False
        self.connection_status = ''
        self.client = None
        self.broker = cfg.kafkaconfig['broker']
        self.broker_v = cfg.kafkaconfig['broker-version']
    
    def connect_to_kafka_host(self):
        try:
            self.client = KafkaClient(hosts=self.broker, broker_version=self.broker_v)
            self.connection = True
            self.connection_status = 'Successfully Connected to Kafka Brokers'
        except ConnectionRefusedError:
            self.connection_status = 'Refused to Connect to Kafka Host'
        except ConnectionError as ce:
            self.connection_status = 'Error Connecting to Kafka Host'
        except TimeoutError as te:
            self.connection_status = 'Kafka Host Connection Timed Out'
        finally:
            print(self.connection_status)
    
    def consume_kafka(self, topic_name):
        try:
            kafka_consumer_topic = self.client.topics[topic_name]
            consumer = kafka_consumer_topic.get_balanced_consumer(consumer_group='twitter-feed', 
                                                                    zookeeper_connect= cfg.zookeeperconfig['zookeeper_host'],
                                                                    auto_commit_enable=True,
                                                                    #auto_commit_interval_ms=1000,
                                                                    #auto_offset_reset=OffsetType.EARLIEST,
                                                                    reset_offset_on_start=True,
                                                                    deserializer=deserialize_utf8
                                                                  ) 
            
            #consumer = kafka_consumer_topic.get_simple_consumer()   
            while True:
                message = consumer.consume()
                print(message)
                twitter_feed = twitterDataModel.TwitterFeed(message.value)
                print(twitter_feed)

        except Exception as e:
            print(e.message)

if __name__ == "__main__":
    custom_consumer = CustomConsumer()
    custom_consumer.connect_to_kafka_host()
    #twitter_feed = twitterDataModel.TwitterFeed()
    
    if(custom_consumer.connection):
        topic_to_consume = input('Enter the topic name to listen to: ')
        custom_consumer.consume_kafka(topic_to_consume)
    else:
        print('Could not connect - {0}'.format(custom_consumer.connection_status))
        
    