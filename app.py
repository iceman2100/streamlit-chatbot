import streamlit as st
from groq import Groq

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(page_title="My AI Chatbot", page_icon="🤖")
st.title("🤖 My AI Chatbot")

# -----------------------------
# Load API key from Streamlit secrets
# -----------------------------
api_key = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=api_key)

# -----------------------------
# Initialize chat history
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        }
    ]


# -----------------------------
# Display previous messages
# -----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# User input box
# -----------------------------
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # Call Groq API
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=st.session_state.messages
    )

    bot_reply = response.choices[0].message.content

    # Show bot message
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
