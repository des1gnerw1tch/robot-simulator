"""Publishes a message to SUBJECT once per second."""

import asyncio

import nats

from examples.constants import SERVER_URL, SUBJECT


async def main():
    nc = await nats.connect(SERVER_URL)

    try:
        count = 0
        while True:
            payload = f"hello #{count}"
            await nc.publish(SUBJECT, payload.encode())
            print(f"Published to {SUBJECT}: {payload}")
            count += 1
            await asyncio.sleep(1)
    finally:
        await nc.drain()


if __name__ == "__main__":
    asyncio.run(main())
