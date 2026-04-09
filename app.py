import streamlit as st
import google.generativeai as genai
import os
from gemini_api import get_response
from prompt import build_prompt
from memory import update_history

# --- 1. INITIAL CONFIG ---
st.set_page_config(page_title="Career Chatbot", page_icon="💼", layout="centered")

# Visual Header
st.title("🚀 Career Advisor Chatbot")
st.markdown("---")

# --- 2. SESSION STATE ---
# This keeps your conversation alive when the app reruns
if "history" not in st.session_state:
    st.session_state.history = []

# --- 3. UI COMPONENTS (INPUT AREA) ---
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Ask your career-related question:", placeholder="e.g., How can I improve my Data Science resume?")
    submitted = st.form_submit_button("Send")

# --- 4. LOGIC ENGINE ---
if submitted and user_input:
    with st.spinner("Analyzing and thinking..."):
        try:
            # 1. Build the prompt using logic from prompt.py
            full_prompt = build_prompt(user_input, st.session_state.history)

            # 2. Get the actual AI response from gemini_api.py
            response_text = get_response(full_prompt)
            
            # 3. Update the session state history using memory.py
            # This ensures the new message is saved for the next turn
            st.session_state.history = update_history(
                st.session_state.history, user_input, response_text
            )
            
        except Exception as e:
            st.error(f"An error occurred: {e}")

# --- 5. DISPLAY CHAT HISTORY ---
# Display messages in reverse or chronological order
# Using st.chat_message for a professional look
for chat in st.session_state.history:
    with st.chat_message("user"):
        st.write(chat["user"])
    with st.chat_message("assistant"):
        st.write(chat["bot"])

# Optional: Add a sidebar button to clear history
if st.sidebar.button("Clear Conversation"):
    st.session_state.history = []
    st.rerun()