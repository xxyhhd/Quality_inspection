from .main import main  # 导入首页的蓝本文件
from .engineer import eng
from .ticket import ticket
# 蓝本对象的列表
default_blueprint = [
    (main, ''),
    (eng, ''),
    (ticket, ''),
]


def register_blueprint(app):
    for blueprint, prefix in default_blueprint:
        app.register_blueprint(blueprint, url_prefix=prefix)

