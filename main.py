#!/usr/bin/env python3
from flask import Flask
import chat
chat.setup()
app = Flask(__name__)

@app.route('/chat/<message>')
def index(message):
    return chat.parse(message)
    
if __name__ == "__main__":
    app.run()
