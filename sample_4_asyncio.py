import asyncio
import random

async def long_operation():
    duration: int = random.randint(1, 10)
    await asyncio.sleep(duration)


async def main():
    try:
        await asyncio.wait_for(long_operation(), timeout=5)
        print("Process completed")
    except asyncio.TimeoutError:
        print("Took too long...")


if __name__ == '__main__':
    asyncio.run(main())
