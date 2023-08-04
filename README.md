# real-time-anomaly-detection
This is an attempt to learn Kafka by building a real-time anomaly detection system using the IsolationForest algorithm.

Run the following commands in two terminal sessions

To Run the Producer:
```docker exec -it kafka kafka-console-producer.sh --topic topic1 --bootstrap-server localhost:9092```

To Run the Consumer:
```docker exec -it kafka kafka-console-consumer.sh --topic topic1 --from-beginning --bootstrap-server localhost:9092```