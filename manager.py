from flask import Flask, request, jsonify
from db import DB


app = Flask(__name__)
db = DB()


@app.route("/users/")
def get_all_users():
    return jsonify(db.get_all_users())

@app.route('/users/<int:chat_id>',methods = ["GET"])
def get_by_id(chat_id):
    return jsonify(db.get_user_by_id(chat_id))

@app.route('/users/',methods = ["POST"])
def create_user():
    data = request.get_json()
    db.create_user(data['first_name'],data['last_name'],data['username'])
    return jsonify({'message':'new user was created'})

@app.route('/users/<int:chat_id>', methods = ["PUT"])
def update(chat_id):
    data = request.get_json()
    db.update(chat_id,data["first_name"],data["last_name"],data["username"])
    return jsonify({'message':'user was updated'})

@app.route('/users/<int:chat_id>',methods = ["DELETE"])
def delete(chat_id):
    db.delete(chat_id)
    return jsonify({"message":"user was deleted"})

if __name__ == "__main__":
    app.run(debug=True)
