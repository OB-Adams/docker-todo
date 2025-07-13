import os
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, Field

MONGODB_CONNECTION_STRING = os.environ["MONGODB_CONNECTION_STRING"]

client = AsyncIOMotorClient(MONGODB_CONNECTION_STRING, uuidRepresentation="standard")

db = client.todolist
todos = db.todos
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TodoItem(BaseModel):
    id: UUID = Field(default_factory=uuid4, alias="_id")
    content: str

class TodoItemCreate(BaseModel):
    content: str


@app.post("/todos", response_model=TodoItem)
async def create_todo(item: TodoItemCreate):
    new_todo = TodoItem(content=item.content)
    await todos.insert_one(new_todo.model_dump(by_alias=True))
    return new_todo

@app.get("/todos", response_model=list[TodoItem])
async def read_todos():
    return await todos.find().to_list(length=None)

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: UUID):
    result = await todos.delete_one({"_id": todo_id})
    if result.deleted_count == 1:
        return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")