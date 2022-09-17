from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome"

@app.route('/play')
def play():
    return render_template("index.html", num=3,color="#9EC5F8")

@app.route('/play/<int:num>')
def play_2(num):
    return render_template("index.html", num=num,color="#9EC5F8")

@app.route('/play/<int:num>/<string:color>')
def play_3(num,color):
#    return num
    return render_template("index.html", num=num,color=color)

@app.route('/<path:path>')
def catch_all(path):
    return 'Sorry! No response. Try again.'

if __name__=="__main__":
    app.run(debug=True, port=8000)
