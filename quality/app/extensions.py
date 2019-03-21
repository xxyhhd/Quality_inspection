from flask_sqlalchemy import SQLAlchemy  # ORM模型，sql语句
from flask_bootstrap import Bootstrap  # 注册蓝本
from flask_migrate import Migrate  # 数据库迁移
from flask_mail import Mail  # 处理邮件
# from flask_login import LoginManager  # 用户登录状态管理模块
from flask_moment import Moment # 处理时间

# 实例化ORM模型
db = SQLAlchemy()
migrate = Migrate(db=db)
moment = Moment()


# 加载app
def ext_int(app):
    db.init_app(app)  # 数据库
    Bootstrap(app)
    migrate.init_app(app=app)
    moment.init_app(app)

