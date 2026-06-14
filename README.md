# My-Glitter-Dash
 # ✨ My Glitter Dash

My Glitter Dash is an AI-powered productivity and personal dashboard built with **Streamlit** and **Google Gemini AI**. It combines a beautiful, glitter-themed interface with intelligent features to help users organize tasks, capture ideas, and interact with an AI assistant in one place.

## 🌟 Features

* 🤖 AI-powered chatbot using Google Gemini
* 💬 Natural language conversations
* ✨ Beautiful glitter-inspired user interface
* 📝 Task and productivity dashboard
* ⚡ Fast and responsive Streamlit application
* 🔒 Secure API key management using Streamlit Secrets

## 🛠️ Tech Stack

* Python
* Streamlit
* Google Gemini API
* HTML & CSS (custom styling)

## 📂 Project Structure

```text
My-Glitter-Dash/
│── Myglitterdash.py
│── requirements.txt
│── README.md
│── .gitignore
└── .streamlit/
    └── secrets.toml (not committed)
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/SiriMudaddla/My-Glitter-Dash.git
```

### 2. Navigate to the project

```bash
cd My-Glitter-Dash
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create the following file:

```text
.streamlit/secrets.toml
```

Add your Gemini API key:

```toml
API_KEY = "YOUR_GEMINI_API_KEY"
```

> **Note:** Never commit your API key to GitHub.

### 5. Run the application

```bash
streamlit run Myglitterdash.py
```

## 🔐 Security

This project uses **Streamlit Secrets** to securely manage API credentials. Sensitive information is excluded from version control using `.gitignore`.

## 📸 Screenshots

Add screenshots of the application here after deployment.

## 📌 Future Enhancements

* Voice interaction
* User authentication
* Calendar integration
* Notes and reminders
* Mood tracking
* Dark and Light themes
* Deployment on Streamlit Community Cloud

## 👩‍💻 Author

**Siri Mudaddla**

GitHub: https://github.com/SiriMudaddla

---


