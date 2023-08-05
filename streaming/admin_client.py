def wait_for_admin_client(admin_client):
    # Wait until the admin client is connected to the Kafka cluster
    while True:
        metadata = admin_client.list_topics(timeout=5)
        if metadata is not None:
            break
        admin_client.poll(0.1)
