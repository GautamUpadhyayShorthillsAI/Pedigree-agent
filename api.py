from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from main import main_async
app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    text: str

@app.post("/process")
async def process_text(input_data: TextInput, request: Request):
    # Access request details
    client_host = request.client.host
    headers = request.headers
    method = request.method
    url = str(request.url)
    agent_response = await main_async(input_data.text)
    return {
        "agent_response":agent_response
    }

if __name__ == "__main__":
    # Run FastAPI app directly with uvicorn
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
