from flask_app import app
from flask import render_template, redirect, request,session
from flask_app.models import user

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/register",methods=["POST"])
def register(): 
    if not user.User.validate_user(request.form):
        return redirect("/")
    print("REQUEST FROM EMAIL IS --------",request.form['email'])
    data = {"email": request.form['email']}
    users_emails = user.User.check_user_email(data)
    print("users emails ------",users_emails)
    if request.form['email'] == users_emails['email']: 
        print("EMAIL ALREADY EXISTS!!!!!")
        return redirect('/')
    print("making new user------")
    user_id = user.User.register(request.form)
    session['user_id'] = user_id
    return redirect("/dashboard")
@app.route("/dashboard")
def dashboard():
    user_id = session['user_id']
    data = {"id": user_id}
    user_info = user.User.get_user_info(data)
    #print("USER ID IS ", user_id)
    #print("USER IS ", user_info)
    return render_template('dashboard.html',user_id = user_id, user_info=user_info)
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
@app.route('/login',methods=["POST"])
def login():
    data = {"email": request.form['email']}
    users_emails = user.User.check_user_email(data)
    print("USERS EMAILS ARE",users_emails)
    if not request.form['email'] == users_emails['email']:
        print('its ok')
    else:
        print("Request Form is ----",request.form)
        user_id = user.User.get_user_info_by_email(request.form)
        #print("USER ID-----",user_id['id'])
        session['user_id'] = user_id['id']
        #print("Session ID is ---- ",session['user_id'])
        return redirect('/dashboard')
    return print("TEST")
