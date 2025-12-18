import requests


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama2"





OPTIONS = {
    "temperature" : 0.15,             #lower => more accuracy - focused
    "top_p" : 0.9,
    "top_k" : 40,
    "repeat_penalty" : 1.1,
    "num_ctx" : 1024
}



def chat():
    print("ollama llama chatbot.......")
    
    messages = [
    {"role": "system", "content": "You are a helpful assistant. type 'exit' to quit"}
    ]

    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit","quit"):
            print("Bye")
            break       
        
        
        messages.append({"role":"user", "content": user_input})
        
        
        resp = requests.post(OLLAMA_URL , json={
            "model":MODEL,
            "messages": messages,
            "stream":False
        }, timeout=300)
        
        
        resp.raise_for_status()
        data = resp.json()
        assistant_reply = data["message"]["content"]

        
        
        
        print("\nBot:", assistant_reply, "\n")
        messages.append({"role":"assistant", "content":assistant_reply})
        
        
if __name__ == "__main__":
    chat()