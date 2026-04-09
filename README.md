# AI Career Advisor Chatbot

A specialized conversational AI application designed to provide technical career guidance and interview preparation. The system leverages large language models to offer structured, actionable advice for professional development.

## 🚀 Features

* **Contextual Memory:** Utilizes a custom memory management system to maintain conversation history for coherent, multi-turn dialogues.
* **Dynamic Prompting:** Implements a structured prompting architecture to ensure responses remain professional, concise, and focused on industry standards.
* **Streamlit Interface:** A clean, responsive web-based UI for seamless user interaction.
* **Secure Configuration:** Uses environment variable management to handle sensitive API credentials.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Frontend:** [Streamlit](https://streamlit.io/)
* **LLM API:** Google Generative AI (Gemini 3 Flash)
* **Environment Management:** `python-dotenv`

## 📂 Project Structure

* `app.py`: The main entry point for the Streamlit web application.
* `gemini_api.py`: Logic for API configuration, model initialization, and response handling.
* `prompt.py`: Houses the system instructions and persona definitions for the AI.
* `memory.py`: Manages the session state and conversation history.
* `.env`: (Hidden) Stores the Google API Key.
* `.gitignore`: Prevents sensitive files and caches from being uploaded.

## 🔧 Installation & Setup

1. **Clone the repository:**
   git clone [https://github.com/mrugakshiharkare/career-advice-chatbot.git](https://github.com/mrugakshiharkare/career-advice-chatbot.git)
   cd career-advice-chatbot
2. **Install dependencies:**
pip install -r requirements.txt  
3. **Set up Environment Variables:**    
Create a .env file in the root directory and add your API key:
GOOGLE_API_KEY=your_actual_api_key_here
4. **Run the application:**  
streamlit run app.py
