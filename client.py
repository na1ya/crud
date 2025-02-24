import httpx
import requests
import asyncio
import websockets

async def make_request():
    name="nina"
    response = requests.get(f"http://127.0.0.1:5010/api/hello/{name}")
    print(response.status_code)
    print(response.json())

async def make_request_nonblocking():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://127.0.0.1:5010/api/hello")
        print(response.status_code)
        print(response.json())

async def make_post():
    async with httpx.AsyncClient() as client:
        response = await client.post("http://127.0.0.1:5010/api/send_file", json="test data")
        print(response.status_code)
        print(response.json())

async def websocket_client():
    uri = "ws://example.com/socket"  # Replace with your WebSocket server URL
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello, WebSocket!")  # Send message
        response = await websocket.recv()  # Receive response
        print(f"✅ Received: {response}")

async def some_tasks():
    tasks = []
    tasks.append(asyncio.create_task(make_request()))
    tasks.append(asyncio.create_task(make_request_nonblocking()))
    tasks.append(asyncio.create_task(make_post()))
    tasks.append(asyncio.create_task(websocket_client()))
    await asyncio.gather(*tasks)

asyncio.run(make_request())
