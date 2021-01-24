import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as ws:
        await ws.send("Hello world")
        greeting = await ws.recv()
        print(greeting)
    
asyncio.get_event_loop().run_until_complete(hello())
