import json
import random
import time
from datetime import datetime
import numpy as np
import config
from create_consumer_producer import create_producer

_id = 0
producer = create_producer()

if producer is not None:
    while True:
        # Generate some abnormal observations
        if random.random() <= config.OUTLIERS_GENERATION_PROBABILITY:
            X_test = np.random.uniform(low=-4, high=4, size=(1, 2))
        else:
            X = 0.3 * np.random.randn(1, 2)
            X_test = (X + np.random.choice(a=[2, -2], size=1, p=[0.5, 0.5]))

        X_test = np.round(X_test, 3).tolist()

        current_time = datetime.utcnow().isoformat()

        record = {"id": _id, "data": X_test, "current_time": current_time}
        # print(record)
        record = json.dumps(record).encode("utf-8")

        producer.produce(topic=config.TRANSACTIONS_TOPIC,
                         value=record)
        producer.flush()
        _id += 1
        time.sleep(config.DELAY)
