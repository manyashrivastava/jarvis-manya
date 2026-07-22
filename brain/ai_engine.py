def get_ai_response(command):

    responses = {
        "hello": "Hello! I am Jarvis. How can I help you?",
        "hi": "Hello! How can I help you?",
        "who are you": "I am Jarvis, your personal AI assistant.",
        "how are you": "I am functioning perfectly."
    }

    for question, answer in responses.items():
        if question in command:
            return answer

    return "I am still learning. You can give me commands like open YouTube, open Notepad, or tell me the time."