from flask import Flask, request, jsonify
from .extensions import migrate, db, jwt, api, cors
from .user.views import user_blueprint

GOOGLE_APPLICATION_CREDENTIALS = "key.json"

# def register_extensions(app):
#     bcrypt.init_app(app)
#     migrate.init_app(app, db)
#     jwt.init_app(app)
#     api.init_app(app)

# def register_blueprints(app):
#     origins = app.config.get('CORS_ORIGIN_WHITELIST', '*')
#     cors.init_app()

app = Flask(__name__)
app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
