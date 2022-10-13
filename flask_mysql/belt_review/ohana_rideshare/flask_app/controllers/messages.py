from email import message
from flask import render_template, redirect, request,session,flash
from flask_app import app
from flask_app.models import ride,user,message

@app.route("/send_message/<int:id>",methods=['POST','GET'])
def send_message(id):
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "content": request.form['content'],
        "ride_id": id,
        "sender_id": request.form['driver_id'],
        "receiver_id": request.form['user_id']
    }
    message.Message.send_message(data)
    return redirect(f"/rides/{id}")