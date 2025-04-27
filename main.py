from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, or specify your Google Sites domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app = FastAPI()

class FormData(BaseModel):
    option: str
    userInput: str

@app.post("/submit")
async def submit_form(data: FormData):
    print(f"Received data: {data}")
    # You can save it to database, file, etc.
    return {"message": "Data received successfully"}
