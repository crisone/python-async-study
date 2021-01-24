import asyncio
import subprocess

async def ping(addr):
    cmd = f"ping {addr}"
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
        )
    # tt = asyncio.create_task(proc.communicate())
    while True:
        l = asyncio.create_task(proc.stdout.readline())
        await l
        print(l.result())
    # try:
        # await asyncio.wait_for(tt, timeout = 1.0)
    # except asyncio.TimeoutError:
        # print(tt.result()[0])

async def main():
    a = loop.create_task(ping("www.baidu.com"))
    b = loop.create_task(ping("www.google.com"))
    await asyncio.wait([a, b])


if __name__=="__main__":
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # asyncio.run(main())
    loop.run_until_complete(main())