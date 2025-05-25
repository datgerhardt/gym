from flask import Flask, render_template, Response
import time 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def chat_events():
    # Implement your chat logic here
    # For example, you can have a list of messages and yield them one by one.
    messages = ["Hello", "How are you?", "I'm fine, thanks!"]
    for message in messages:
        for m in message:
            yield f"data: {m}\n\n"
        # time.sleep(1)

@app.route('/stream_chat')
def stream_chat():
    return Response(chat_events(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(port=5005,debug=True)

