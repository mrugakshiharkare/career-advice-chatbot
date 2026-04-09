def build_prompt(user_input, history):
    # Start with a system persona
    system_context = "You are a professional Career Advisor. Give concise, encouraging, and actionable advice."
    
    # Optional: Format the history so the AI remembers previous context
    history_context = ""
    for chat in history:
        history_context += f"User: {chat['user']}\nBot: {chat['bot']}\n"
    
    # Combine everything
    full_prompt = f"{system_context}\n\nChat History:\n{history_context}\nNew Question: {user_input}"
    return full_prompt