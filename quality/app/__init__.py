from flask import Flask
# 导入当前网站的配置类
from app.config import config
# 加载所有的第三方扩展库
from app.extensions import ext_int
# 导入注册的蓝本函数
from app.views import register_blueprint


# 项目初始化方法
def create_app(ConfigName):
    app = Flask(__name__)
    # 加载网站配置，config.py文件
    app.config.from_object(config[ConfigName])
    # 加载所有第三方扩展库
    ext_int(app)
    # 注册蓝本
    register_blueprint(app)
    # 初始化加载自定义过滤器

    return app
