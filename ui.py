import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="Ollama LLaMA2 Chatbot", page_icon="💬")
st.title("💬 Yogi's Ollama LLaMA2 Chatbot")

# Store chat history in Streamlit session
if "history" not in st.session_state:
    st.session_state.history = []

# Display chat messages
for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state.history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Call FastAPI backend
    try:
        r = requests.post(API_URL, json={
            "message": user_input,
            "history": st.session_state.history[:-1]  # send previous history only
        }, timeout=300)
        r.raise_for_status()
        data = r.json()
        bot_reply = data["reply"]

    except Exception as e:
        bot_reply = f"❌ Error: {e}"

    # Show bot reply
    st.session_state.history.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

# Optional: Clear chat button
if st.button("🧹 Clear Chat"):
    st.session_state.history = []
    st.rerun()
