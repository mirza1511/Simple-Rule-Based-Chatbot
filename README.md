💬 Smart Chatbot - Rule Based GUI

A simple rule-based chatbot with a modern GUI built using Python Tkinter. The bot responds to 30+ predefined messages with typing animation and chat bubbles like ChatGPT.

✨ Features
- 30+ Predefined Responses: Greetings, jokes, basic Q&A, time/date
- Modern GUI: Dark theme with user/bot chat bubbles 
- Typing Animation: Shows "Bot is typing..." before reply
- Keyword Matching: Handles variations like `?` and `.` in input
- No External Libraries: Uses only built-in Python modules

🖼️ Screenshot
<img width="495" height="626" alt="image" src="https://github.com/user-attachments/assets/da8c060a-e84d-4214-a040-ae72959a302a" />


🚀 How to Run
1. Make sure Python 3.6+ is installed
2. Clone this repository:
   ```bash
   git clone https://github.com/mirza1511/Simple-Rule-Based-Chatbot.git
3. Run the chatbot:
   python chatbot.py


💡 How to Use
1. Type your message in the input box at the bottom
2. Press `Enter` or click `Send`
3. Bot will reply with typing animation

Try these commands:
hi, hello, how are you, what is your name, tell me a joke, time, date, help, bye


📋 Requirements
- Python 3.6 or higher
- Tkinter (comes pre-installed with Python)

No `pip install` needed.

🔧 Code Structure
Function | Purpose
`get_response()` | Matches user input with predefined responses
`display_message()` | Shows chat bubbles for user/bot
`bot_reply_with_typing()` | Adds 1s delay + typing animation
`responses` dict | Contains 30+ key-value pairs for replies


👨‍💻 Author
Mirza1511




