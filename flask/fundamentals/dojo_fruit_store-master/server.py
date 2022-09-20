from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    total_fruits = int(request.form['strawberry'])+int(request.form['raspberry'])+int(request.form['apple'])+int(request.form['blackberry'])
    print(f"Charging {request.form['first_name']} {request.form['last_name']} for {total_fruits} fruits.")
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True,port=8000)    