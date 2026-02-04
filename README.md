# 🤖 Groq AI Chatbot (Streamlit)

This is a simple web-based AI chatbot built using **Streamlit** and the **Groq API**.

The app runs completely on the internet and allows users to chat with an AI model through a clean web interface.

---

## 🚀 Features

- Fully web-based chatbot
- Built using Python and Streamlit
- Uses Groq LLMs (LLaMA 3.1)
- Secure API key handling with Streamlit Secrets
- Chat history support
- Easy to deploy and share

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Groq API (LLaMA 3.1)

---

## 📦 Installation & Setup

### 1. Clone the repository
```bash
```
git clone https://github.com/your-/streamlit-chatbot.git
cd streamlit-chatbot
2. Install dependencies
pip install -r requirements.txt

3. Add API Key (Important)

Create a .streamlit/secrets.toml file and add:

GROQ_API_KEY = "your_groq_api_key_here"

▶️ Run the App Locally
streamlit run app.py


Open the browser at:

[http://localhost:8501](https://app-chatbot-theqcapv6ll8wnqdymqmuw.streamlit.app/)

🌐 Deployment

This app can be deployed easily using Streamlit Cloud.

Push code to GitHub

Connect the repo to Streamlit Cloud

Add GROQ_API_KEY in Streamlit Secrets

Deploy and share the app link

🔒 Security Note

Never hardcode API keys in the source code

Always use environment variables or Streamlit Secrets

📌 Model Used

llama-3.1-8b-instant (Groq)

✅ Status

✔️ Working
✔️ Cloud-based
✔️ Shareable
