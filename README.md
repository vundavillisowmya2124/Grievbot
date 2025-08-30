𝐆𝐫𝐢𝐞𝐯𝐁𝐨𝐭 🤖

GrievBot is a web-based chatbot that provides instant answers to user queries using Wikipedia summaries. 
It’s designed to handle common questions, explanations, and general information in a friendly chat interface.
The main goal is to provide a simple, interactive chatbot interface that can run locally without complicated AI setups or API keys.

𝐓𝐞𝐜𝐡𝐧𝐨𝐥𝐨𝐠𝐢𝐞𝐬 𝐔𝐬𝐞𝐝 🛠️

- 𝐏𝐲𝐭𝐡𝐨𝐧 – Backend programming language  
- 𝐅𝐥𝐚𝐬𝐤 – Web framework for serving the chatbot and handling requests  
- 𝐖𝐢𝐤𝐢𝐩𝐞𝐝𝐢𝐚 𝐏𝐲𝐭𝐡𝐨𝐧 𝐋𝐢𝐛𝐫𝐚𝐫𝐲 – Fetches concise summaries from Wikipedia  
- 𝐇𝐓𝐌𝐋 / 𝐂𝐒𝐒 / 𝐉𝐚𝐯𝐚𝐒𝐜𝐫𝐢𝐩𝐭 – Frontend interface with a chatbox  
- 𝐉𝐒𝐎𝐍 – Communication between frontend and backend (AJAX requests)

𝐇𝐨𝐰 𝐈𝐭 𝐖𝐨𝐫𝐤𝐬 ⚙️

1. 𝐔𝐬𝐞𝐫 𝐈𝐧𝐭𝐞𝐫𝐚𝐜𝐭𝐢𝐨𝐧 – Users type questions in the chat interface  
2. 𝐅𝐫𝐨𝐧𝐭𝐞𝐧𝐝 𝐇𝐚𝐧𝐝𝐥𝐢𝐧𝐠  – JavaScript captures user input and sends it to the Flask backend via a POST request  
3. 𝐁𝐚𝐜𝐤𝐞𝐧𝐝 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠  – Flask searches Wikipedia for a short summary of the question:  
   - Returns summary if the page exists   
   - Suggests possible topics if the query is ambiguous   
   - Returns a polite message if no relevant page is found  
4. 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 𝐃𝐢𝐬𝐩𝐥𝐚𝐲  – The bot’s response is sent back to the frontend and displayed in the chatbox  
5. 𝐂𝐨𝐧𝐭𝐢𝐧𝐮𝐨𝐮𝐬 𝐂𝐡𝐚𝐭  – Users can keep asking questions, and the bot responds instantly
  
𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐒𝐭𝐫𝐮𝐜𝐭𝐮𝐫𝐞 📂

GrievBot/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # Frontend HTML file
└── static/
    ├── style.css          # Chat interface styling
    └── script.js          # Frontend JS for sending/receiving messages

𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐚𝐭𝐢𝐨𝐧 & 𝐒𝐞𝐭𝐮𝐩 🚀

1. 𝐂𝐥𝐨𝐧𝐞 𝐭𝐡𝐞 𝐫𝐞𝐩𝐨𝐬𝐢𝐭𝐨𝐫𝐲:
   git clone https://github.com/vundavillisowmya2124/Grievbot.git
   cd Grievbot
2. 𝐈𝐧𝐬𝐭𝐚𝐥𝐥 𝐝𝐞𝐩𝐞𝐧𝐝𝐞𝐧𝐜𝐢𝐞𝐬:
   pip install -r requirements.txt
3. 𝐑𝐮𝐧 𝐭𝐡𝐞 𝐅𝐥𝐚𝐬𝐤 𝐚𝐩𝐩:
   python app.py
4. 𝐎𝐩𝐞𝐧 𝐢𝐧 𝐲𝐨𝐮𝐫 𝐛𝐫𝐨𝐰𝐬𝐞𝐫 🌐: [Open GrievBot in your browser](http://127.0.0.1:5000/)
5. 𝐒𝐭𝐚𝐫𝐭 𝐚𝐬𝐤𝐢𝐧𝐠 𝐪𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 💬 – the bot will respond instantly with Wikipedia summaries 📚

𝐓𝐫𝐲 𝐓𝐡𝐞𝐬𝐞 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 💬

1. How to reset password? 
2. Explain evaporation
3. What is Python?
4. Who is Albert Einstein?
5. Define gravity 
6. History of the Internet

 𝐋𝐢𝐜𝐞𝐧𝐬𝐞 📄

 This project is MIT licensed – feel free to use, modify, and share

 GrievBot transforms your curiosity into instant knowledge! From answering everyday questions to explaining complex concepts, it combines Python, Flask, and Wikipedia to make learning interactive and effortless. Step in, ask away, and let GrievBot be your smart companion! 🌟💬
 


