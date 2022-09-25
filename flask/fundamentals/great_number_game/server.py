from flask import Flask, render_template, session, request, redirect 
import random 
app = Flask(__name__)  
app.secret_key = "Svet is the best!"

@app.route('/')         
def index():
    if 'number' not in session:
        session['number'] = random.randint(1,100)
    print(session['number'])
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess_num():
    session['guess'] = int(request.form['guess_num'])
    print(session['guess'])
    return redirect ('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True,port=8000)    