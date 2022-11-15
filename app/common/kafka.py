import asyncio

from aiokafka import AIOKafkaProducer, AIOKafkaConsumer


class Kafka:
    loop = asyncio.get_event_loop()
    producer = AIOKafkaProducer(loop=loop, bootstrap_servers='localhost:29092')
    consumer = AIOKafkaConsumer('fastapi_topic', bootstrap_servers='localhost:29092', loop=loop)

    async def consume(self):
        await self.consumer.start()
        try:
            async for msg in self.consumer:
                print(
                    msg.topic,
                    msg.partition,
                    msg.offset,
                    msg.key,
                    msg.value,
                    msg.timestamp,
                )

        finally:
            await self.consumer.stop()

    async def start(self):
        await self.producer.start()
        self.loop.create_task(self.consume())
