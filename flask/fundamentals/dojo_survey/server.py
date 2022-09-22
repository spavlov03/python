from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = "Svet is the best"
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/process', methods=['POST'])
def submit_user():
    print("Got Post Info")
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['favlang'] = request.form['favlang']
    session['comment'] = request.form['comment']
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return redirect('/result')
@app.route('/result')
def go_back():
    
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return render_template("result.html",name=session['name'],location=session['location'],favlang=session['favlang'],comment=session['comment'])
if __name__ == "__main__":
    app.run(debug=True,port=8000)

