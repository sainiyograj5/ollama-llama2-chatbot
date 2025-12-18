# Ollama LLaMA2 Chatbot 🤖

A local AI chatbot built using **Streamlit**, **FastAPI**, and **Ollama (LLaMA2)**.  
This project demonstrates how to build a full-stack chatbot that runs completely on a local machine without relying on paid APIs.

---

## 🚀 Features

- 💬 Interactive chat UI using Streamlit  
- ⚡ FastAPI backend for handling requests  
- 🧠 LLaMA2 model served locally via Ollama  
- 🔄 Chat history maintained during session  
- 🔐 Fully local & private (no external API calls)

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit** – Frontend UI
- **FastAPI** – Backend API
- **Ollama** – Local LLaMA2 model
- **Requests** – API communication

---

## 📂 Project Structure

```text
ollama-llama2-chatbot/
│
├── app.py        # FastAPI backend
├── chat.py       # Ollama / LLaMA2 interaction logic
├── ui.py         # Streamlit frontend
├── screenshots/  # Project screenshots
├── .gitignore
└── README.md



# Ollama LLaMA2 Chatbot

A chatbot built using Streamlit, FastAPI, and Ollama LLaMA2.

## Screenshots

![Chat UI](screenshots/chat-ui.png)




#HOW TO US EMY PROJECT ON UR MACHINE
#FOLLOW THE STEPS BELOW


⚙️ Setup & Installation
1️⃣ Clone the repository
git clone https://github.com/sainiyogra5/ollama-llama2-chatbot.git
cd ollama-llama2-chatbot

2️⃣ Create virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ How to Run
Start Ollama

Make sure Ollama is installed and the LLaMA2 model is pulled:

ollama pull llama2

Start Backend (FastAPI)
python app.py

Start Frontend (Streamlit)
streamlit run ui.py


Open browser at:

http://localhost:8501
