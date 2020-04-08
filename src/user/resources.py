from flask_restful import Resource, reqparse
from .models import User, RevokedTokenModel

parser = reqparse.RequestParser()
parser.add_argument(
    'username', help='This field cannot be blank', required=True)
parser.add_argument(
    'password', help='This field cannot be blank', required=True)

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return RevokedTokenModel.is

class UserRegistration():
    def post(self):
        data = parser.parse_args()

    if User.find_by_username(data['username']):
            return {'message': 'User {} already exists'.format(data['username'])}

        new_user = User(
            username=data['username'],
            password=Account.generate_hash(data['password'])
        )
        try:    
            new_user.save_to_db()
            access_token = create_access_token(identity=data['usename'])
            refresh_token = create_refresh_token(identity=data['username'])
            return {
                'message': 'User {} was created'.format(data['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        except Exception as e:
            return f"Error occured: {e}", 500

class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = User.find_by_username(data['username'])
        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}

        if data['password'] == current_user.password:
            access_token = create_access_token(identity=data['username'])
            refresh_token = create_refresh_token(identity=data['username'])
            user = {
                "username": current_user.username,
                "name": current_user.name,
                "token": access_token,
                "refresh_token": refresh_token
            }
            return jsonify(user)
        else:
            return f"Error occured: {e}", 500

class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500

class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500

class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {'access_token': access_token}

class AllUsers(Resource):
    def get(self):
        return Account.return_all()

    def delete(self):
        return Account.delete_all()

class SecretResource(Resource):
    @jwt_required
    def get(self):
        return {
            'answer': 42
        }