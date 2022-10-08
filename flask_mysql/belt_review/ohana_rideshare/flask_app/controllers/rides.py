from flask import render_template, redirect, request,session,flash
from flask_app import app
from flask_app.models import ride,user

@app.route("/rides/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/logout")
    data = {"id": session['user_id']}
    all_rides = ride.Ride.get_all_rides()
    print("ALL RIDES ARE -----",all_rides)
    return render_template('dashboard.html',user = user.User.get_user_by_id(data),all_rides=all_rides)

@app.route("/rides/new")
def add_ride():
    if "user_id" not in session:
        return redirect("/logout")
    return render_template("request_ride.html")
@app.route("/new_ride",methods=['POST'])
def new_ride():
    if "user_id" not in session:
        return redirect("/logout")
    if not ride.Ride.validate_ride(request.form):
        return redirect("/rides/new")
    data = {
        "destination": request.form['destination'],
        "pick_up_location": request.form['pick_up_location'],
        "rideshare_date": request.form['rideshare_date'],
        "details": request.form['details'],
        "user_id": session['user_id']
    }
    print("DATA IN CONTROLLER IS ----",data)
    ride.Ride.request_ride(data)
    return redirect('/rides/dashboard')