from flask import Flask,request,jsonify
from flask_cors import CORS
import requests
app = Flask(__name__)
CORS(app)

@app.route("/api/followers")
def get_followers():
  args = request.args
  username = args.get("username")
  res = requests.get(f"https://api.github.com/users/{username}/followers")
  print(res.json())
  return res.json()


if __name__ == "__main__":
  app.run(debug=True,port=8000)