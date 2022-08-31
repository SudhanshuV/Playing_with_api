from flask import Flask,request,jsonify
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://Sudhanshu_cluster:15991799#Mdb@cluster0.qcrsb.mongodb.net/?retryWrites=true&w=majority")
db = client['datadb']
tb = db['datatb']

@app.route('/insertmg',methods=['GET','POST'])
def insertmg():
    if request.method=='POST':
        name=request.json['naam']
        addr=request.json['ptaa']
        sal=request.json['kmai']
        tb.insert_one({"naam":name,"ptaa":addr,"kmai":sal})
        return jsonify(str("inserted"))


@app.route('/delmg',methods=['GET','POST'])
def deletmg():
    if request.method=='POST':
        name=request.json['naam']
        tb.delete_one({"naam":name})
        return jsonify(str("delete done"))

@app.route('/updmg',methods=['GET','POST'])
def updtemg():
    if request.method=='POST':
        name=request.json['naam']
        tb.update_one({"naam":name},{"$set":{"ptaa":"Lucknow Kali pahadi ke neeche"}})
        return jsonify(str("update done"))


@app.route('/upmg',methods=['GET','POST'])
def updtmg():
    if request.method=='POST':
        name=request.json['naam']
        addr = request.json['ptaa']
        tb.update_one({"naam":name},{"$set":{"ptaa":addr}})
        return jsonify(str("update done"))


if __name__=="__main__":
    app.run()