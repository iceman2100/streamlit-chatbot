import streamlit as st
from groq import Groq

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")
st.title("🤖 Groq AI Chatbot")

# -----------------------------
# Load API key
# -----------------------------
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# -----------------------------
# UI chat history (for display only)
# -----------------------------
if "ui_messages" not in st.session_state:
    st.session_state.ui_messages = []

# -----------------------------
# API chat history (STRICT format)
# -----------------------------
if "api_messages" not in st.session_state:
    st.session_state.api_messages = [
        {
            "role": "system",
            "content": "You are a helpful, polite AI assistant."
        }
    ]

# -----------------------------
# Display previous messages
# -----------------------------
for msg in st.session_state.ui_messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# User input
# -----------------------------
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message in UI
    st.session_state.ui_messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # Add user message to API history
    st.session_state.api_messages.append(
        {"role": "user", "content": user_input}
    )

    # -----------------------------
    # Call Groq API
    # -----------------------------
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=st.session_state.api_messages,
        temperature=0.7
    )

    bot_reply = response.choices[0].message.content

    # Show assistant message in UI
    st.session_state.ui_messages.append(
        {"role": "assistant", "content": bot_reply}
    )
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    # Add assistant message to API history
    st.session_state.api_messages.append(
        {"role": "assistant", "content": bot_reply}
    )
