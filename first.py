from flask import Flask,request,jsonify
import mysql.connector as conn
import pandas as pd

app = Flask(__name__)   # for creating routing.

mydb = conn.connect(host='localhost',user='root',passwd='query4u')
cur=mydb.cursor()
cur.execute("create database if not exists task21")
cur.execute("create table if not exists task21.tasktb(name varchar(20),desig varchar(20),salary int)")


@app.route('/insert',methods=['GET','POST'])
def insert():
    if request.method=='POST':
        name=request.json['name']
        desig=request.json['desig']
        salary=request.json['salary']
        cur.execute("insert into task21.tasktb values(%s,%s,%s)",(name,desig,salary))
        mydb.commit()
        return jsonify(str('insertion done'))

@app.route('/update',methods=['GET','POST'])
def update():
    if request.method=='POST':
        desig=request.json['desig']
        cur.execute("update task21.tasktb set name= %s where desig= %s",("Tiki",desig))
        mydb.commit()
        return jsonify(str('update done'))

@app.route('/delete',methods=['GET','POST'])
def delete():
    if request.method=='POST':
        name=request.json['name']
        cur.execute("delete from task21.tasktb where name=%s",(name,))
        mydb.commit()
        return jsonify(str('delete done'))

@app.route('/select',methods=['POST','GET'])
def select_all():
    if request.method=='POST':
        l=[]
        cur.execute("select * from task21.tasktb")
        for i in cur.fetchall():
            l.append(i)
    return jsonify(str(l))

@app.route('/file',methods=['GET','POST'])
def filo():
    if request.method=='POST':
        name=request.json['name']
        f=pd.read_csv(name)
        return jsonify(str(f))


if __name__=='__main__':
    app.run()