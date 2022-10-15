from datetime import datetime
from flask import render_template, redirect, request,session,flash
from flask_app import app
from flask_app.models import user,message


@app.route('/wall')
def wall():
    data = {"id":session['user_id'],
    "sender_id":session['user_id'],
    "receiver_id":session['user_id']}
    users_messages = message.Message.get_all_messages_for_user(data)
    user_in_session = user.User.get_user_by_id(data)
    messages_by_user = message.Message.get_all_messages_by_user(data)
    today = datetime.today()
    return render_template("wall.html",all_users=user.User.get_all_users(),users_messages=users_messages,user_in_session=user_in_session,messages_by_user=messages_by_user,today=today)

@app.route('/send_message/<int:id>',methods=["POST"])   
def send_message(id): 
    current_user = session['user_id']
    data = {
        "content": request.form['content'],
        "sender_id": current_user, 
        "receiver_id": id
    }
    message.Message.send_message(data)
    return redirect('/wall')
@app.route('/delete/<int:id>')
def delete_message(id):
    data = {"id": id}
    message.Message.message_delete(data)
    return redirect("/wall")