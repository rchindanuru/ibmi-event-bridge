# ibmi-event-bridge
Sample code that turns IBM i business events (orders, inventory, jobs) into messages ready for Kafka, queues, or cloud analytics.

## What this repo is for

- Show how to shape IBM i events as clean JSON messages.
- Demonstrate simple producers that can send these events to Kafka or other event backbones.
- Provide starting points for connecting legacy workloads to modern, event-driven systems.

## Sample event files

Under `samples/events` you will find:

- `orders.json`: Example order events from IBM i order processing.
- `inventory.json`: Example inventory adjustment events from an IBM i-based warehouse or factory.
- `jobs.json`: Example job status events for batch jobs.

These files show how IBM i business events can be represented as JSON messages ready for streaming platforms and analytics.

## Python Kafka producer example

The script at `producers/python/kafka_producer_example.py` demonstrates how to send these events to a Kafka topic.

Basic idea:

- Read JSON events from the `samples/events` folder.
- For each event, send a message to a Kafka topic (for example, `ibmi-events`).

If you have Python and kafka-python installed, and Kafka running locally:

```bash
pip install kafka-python
python producers/python/kafka_producer_example.py
```

If `kafka-python` is not installed, the script will just print the messages it would send. This is still useful for seeing the event format.
