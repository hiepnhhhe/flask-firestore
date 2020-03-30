from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, jwt_optional, create_access_token, current_user

from .models import User
from ..app import user_ref

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/api/users', methods=['POST'])
def create_user():
    try:
        user_ref.add(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@user_blueprint.route('/api/list')
def read():
    try:
        all_users = [doc.to_dict() for doc in user_ref.stream()]
        return jsonify(all_users), 200
    except Exception as e:
        return f"An error eccured: {e}"


@user_blueprint.route('/api/list:{user_id}', methods=['POST'])
def search():
    try:
        user = user_ref.document(user_id).get()
        return jsonify(user), 200
    except Exception as e:
        return f"An error eccured: {e}"

# import resources

# api.add_resource(resources.UserRegistration, '/register')
# api.add_resource(resources.UserLogin, '/login')
# api.add_resource(resources.UserLogoutAccess, '/logout/access')
# api.add_resource(resources.UserLogoutRefresh, '/token/refresh')
# api.add_resource(resources.TokenRefresh, '/token/refresh')
# api.add_resource(resources.AllUsers, '/users')
# api.add_resource(resources.SecretResource, '/secret')
