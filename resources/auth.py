from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt_extended import create_access_token
from datetime import timedelta
from passlib.hash import pbkdf2_sha512


class Auth(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('username',
                      type=str,
                      required=True,
                      help='This field cannot be left blank')
  parser.add_argument('password',
                      type=str,
                      required=True,
                      help='This field cannot be left blank')

  def post(self):
    data = Auth.parser.parse_args()
    user = UserModel.find_by_attribute(username=data['username'])
    if user and pbkdf2_sha512.verify(data['password'], user.password):  # verify password
      access_token = create_access_token(identity=user.id, expires_delta=timedelta(minutes=30))
      return {'access_token': access_token}, 200
    return {'message': 'Wrong username or password'}, 401
