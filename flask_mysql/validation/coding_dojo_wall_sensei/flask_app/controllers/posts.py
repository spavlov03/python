from flask_app import app
from flask import render_template, redirect, request,session
from flask_app.models import post

@app.route('/wall_post',methods=["POST"])
def wall_post():
    data = {
        "content": request.form['content'],
        'user_id': session['user_id']
    }
    post.Post.save(data)
    return redirect('/wall')
@app.route('/posts/delete/<id>')
def delete_post(id):
    data = {"id":id}
    post.Post.post_delete(data)
    return redirect('/wall')