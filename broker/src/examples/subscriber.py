"""Subscribes to SUBJECT and prints each message received."""

import asyncio

import nats

from examples.constants import SERVER_URL, SUBJECT


async def main():
    nc = await nats.connect(SERVER_URL)
    sub = await nc.subscribe(SUBJECT)
    print(f"Subscribed to {SUBJECT}")

    try:
        async for msg in sub.messages:
            print(f"Received on {msg.subject}: {msg.data.decode()}")
    finally:
        await nc.drain()


if __name__ == "__main__":
    asyncio.run(main())
