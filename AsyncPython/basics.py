import asyncio
import time

async def fun_process_1():
    print("First Step co-routine 1")
    await asyncio.sleep(6)
    result = await fun_process_2()
    print("Second Step co-routine 1")
    print(f"fun_process_1 result is {result}")

async def fun_process_2():
    print("First Step co-routine 2")
    await asyncio.sleep(8)
    print("Second Step co-routine 2")
    return "Akshay is a Good Boy"

asyncio.run(fun_process_1())


