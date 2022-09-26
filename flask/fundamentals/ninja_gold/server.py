from flask import Flask , session, redirect , render_template, request
import random
app = Flask(__name__)  
app.secret_key = "Svet is the best"

@app.route('/')         
def index():
    if "gold" not in session: 
        session['gold'] = 0
    if "activity" not in session: 
        session['activity'] = ""
    return render_template('index.html')
@app.route('/process_money',methods=['POST'])
def find_gold(): 
    if request.form['option'] == "farm":
        num = random.randint(10,20)
        session['gold'] += num
        session['activity'] += f"<p class='text-success'>You earned {num} Gold from the Farm!"
    if request.form['option'] == "cave":
        num = random.randint(5,10)
        session['gold'] += num
        session['activity'] += f"<p class='text-success'>You earned {num} Gold from the Cave!"
    if request.form['option'] == "house":
        num = random.randint(2,5)
        session['gold'] += num
        session['activity'] += f"<p class='text-success'>You earned {num} Gold from the House!"
    if request.form['option'] == "casino":
        num = random.randint(-50,50)
        session['gold'] += num
        if num <0: 
            session['activity'] += f"<p class='text-danger'>You lost {num} Gold from the Casino!"
        else:
            session['activity'] += f"<p class='text-success'>You earned {num} Gold from the Casino!"
    return redirect('/')
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True,port=8000)    