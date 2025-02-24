
from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi import Header
from fastapi import Body
from fastapi import HTTPException
from pydantic import BaseModel

import uvicorn

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():    
    return RedirectResponse("/static/index.html")

@app.get("/api/hello")
async def hello():
    return {"message": "Hello from FastAPI!"}

@app.get("/api/hello_error")
async def hello_error():
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/api/hello/{name}")
async def hello(name: str, user_agent: str = Header(default=None)):
    return {"message": f"Hello from FastAPI! {name}, agent {user_agent}"}

@app.post("/api/send_file")
async def send_file(body: str = Body(default=None)):
    print("Body received:")
    print(body)

    return {"message": "uploaded"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message received: {data}")
    except:
        await websocket.close()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5010)
