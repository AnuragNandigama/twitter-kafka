from pykafka import KafkaClient
from pykafka import exceptions
from pykafka.utils import serialize_utf8, deserialize_utf8
import baseconfig as cfg
import json

class CustomProducerKafka:    
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
        except ConnectionError:
            self.connection_status = 'Error Connecting to Kafka Host'
        except TimeoutError:                                                                             
            self.connection_status = 'Kafka Host Connection Timed Out'
        finally:
            print(self.connection_status)
    
    def produce_data(self, data_to_produce, topic_name):
        try:
            #Creating the topic
            kafka_producer_topic = self.client.topics[topic_name]
            #Producing
            with kafka_producer_topic.get_sync_producer(serializer=serialize_utf8) as producer:
                producer.produce(data_to_produce) 
                #producer.produce('This is Python Message')
                print('PRODUCER------------------------IS------------------------------WORKING')  
                print(data_to_produce)             
        except TypeError:
            #print(te.message)
            return ('Kafka Error')
        