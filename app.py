from flask import Flask
from controllers.data import data_bp
from controllers.user import user_bp
from database.db import init_db

app = Flask(__name__)
init_db(app)

app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(data_bp, url_prefix='/data')


if __name__ == '__main__':
    app.run(debug=True, port=8800)