from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/success')
def success():
    return "Success"
@app.route('/hello/<string:banana>/<int:num>')
def hello(banana,num):
    return render_template("hello.html", banana=banana, num=num)
@app.route('/<path:path>')
def catch_all(path):
    return 'Sorry! No response. Try again.'
if __name__=="__main__":
    app.run(debug=True, port=8000)
