import asyncio
import multiprocessing
from websockets.sync.client import connect


async def hello():
    with connect("ws://localhost:8000/ws/translate/") as websocket:
        websocket.send("Hello world!")
        message = websocket.recv()
        print(f"Received: {message}")
if __name__ == "__main__":
    asyncio.run(hello())