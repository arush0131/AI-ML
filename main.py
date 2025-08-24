from urllib import request
from flask import Flask,render_template,request


app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html> <h1>Welcome to the Flask application!</h1> </html>"

@app.route("/index",methods=["GET"])
def index():
    return render_template("index.html")


@app.route('/form',methods=["GET","POST"])
def form():
    if request.method == 'POST':
       pass
    return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=True) 
