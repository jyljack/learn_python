import aioamqp
import asyncio
import logging
  
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


async def receive():
    await asyncio.sleep(2)
    try:
        transport, protocol = await aioamqp.connect(host='localhost', port=5672, login='admin', password='admin',
                                                    virtualhost='vh_admin', login_method='PLAIN')
    except aioamqp.AioamqpException:
        logging.error("Error")
        return

    channel = await protocol.channel()
    # generate a random queue name
    result = await channel.queue_declare(queue_name='demo.queue')
    #  binds queue to the exchange
    queue_name = result['queue']
    logging.debug(queue_name)
    # configure the QOS: it specifies how the worker unqueues message.
    await channel.queue_bind(exchange_name='demo.exchange', queue_name="demo.queue", routing_key='demo.queue')

    await channel.basic_qos(prefetch_count=1, prefetch_size=0, connection_global=False)

    await channel.basic_consume(callback, queue_name='demo.queue')


async def publish():
    try:
        transport, protocol = await aioamqp.connect(host='localhost', port=5672,
                                                    login='admin', password='admin',
                                                    virtualhost='vh_admin', login_method='PLAIN')
    except aioamqp.AioamqpException:
        logging.error("Error")
        return
    channel = await protocol.channel()

    message = 'Hello World'
    await channel.exchange_declare(exchange_name='demo.exchange', type_name='topic')
    await channel.basic_publish(message, exchange_name='demo.exchange', routing_key='demo.queue')


async def callback(channel, body, envelope, properties):
    logging.debug("consumer {} received {} ({})".format(envelope.consumer_tag, body, envelope.delivery_tag))
    await channel.basic_client_ack(delivery_tag=envelope.delivery_tag)


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.create_task(publish())
    event_loop.create_task(receive())
    event_loop.run_forever()
