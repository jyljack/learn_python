import asyncio
import aioredis


async def main():
    redis = aioredis.from_url("redis://152.32.146.94", db=0, decode_responses=True, password="redis", encoding="utf-8")
    await redis.set("demo-key", "demo-value")
    value = await redis.get("demo-key")
    await redis.close()
    print(value)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
