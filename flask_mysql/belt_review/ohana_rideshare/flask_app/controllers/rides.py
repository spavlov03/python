from flask import render_template, redirect, request,session,flash
from flask_app import app
from flask_app.models import ride,user

@app.route("/rides/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/logout")
    data = {"id": session['user_id']}
    all_rides = ride.Ride.get_all_rides()
    all_rides_with_drivers = ride.Ride.get_all_rides_with_drivers()
    #print("ALL RIDES ARE -----",all_rides)
    return render_template('dashboard.html',user = user.User.get_user_by_id(data),all_rides=all_rides,all_rides_with_drivers=all_rides_with_drivers)

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
    #print("DATA IN CONTROLLER IS ----",data)
    ride.Ride.request_ride(data)
    return redirect('/rides/dashboard')
@app.route("/rides/delete/<int:id>")
def delete_ride(id): 
    if "user_id" not in session:
        return redirect("/logout")
    data = {"id":id}
    one_ride = ride.Ride.get_ride_by_id(data)
    #print(one_ride)
    if session['user_id'] == one_ride['user_id']:
        ride.Ride.delete_ride(data)
    return redirect('/rides/dashboard')
@app.route("/rides/<int:id>/add_driver")
def add_driver(id):
    if "user_id" not in session:
        return redirect("/logout")
    driver_data = {
        "id":id,
        "driver_id": session["user_id"]
        }
    ride.Ride.driver_add(driver_data)
    return redirect('/rides/dashboard')
@app.route("/rides/<int:id>/remove_driver")
def remove_driver(id):
    if "user_id" not in session:
        return redirect("/logout")
    ride.Ride.driver_remove(id)
    return redirect('/rides/dashboard')
@app.route("/rides/<int:id>")
def show_ride(id):
    if "user_id" not in session:
        return redirect("/logout")
    data = {"id":id}
    msg_data = {"ride_id":id}
    this_ride = ride.Ride.get_one_ride_with_drivers(data)
    user_in_session = session['user_id']
    return render_template("show_ride.html",this_ride = this_ride,user_in_session=user_in_session)
@app.route("/rides/edit/<int:id>")
def edit_ride(id): 
    if "user_id" not in session:
        return redirect("/logout")
    data = {"id":id}
    one_ride = ride.Ride.get_ride_by_id(data)
    return render_template("edit_ride.html",one_ride = one_ride)
@app.route("/edit_ride/<int:id>",methods=["POST"])
def ride_edit(id):
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "id":id,
        "pick_up_location": request.form['pick_up_location'],
        "details": request.form['details']
    }
    if not ride.Ride.validate_ride(request.form):
        return redirect(f"/rides/edit/{id}")
    ride.Ride.edit_ride_by_id(data)
    return redirect(f"/rides/{id}")

# @app.route("/send_message/<int:id>",methods=['POST','GET'])
# def send_message(id):
#     if "user_id" not in session:
#         return redirect("/logout")
#     data = {
#         "content": request.form['content'],
#         "ride_id": id,
#         "sender_id": request.form['driver_id'],
#         "receiver_id": request.form['user_id']
#     }
#     ride.Ride.send_message(data)
#     return redirect(f"/rides/{id}")