
import requests
import re
from typing import Optional

# ==============================
# Gemini API Configuration
# ==============================

API_KEY = "AIzaSyDMv2AoHLuFkXN4FwvKTgffG3YxCozABq8"

API_URL = (
    f"https://generativelanguage.googleapis.com/v1beta/models/"
    f"gemini-2.5-flash:generateContent?key={API_KEY}"
)

# ==============================
# Personal Information Detection
# ==============================

PERSONAL_INFO_PATTERNS = [
    r"\b\d{10}\b",  # Phone Number
    r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",  # Email
    r"\b\d{12}\b",  # Aadhaar-like Number
    r"\b\d{16}\b"   # Card-like Number
]


def contains_personal_info(text: str) -> bool:
    """
    Check if the user input contains sensitive information.
    """

    for pattern in PERSONAL_INFO_PATTERNS:
        if re.search(pattern, text):
            return True

    return False


# ==============================
# Gemini API Request Function
# ==============================

def get_gemini_response(user_input: str) -> str:
    """
    Send user input to Gemini API and return response.
    """

    # Safety Check
    if contains_personal_info(user_input):
        return (
            "⚠️ Please avoid sharing personal information like:\n"
            "- Phone Numbers\n"
            "- Emails\n"
            "- Aadhaar Numbers\n"
            "- Card Details"
        )

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": user_input
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=30
        )

        # Raise error for bad status codes
        response.raise_for_status()

        response_data = response.json()

        # Extract Gemini response safely
        candidates = response_data.get("candidates")

        if not candidates:
            return "⚠️ No response received from Gemini API."

        return candidates[0]["content"]["parts"][0]["text"]

    except requests.exceptions.Timeout:
        return "⚠️ Request timed out. Please try again."

    except requests.exceptions.ConnectionError:
        return "⚠️ Internet connection error."

    except requests.exceptions.HTTPError as err:
        return f"⚠️ HTTP Error: {err}"

    except Exception as e:
        return f"⚠️ Unexpected Error: {e}"


# ==============================
# Main Chat Application
# ==============================

def main():
    """
    Run chatbot in terminal.
    """

    print("=" * 50)
    print("🤖 Gemini AI Chatbot")
    print("Type 'exit' to close the chatbot")
    print("=" * 50)

    while True:

        user_input = input("\nYou: ").strip()

        if not user_input:
            print("⚠️ Please enter a message.")
            continue

        if user_input.lower() in ["exit", "quit"]:
            print("\n👋 Goodbye!")
            break

        response = get_gemini_response(user_input)

        print(f"\nGemini: {response}")


# ==============================
# Program Entry Point
# ==============================

if __name__ == "__main__":
    main()
