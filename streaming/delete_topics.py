from confluent_kafka.admin import AdminClient
import config
import logging
from admin_client import wait_for_admin_client
import argparse

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def delete_kafka_topics(broker_name, topics):
    admin_client = AdminClient({
        'bootstrap.servers': broker_name
    })
    wait_for_admin_client(admin_client)

    fs = admin_client.delete_topics(topics, operation_timeout=30)

    # Wait for operation to finish.
    for topic, f in fs.items():
        try:
            f.result()  # The result itself is None
            logging.info("Topic {} deleted".format(topic))
        except Exception as e:
            logging.info("Failed to delete topic {}: {}".format(topic, e))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Delete Kafka topics")
    parser.add_argument("topics", nargs="+", help="List of topic names to delete")
    args = parser.parse_args()

    # Kafka broker details
    broker_name = config.KAFKA_BROKER

    # Topic details
    # topic_names = ["anomalies", "transactions"]
    topic_names = args.topics

    # Delete the Kafka topics
    delete_kafka_topics(broker_name, topic_names)
