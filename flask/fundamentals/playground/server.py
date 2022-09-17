from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/play')
def play():
    return render_template("play.html")

@app.route('/play/<int:num>')
def play_num(num):
#    return num
    return render_template("play.html", num=num)

@app.route('/<path:path>')
def catch_all(path):
    return 'Sorry! No response. Try again.'

if __name__=="__main__":
    app.run(debug=True, port=8000)
