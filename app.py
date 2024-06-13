from flask import Flask
from flask_cors import CORS
from controllers.data import data_bp
from controllers.user import user_bp
from database.db import init_db

app = Flask(__name__)
init_db(app)
CORS(app)

app.register_blueprint(user_bp, url_prefix='/api/user')
app.register_blueprint(data_bp, url_prefix='/api/jobs')


if __name__ == '__main__':
    app.run(debug=True, port=8800)