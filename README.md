# real-time-anomaly-detection
This is an attempt to learn Kafka by building a real-time anomaly detection system using the IsolationForest algorithm.

## Setup
Run the following commands in two terminal sessions to start the Producer and Consumer in your local machine.

- To Run the Producer:

```bash
kafka-console-producer --topic topic1 --bootstrap-server localhost:29092
```

- To Run the Consumer:

```bash
kafka-console-consumer --topic topic1 --from-beginning --bootstrap-server localhost:29092
```


Run the following commands in two terminal sessions to start the Producer and Consumer in the Docker container itself.

- To Run the Producer:

```bash
docker exec -it kafka kafka-console-producer.sh --topic topic1 --bootstrap-server localhost:9092
```

- To Run the Consumer:

```bash
docker exec -it kafka kafka-console-consumer.sh --topic topic1 --from-beginning --bootstrap-server localhost:9092
```