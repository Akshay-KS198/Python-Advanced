import asyncio
import time

async def fun_process_1():
    print("First Step co-routine 1")
    await asyncio.sleep(3)
    print("Second Step co-routine 1")

async def fun_process_2():
    print("First Step co-routine 2")
    await asyncio.sleep(4)
    print("Second Step co-routine 2")


async def main():
    task = await asyncio.gather(fun_process_1(), fun_process_2())
    print("Main Executed")

asyncio.run(main())
