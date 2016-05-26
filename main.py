# coding=utf-8
from utils.conf import INNER_IP, port
from handlers import app


if __name__ == '__main__':
    app.run(debug=True, host=INNER_IP, port=port)