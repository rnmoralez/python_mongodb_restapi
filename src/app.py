from flask import Flask, request 
from flask_pymongo import PyMongo 
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['MONGO_URI']='mongodb+srv://rnmoralez:Arbol1994@practica.8tvn6ho.mongodb.net/pythonmongodb?retryWrites=true&w=majority'
mongo = PyMongo(app)

@app.route('/users')
def find_user():
    id = mongo.db.users.find()
    print(str(id))
    return {True: False}
 

@app.route('/users', methods=['POST'])
def create_user():
    #Receiving data
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']

    if username and email and password:
        hashed_password = generate_password_hash(password)
        id = mongo.db.users.insert_one(
             {'username': username, 'email':email, 'password': hashed_password}
        )
        response = {
            'id': str(id),
            'username': username,
            'password': password,
            'email': email
        }   
        return response 
    
    else:
        {'message': 'received'}

    return {'message': 'received'}



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)


