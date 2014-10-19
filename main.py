#!/usr/bin/env python3
from flask import Flask
import chat

app = Flask(__name__)
app.debug = True
chat.setup()

@app.route('/chat/<message>')
def msg(message):
    return str(chat.parse(message))

@app.route('/')
def index():
    body = """
    <html>
      <head>
        <script src="//code.jquery.com/jquery-1.11.0.min.js"></script>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
        <script type="text/javascript">
          $(function(){
            $("#btn").click(function(){
              document.location = '/chat/' + $("#message")[0].value;
            });
          });
        </script>
      </head>
      <body>
          <input type="text" id="message" value="the swift brown fox jumps over the lazy dog" size="250"/>  
          <input type="submit" id="btn" value="Compile?!?!?" onClick="document.location='/chat/' + document.getElementById('message').value;"/>
      </body>
    </html>"""
    return body

if __name__ == "__main__":
    app.run()
