import asyncio


async def coroutine1():
    print("One Start")
    await asyncio.sleep(2)
    print("One End")

    return "One Done"


async def coroutine2():
    print("Two Start")
    await asyncio.sleep(5)
    print("Two End")

    return "Two Done"


async def main():
    tasks = [
        asyncio.create_task(coroutine1()),
        asyncio.create_task(coroutine2()),
    ]

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    print("Finished Tasks:")
    for t in done:
        print(t)
    print("\n" * 3)

    print("Pending Tasks:")
    for p in pending:
        print(p)

    await asyncio.wait(pending)

if __name__ == "__main__":
    asyncio.run(main())
