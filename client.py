import requests
import asyncio
import time

async def sleep_time(sec: int):
    loop = asyncio.get_running_loop()
    res = await loop.run_in_executor(None, requests.get, f"http://127.0.0.1:8000/sleep_time/?sec={sec}")
    return res.text

async def main():
    print(f"Sending request to server... {time.strftime('%X')}")
    res = await asyncio.gather(sleep_time(1), sleep_time(2), sleep_time(3))   
    print(res)
    print(f"Received response from server... {time.strftime('%X')}")


if __name__ == "__main__":
    asyncio.run(main())