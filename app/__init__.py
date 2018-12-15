# 对整个应用做初始化操作
# 主要工作
# 1.构建 Flask 应用以及各种配置
# 2.构建 SQLAlchemy 的应用

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    # 配置启动模式为调试模式, 和app.run(debug=True)
    app.config['DEBUG'] = True

    # 配置数据库的连接字符串
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123456@localhost:3306/blog"

    # 配置自动提交
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    # 配置SECRET_KEY, SESSION时使用
    app.config['SECRET_KEY'] = 'aixieshaxiesha'

    # 数据库应用实例的初始化
    db.init_app(app)

    # 将 main 蓝图程序关联到app上
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # 将 users 蓝图程序关联到app上
    from .users import users as users_blueprint
    app.register_blueprint(users_blueprint)

    return app






