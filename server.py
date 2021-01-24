import asyncio
import websockets

class TestMgr:
    def __init__(self):
        self.bb = 10086

    async def ws_handler(self, ws, path):
        async for m in ws:
            print(m, " --- ", self.bb)
            await ws.send("hi there")
    
    def run_server(self):
        self.server = websockets.serve(
            self.ws_handler, 
            "localhost",
            8765
        )
        asyncio.get_event_loop().run_until_complete(self.server)
        asyncio.get_event_loop().run_forever()

if __name__=="__main__":
    t = TestMgr()
    t.run_server()