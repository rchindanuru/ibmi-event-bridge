import json
from pathlib import Path

try:
    from kafka import KafkaProducer  # from kafka-python
except ImportError:
    KafkaProducer = None


def load_events(path: str):
    p = Path(path)
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)


def main():
    orders = load_events("samples/events/orders.json")
    inventory = load_events("samples/events/inventory.json")
    jobs = load_events("samples/events/jobs.json")

    all_events = orders + inventory + jobs

    if KafkaProducer is None:
        print("KafkaProducer not installed. Showing messages that would be sent:")
        for event in all_events:
            print(json.dumps(event))
        return

    producer = KafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        key_serializer=lambda k: k.encode("utf-8"),
    )

    for event in all_events:
        key = event.get("event_type", "unknown")
        producer.send("ibmi-events", key=key, value=event)

    producer.flush()
    producer.close()
    print("Events sent to Kafka topic 'ibmi-events'.")


if __name__ == "__main__":
    main()
