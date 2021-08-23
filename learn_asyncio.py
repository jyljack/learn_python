import asyncio


def callback(sleep_times):
    print("success time {}".format(sleep_times))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.call_later(2, callback, 2)
    loop.call_later(1, callback, 1)
    loop.call_later(3, callback, 3)

    loop.run_forever()
