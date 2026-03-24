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

