from flask import Flask, request, abort
from skpy import Skype,SkypeChats
app= Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    sk = Skype('rajesh.panwar@appwrk.com', 'appwrk@grow123')
    if request.method == 'POST':
        print(request.json)
        channel = sk.chats.chat('19:752974eaf3f0483fa061f440e906318f@thread.skype')
        channel.sendMsg(request.json)
        return 'success', 200
    else:
        abort(400)

@app.route("/")
def home_view():
        return "<h1>Welcome to Geeks for Geeks</h1>"
