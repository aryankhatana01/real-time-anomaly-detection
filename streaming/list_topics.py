from confluent_kafka.admin import AdminClient
import config
from admin_client import wait_for_admin_client

def list_kafka_topics(broker_name):
    # Configure the admin client with the bootstrap servers
    admin_client = AdminClient({
        'bootstrap.servers': broker_name
    })
    wait_for_admin_client(admin_client)

    # List the topics
    topics = admin_client.list_topics(timeout=5)
    return topics.topics

if __name__ == "__main__":
    # Kafka broker details
    broker_name = config.KAFKA_BROKER

    # List the Kafka topics
    topics = list_kafka_topics(broker_name)
    print(topics)
