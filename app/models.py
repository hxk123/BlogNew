# 声明所有的实体类
# 导入db, 以遍在实体类中使用
from . import db


# 博客类型表
class BlogType(db.Model):
    __tablename__ = 'blogtype'
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(20), nullable=False)
    # 定义与 Topic 关联关系和反向引用
    topics = db.relationship('Topic', backref='blogtype', lazy='dynamic')


# 分类表
class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    cate_name = db.Column(db.String(50), nullable=False)
    # 定义与 Topic 关联关系和反向引用
    topics = db.relationship('Topic', backref='category', lazy='dynamic')


# 用户表
class User(db.Model):
    __tablename__ = 'user'
    ID = db.Column(db.Integer, primary_key=True)
    loginname = db.Column(db.String(50), nullable=False)
    uname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    # 个人主站地址
    url = db.Column(db.String(200))
    upwd = db.Column(db.String(30), nullable=False)
    is_author = db.Column(db.Boolean, default=False)
    # 建立 与 Reply 之间的 关联属性和反向引用关系
    replies = db.relationship("Reply", backref='user', lazy='dynamic')
    # 建立 User 与 Topic 之间的 关联属性和反向引用关系
    topics = db.relationship('Topic', backref='user', lazy='dynamic')

    # 增加多(User)对多(Topic)的关联属性和反向引用关系
    voke_topics = db.relationship(
        "Topic",
        secondary='voke',
        lazy='dynamic',
        backref=db.backref("voke_users", lazy='dynamic')
    )


# 文章表
class Topic(db.Model):
    __tablename__ = 'topic'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False)
    read_num = db.Column(db.Integer, default=0)
    content = db.Column(db.Text, nullable=False)
    images = db.Column(db.Text)
    # 一(BlogType)对多(Topic)的关系
    blogtype_id = db.Column(db.Integer, db.ForeignKey('blogtype.id'))
    # 一(Category)对多(Topic)的关系
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    # 一(Users)对多(Topic)的关系
    user_id = db.Column(db.Integer, db.ForeignKey('user.ID'))
    # 建立 与 Reply 之间的 关联属性和反向引用关系
    replies = db.relationship("Reply", backref='topic', lazy='dynamic')


# 评论表
class Reply(db.Model):
    __tablename__ = 'reply'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    reply_time = db.Column(db.DateTime)
    # 一(Users)对多(Reply)的关系
    user_id = db.Column(db.Integer, db.ForeignKey('user.ID'))
    # 一(Topic)对多(Reply)的关系
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))


# 喜欢的人数表
class Voke(db.Model):
    __tablename__ = 'voke'
    id = db.Column(db.Integer, primary_key=True)
    # 一(Users)对多(Voke)的关系
    user_id = db.Column(db.Integer, db.ForeignKey('user.ID'))
    # 一(Topic)对多(Voke)的关系
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))





