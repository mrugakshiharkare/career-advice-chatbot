def update_history(history, user_input, response):
    # Append the latest exchange to the history list
    history.append({
        "user": user_input,
        "bot": response
    })
    return history