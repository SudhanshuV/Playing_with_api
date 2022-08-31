from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/just45fun')
def j45f():
    qtpi=request.args.get("stud")
    return "This is just 45 fun {}".format(qtpi)

if __name__=="__main__":
    app.run(port=5003)