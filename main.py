# coding=utf-8
from conf import INNER_IP, port, FLASK_MONGO_ENGINE_CONF
from flask import Flask
from handlers import user, other, api
from utils.models import engine


app = Flask(__name__)
app.config.update(FLASK_MONGO_ENGINE_CONF)
engine.init_app(app)
app.use_api = True


if __name__ == '__main__':
    app.register_blueprint(api)
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(other, url_prefix='/other')
    app.run(debug=True, host=INNER_IP, port=port)