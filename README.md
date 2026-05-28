# Gemini AI Chatbot 🤖

A simple AI chatbot built using Python and the Gemini API.
This chatbot can generate real-time responses directly in the terminal and also includes basic personal information detection for user safety and privacy.

---

# Features

* Real-time AI responses using Gemini API
* Detects personal information before sending requests
* Blocks sensitive data like:

  * Phone numbers
  * Email addresses
  * Aadhaar numbers
  * Card numbers
* Error handling for API and internet issues
* Simple terminal-based interface
* Beginner-friendly Python project

---

# Technologies Used

* Python
* Gemini API
* Requests Library
* Regular Expressions (Regex)

---

# Project Structure

```bash id="zlnw5o"
gemini-chatbot/
│
├── chatbot.py
├── README.md
└── requirements.txt
```

---

# Installation

Clone the repository:

```bash id="y8d9e6"
git clone https://github.com/your-username/gemini-chatbot.git
```

Move into the project folder:

```bash id="jg8go4"
cd gemini-chatbot
```

Install dependencies:

```bash id="m5i1b6"
pip install requests
```

---

# API Setup

Open the Python file and replace:

```python id="vvf2ic"
API_KEY = "YOUR_GEMINI_API_KEY"
```

with your actual Gemini API key.

---

# Run the Project

```bash id="l3jvc6"
python chatbot.py
```

---

# Example Output

```text id="4f8tbg"
==================================================
🤖 Gemini AI Chatbot
Type 'exit' to close the chatbot
==================================================

You: Hello
Gemini: Hi! How can I help you today?
```

---

# Personal Information Detection

The chatbot checks user input before sending it to the API.
If sensitive information is detected, the chatbot blocks the message and shows a warning.

Example:

```text id="pv76qx"
⚠️ Please avoid sharing personal information.
```

---

# Error Handling

The project can handle:

* Internet connection errors
* Timeout issues
* Invalid API responses
* Unexpected exceptions

---

# Future Improvements

* GUI using Tkinter
* Streamlit Web App
* Chat history support
* Voice assistant features
* Database integration
* Dark mode UI

---

# Learning Outcomes

This project helped in learning:

* API Integration
* Python Functions
* Regex Validation
* Exception Handling
* User Input Processing
* AI Application Development

---

# Author

Developed by Hritik Khokhar

---

# License

This project is open-source and free to use for learning purposes.
