from flask import Flask, request, abort
from skpy import Skype,SkypeChats
sk = Skype('devbrat.pandey@appwrk.com', 'January@2021')
app= Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        channel = sk.chats.chat('19:752974eaf3f0483fa061f440e906318f@thread.skype')
        channel.sendMsg(request.json)
        return 'success', 200
    else:
        abort(400)

