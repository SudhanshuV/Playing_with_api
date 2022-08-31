from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/just4fun')
def j4f():
    return "This is just 4 fun"

if __name__=="__main__":
    app.run(port=5003)