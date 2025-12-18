from fastapi import FastAPI
from pydantic import BaseModel
import requests


app = FastAPI()


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama2"



OPTIONS = {
    "temperature" : 0.2,             #accuracy - focused
    "top_p" : 0.9,
    "top_k" : 40,
    "repeat_penalty" : 1.1,
    "num_ctx" : 1024
}

class ChatRequest(BaseModel):
    message : str
    history : list[dict] = []
    
@app.post("/chat")
def chat(req : ChatRequest):
    messages = [{"role":"system", "content": "you are a helpful assistant....."}]
    messages += req.history
    messages.append({"role" : "user", "content": req.message})
    
    
    r = requests.post(OLLAMA_URL, json={
        "model" : MODEL,
        "messages" : messages,
        "stream" : False
    }, timeout=300)
    r.raise_for_status()
    
    
    
    
    reply = r.json()["message"]["content"]
    messages.append({"role" : "assistant", "content" : reply})
    
    
    
    
    #return updated history (excluding system)
    
    return {"reply" : reply, "history" : messages[1:]}



# @app.get("/")
# def home():
#     return {"status": "ok", "message": "FastAPI is running. Use POST /chat"}
