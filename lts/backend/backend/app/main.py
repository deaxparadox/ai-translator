from typing import Union

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import app.settings.local as settings
from app.schema import HelloModel
from app.ws import manager
from app.database import engine, SessionLocal, get_db

from app.history import schema, models
from app.history.app import router as history_router

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    history_router,
    prefix="/history",
    tags=['history'],
)

# Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=settings.ALLOWED_METHODS,
    allow_headers=settings.ALLOWED_HEADERS,
)


@app.get("/", response_model=HelloModel)
async def read_root(db: Session = Depends(get_db)):
    # print(db.query(model.History).get("2024-02-23T13:50:02.711114"))
    # print(db.query(model.History).filter(model.History.id=="2024-02-23T13:50:02.711114").first())
    # for q in db.query(model.History).all():
    #     print(q)
    # history = model.History(english="What is your name?", hindi="नमस्ते")
    # db.add(history)
    # db.commit()
    # db.refresh(history)
    # print(history)
    # return {"message": settings.transcriber("hello everyone")[0]["translation_text"]}
    return {"message": "Hello Everyone"}


# @app.get("/history", response_model=schema.Histories)
# async def read_root(db: Session = Depends(get_db)):
#     histories = db.query(models.History).filter(models.History.id=="2024-02-23T13:50:02.711114")
#     return {
#         'histories': histories
#     }

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.websocket("/ws/translate")
async def websocket_connect(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            data = settings.transcriber(data)[0]['translation_text']
            await manager.send_personal_message(f"{data}", websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)

@app.websocket("/ws/clients/{client_id}")
async def websocket_connect_multiple(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")