import json
import os
from joblib import load
import logging
from multiprocessing import Process

import numpy as np

from create_consumer_producer import create_producer, create_consumer
import config

model_path = os.path.abspath('../training/model.joblib')


def detect():
    consumer = create_consumer(topic=config.TRANSACTIONS_TOPIC, group_id=config.TRANSACTIONS_CONSUMER_GROUP)

    producer = create_producer()

    clf = load(model_path)

    while True:
        message = consumer.poll(timeout=50)
        if message is None:
            continue
        if message.error():
            logging.error("Consumer error: {}".format(message.error()))
            continue

        # Message that came from producer
        record = json.loads(message.value().decode('utf-8'))
        data = record["data"]

        prediction = clf.predict(data)

        # If an anomaly comes in, send it to anomalies topic
        if prediction[0] == -1:
            score = clf.score_samples(data)
            record["score"] = np.round(score, 3).tolist()

            _id = str(record["id"])
            record = json.dumps(record).encode("utf-8")
            # print("Anomaly detected: {}".format(record))

            producer.produce(topic=config.ANOMALIES_TOPIC,
                             value=record)
            producer.flush()


    consumer.close()


# One consumer per partition
if __name__ == "__main__":
    for _ in range(config.NUM_PARTITIONS):
        p = Process(target=detect)
        p.start()