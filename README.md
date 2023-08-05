# Real Time Anomaly Detection using Kafka
This is an attempt to learn Kafka by building a real-time anomaly detection system using the IsolationForest algorithm.

## Steps to run the project
1. Run ```docker compose up -d``` which will start the Kafka and Zookeeper containers.
2. Run ```python3 streaming/create_topic.py``` to create the topics in Kafka.
3. Run ```python3 streaming/producer.py``` to start the producer in one terminal.
4. Run ```python3 streaming/consumer.py``` to start the consumer in another terminal.

To see the result of the anomaly detection, Run ```kafka-console-consumer --topic anomalies --from-beginning --bootstrap-server localhost:29092``` which will log the anomalies detected by the algorithm.

To see the transactions being sent to Kafka, Run ```kafka-console-consumer --topic transactions --from-beginning --bootstrap-server localhost:29092``` which will log the transactions sent to Kafka.

## Sample Usage Commands
[ ] Run the following commands in two terminal sessions to start the Producer and Consumer in your local machine.

- To Run the Producer:

```bash
kafka-console-producer --topic topic1 --bootstrap-server localhost:29092
```

- To Run the Consumer:

```bash
kafka-console-consumer --topic topic1 --from-beginning --bootstrap-server localhost:29092
```

-----------------------------------------------------------------------------

[ ] Run the following commands in two terminal sessions to start the Producer and Consumer in the Docker container itself.

- To Run the Producer:

```bash
docker exec -it kafka kafka-console-producer.sh --topic topic1 --bootstrap-server localhost:9092
```

- To Run the Consumer:

```bash
docker exec -it kafka kafka-console-consumer.sh --topic topic1 --from-beginning --bootstrap-server localhost:9092
```