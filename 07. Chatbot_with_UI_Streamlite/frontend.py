from backend import chat
import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage
load_dotenv()

st.title("💬 My AI Chatbot")

st.subheader("Langgraph Powered AI Chat....")

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input('Type here')

if user_input:
    # Add user message to history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    # Define thread_id for checkpointer
    config = {"configurable": {"thread_id": "thread-1"}}

    # Stream AI response
    with st.chat_message('assistant'):
        ai_message = st.write_stream(
            chunk.content
            for chunk, _ in chat.stream(
                {"message": [HumanMessage(content=user_input)]},
                stream_mode="messages",
                **config  # pass thread_id here
            )
        )

    # Save bot reply
    st.session_state['message_history'].append(
        {'role': 'assistant', 'content': ai_message}
    )
