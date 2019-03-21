import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # 密钥
    SECRET_KEY = '123QWE'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 每页显示数据的条数，分页使用
    PAGE_NUM = 3


# 开发环境的配置
class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'check-dev.sqlite')


# 测试环境的配置
class TestingConfig(Config):
    DEBUG = False
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456789@127.0.0.1:3306/flask_blog_test'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'blog-test.sqlite')


# 生成环境的配置
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456789@127.0.0.1:3306/flask_blog_real'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'blog.sqlite')


# 配置类的别名
config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
