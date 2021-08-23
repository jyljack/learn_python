import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        params = {'key1': 'value1', 'key2': 'value2'}
        async with session.get('http://httpbin.org/get', params=params) as response:
            print("Url:", response.url)
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:100], "...")
        async with session.post('http://httpbin.org/post', data=b'data') as response:
            print("Url:", response.url)
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:100], "...")
        async with session.ws_connect('ws://localhost:8765') as ws:
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    if msg.data == 'close cmd':
                        await ws.close()
                        break
                    else:
                        await ws.send_str('answer')
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    break


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
