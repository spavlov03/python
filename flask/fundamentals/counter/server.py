from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "Svet is the best!"

@app.route('/')         
def count():
    if 'count' in session:
        session['count'] = session.get('count') + 1
    else: 
        session['count'] = 1
    return render_template('index.html', count=session['count'])

@app.route('/2')         
def count2():
    if 'count' in session:
        session['count'] = session.get('count') + 2
    return render_template('index.html', count=session['count'])

@app.route('/destroy_session')         
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True,port=8000)    