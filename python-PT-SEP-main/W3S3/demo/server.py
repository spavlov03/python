from flask import Flask, render_template

app = Flask(__name__)


# @app.route("/")
# def index():
#     return "Hello World"
@app.route("/")
def index():
    all_students = [
        {"id": 1, "name": "test", "email": "t@t.com", "created_at": "1232q3213", "updated_at": "1232q3213"},
        {"id": 2, "name": "john", "email": "j@t.com", "created_at": "1232q3213", "updated_at": "1232q3213"},
        {"id": 3, "name": "jack", "email": "ja@t.com", "created_at": "1232q3213", "updated_at": "1232q3213"},
        {"id": 4, "name": "jane", "email": "je@t.com", "created_at": "1232q3213", "updated_at": "1232q3213"},
    ]
    return render_template("index.html", name="Jack", students=all_students)


if __name__ == "__main__":
    # FOR MAC USERS :'( we need to add port=8000
    # BY default the server will be at localhost:5000
    app.run(debug=True, port=8000)
