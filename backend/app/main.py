from fastapi import FastAPI # Main class starts the app
from fastapi.responses import JSONResponse # For responsing JSON formatted responses to browser

from .schemas import ChatRequest, ChatResponse
from .gpt_service import generate_reply

from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Güvenlik için "*" yerine "http://localhost:3000" önerilir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Test with
'''
cd backend
uvicorn app.main:app --reload
''' 
@app.get("/ping")
def ping():
    return JSONResponse(content={"message":"pong"})


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    reply = generate_reply(request.message)
    return {"reply": reply}