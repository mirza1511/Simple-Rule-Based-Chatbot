import tkinter as tk
from tkinter import scrolledtext
import datetime

# ================= RESPONSES (30+) =================
responses = {
    "hi": "Hello! 😊",
    "hello": "Hi there!",
    "hey": "Hey! What's up?",
    "good morning": "Good morning! ☀️",
    "good evening": "Good evening!",
    "good night": "Good night 🌙",

    "how are you": "I'm doing great 😊",
    "what is your name": "I'm your chatbot assistant.",
    "who made you": "I was created as a project.",
    "how old are you": "I don't have an age 😄",

    "help": "You can ask me questions, jokes, or general chat!",
    "what can you do": "I can chat and answer basic questions.",

    "what is python": "Python is a powerful programming language.",
    "what is ai": "AI means Artificial Intelligence.",
    "what is machine learning": "Machine learning is when systems learn from data.",
    "what is chatbot": "A chatbot is a program that talks with users.",

    "tell me a joke": "Why don’t programmers like nature? Too many bugs 😂",
    "another joke": "Why did the computer get cold? It forgot to close windows 😄",

    "i am happy": "That's great to hear! 😊",
    "i am sad": "I'm here for you ❤️",
    "i am bored": "Try coding something fun or watch a movie 🎬",
    "do you like me": "Of course! You're awesome 😄",

    "time": datetime.datetime.now().strftime("Current time: %H:%M:%S"),
    "date": str(datetime.date.today()),

    "weather": "I can't check live weather yet 🌦️",
    "where are you": "I live inside your computer 💻",
    "are you real": "I'm virtual but I exist 😉",
    "thanks": "You're welcome!",
    "thank you": "Anytime! 😊",

    "bye": "Goodbye! 👋",
    "default": "Sorry, I didn't understand that."
}

def get_response(user_input):
    user_input = user_input.lower().strip()
    user_input = user_input.replace("?", "").replace(".", "")

    for key in responses:
        if key in user_input:
            return responses[key]

    if "joke" in user_input:
        return responses["tell me a joke"]
    elif "name" in user_input:
        return responses["what is your name"]
    elif "help" in user_input:
        return responses["help"]

    return responses["default"]

# ================= GUI =================

root = tk.Tk()
root.title("💬 Smart Chatbot")
root.geometry("500x600")
root.configure(bg="#343541")

# Chat Area
chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Segoe UI", 11),
    bg="#343541",
    fg="white",
    bd=0,
    padx=10,
    pady=10
)
chat_area.pack(fill=tk.BOTH, expand=True)
chat_area.config(state=tk.DISABLED)

# Tags (bubble style)
chat_area.tag_config("user", background="#10a37f", foreground="white",
                     justify="right", lmargin1=100, lmargin2=100, rmargin=10, spacing3=8)

chat_area.tag_config("bot", background="#444654", foreground="white",
                     justify="left", lmargin1=10, lmargin2=10, rmargin=100, spacing3=8)

chat_area.tag_config("typing", foreground="gray")

# Display message
def display_message(msg, sender):
    chat_area.config(state=tk.NORMAL)

    if sender == "user":
        chat_area.insert(tk.END, msg + "\n", "user")
    else:
        chat_area.insert(tk.END, msg + "\n", "bot")

    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)

# Typing animation
def bot_reply_with_typing(user_msg):
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "Bot is typing...\n", "typing")
    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)

    # delay then replace typing text
    root.after(1000, lambda: show_bot_reply(user_msg))

def show_bot_reply(user_msg):
    chat_area.config(state=tk.NORMAL)

    # remove "typing..."
    chat_area.delete("end-2l", "end-1l")

    reply = get_response(user_msg)
    chat_area.insert(tk.END, reply + "\n", "bot")

    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)

# Send message
def send_message(event=None):
    user_msg = entry_box.get().strip()
    if user_msg == "":
        return

    display_message(user_msg, "user")
    entry_box.delete(0, tk.END)

    bot_reply_with_typing(user_msg)

# Input Area
input_frame = tk.Frame(root, bg="#40414f")
input_frame.pack(fill=tk.X)

entry_box = tk.Entry(
    input_frame,
    font=("Segoe UI", 12),
    bg="#40414f",
    fg="white",
    insertbackground="white",
    bd=0
)
entry_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)
entry_box.bind("<Return>", send_message)

send_btn = tk.Button(
    input_frame,
    text="Send",
    command=send_message,
    bg="#10a37f",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    bd=0,
    padx=15
)
send_btn.pack(side=tk.RIGHT, padx=10)

root.mainloop()     