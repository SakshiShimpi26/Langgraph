import streamlit as st
import uuid
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from backend import chat   # YOUR existing LangGraph object

load_dotenv()

st.set_page_config(page_title="LangGraph Chatbot", layout="wide")

# ---------------------------
# Session storage
# ---------------------------
if "chats" not in st.session_state:
    st.session_state.chats = {}   # {chat_id: [ {role, content}, ... ]}

if "active_chat" not in st.session_state:
    st.session_state.active_chat = None

# ---------------------------
# Sidebar UI (Chat list)
# ---------------------------
with st.sidebar:
    st.title("LangGraph Chatbot")

    # For New chats creation with UUID no chat name in sidebar
    # if st.button("➕ New Chat"):
    #     chat_id = str(uuid.uuid4())
    #     st.session_state.active_chat = chat_id
    #     st.session_state.chats[chat_id] = []

    # For New chats creations with chat name in sidebar
    new_chat_name = st.text_input("New chat name")

    if st.button("➕ Create Chat") and new_chat_name:
        if new_chat_name not in st.session_state.chats:
            st.session_state.chats[new_chat_name] = []
            st.session_state.active_chat = new_chat_name
        else:
            st.warning("Chat name already exists")

    st.divider()
    st.subheader("My Conversations")

    for cid in st.session_state.chats:
        if st.button(cid, key=cid):
            st.session_state.active_chat = cid

# ---------------------------
# Main UI
# ---------------------------
st.subheader("LangGraph Powered AI Chat")

if st.session_state.active_chat is None:
    st.info("Create or select a chat to begin")
    st.stop()

messages = st.session_state.chats[st.session_state.active_chat]

# Show previous messages
for message in messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Type here...")

# IMPORTANT — LangGraph memory binding
config = {
    "configurable": {
        "thread_id": st.session_state.active_chat
    }
}

if user_input:

    # Store user message
    messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Stream assistant reply
    with st.chat_message("assistant"):
        ai_message = st.write_stream(
            chunk.content
            for chunk, _ in chat.stream(
                {"message": [HumanMessage(content=user_input)]},
                stream_mode="messages",
                config=config
            )
        )

    # Store assistant message
    messages.append({"role": "assistant", "content": ai_message})
