import random
from  flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hallo():
    return "<a href='/b1'> <a href='/b2'> <img src='https://picsum.photos/200'>"
    
    

    
@app.route('/b1')
def b1():
    return "<h1>texti </h1>", render_template("b1.html")

@app.route("/b2/<user>")
def b2(user):
    notandi = user
    return render_template("b2.html", user=notandi) 

if __name__ == "__main__":
    app.run(debug=True)