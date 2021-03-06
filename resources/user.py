import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

# create a new class for user to register into database
class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type = str,
        required = True,
        help = "This field cannot be blank."
    )
    parser.add_argument('password',
        type = str,
        required = True,
        help = "This field cannot be blank."
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        # prevent registering same username twice
        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists."}, 400

        ### use SQLAlchemy
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "INSERT INTO users VALUES (NULL, ?, ?)" # because we use system's id with automatic incremental, keep id as NULL
        # cursor.execute(query, (data['username'], data['password']))
        #
        # connection.commit()
        # connection.close()
        ###

        # user = UserModel(data['username'], data['password'])
        # simplify
        user = UserModel(**data) # because we use a parser, we ensure that data only contains name and password
        user.save_to_db()

        return {"message": "User created successfully."}, 201
