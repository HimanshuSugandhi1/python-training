import mongo
from flask import *
from pymongo import MongoClient
from flask_pymongo import pymongo
from bson.json_util import dumps
myclient =MongoClient("mongodb://localhost:27017/")
mydb = myclient["Students"]
mycol = mydb["Studentdata"]
app=Flask(__name__)
userdata=[{}]

@app.route('/',methods=['POST'])
def add_user():
    req=request.get_json()
    mycol.insert_one(req)
    return make_response(jsonify({"msg": "user created"}), 200)

@app.route('/display')
def displaydata():
   user=mycol.find()
   resp=dumps(user)
   return resp
@app.route('/display/<name>')
def displayuser(name):
    user=mycol.find_one({'name':name})
    resp=dumps(user)
    return resp
@app.route('/delete/<name>', methods=['DELETE'])
def deleteuser(name):
    user=mycol.delete_one({'name':name})
    resp=jsonify("user deleted susscessfully")
    resp.status_code=200
    return resp
@app.route('/update/<name>', methods=['PUT'])
def updateuser(name):

    req = request.get_json()
    resp=mycol.update_one({"name":name},{'$set':req})
    resp=jsonify("user updated")
    resp.status_code=200
    return resp


if __name__=='__main__':
        app.run(debug=True)