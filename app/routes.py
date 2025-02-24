from flask import Flask, request, jsonify
from app.database import get_db
from passlib.hash import pbkdf2_sha256
app = Flask(__name__)  


@app.route('/users', methods=['GET'])
def get_all_users():
    db = get_db()
    users = list(db.users.find({}, {'_id': 0}))  
    return jsonify(users), 200


@app.route('/users', methods=['POST'])
def create_user():
    db = get_db()
    data = request.get_json()  
    user_id = str(db.users.count_documents({}) + 1)  
    data['id'] = user_id
    db.users.insert_one(data)  
    return jsonify({'id': user_id, 'message': 'User created'}), 201


@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    db = get_db()
    user = db.users.find_one({'id': id}, {'_id': 0})
    if user:
        return jsonify(user), 200
    return jsonify({'message': 'User not found'}), 404

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    db = get_db()
    data = request.get_json()
    result = db.users.update_one({'id': id}, {'$set': data})
    if result.matched_count > 0:
        return jsonify({'message': 'User updated'}), 200
    return jsonify({'message': 'User not found'}), 404


@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    db = get_db()
    result = db.users.delete_one({'id': id})
    if result.deleted_count > 0:
        return jsonify({'message': 'User deleted'}), 200
    return jsonify({'message': 'User not found'}), 404
def create_user():
    try:
        db = get_db()
        data = request.get_json()
        user_id = str(db.users.count_documents({}) + 1)
        data['id'] = user_id
        db.users.insert_one(data)
        return jsonify({'id': user_id, 'message': 'User created'}), 201
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500