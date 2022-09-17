from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 配置数据库的连接参数
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/test_flask'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'weibo_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    birth_date = db.Column(db.Date, nullable=True)
    age = db.Column(db.Integer, default=0)


class UserAddress(db.Model):
    """ 用户的地址 """
    __tablename__ = 'weibo_user_addr'
    id = db.Column(db.Integer, primary_key=True)
    addr = db.Column(db.String(256), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('weibo_user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('address', lazy=True))


@app.route('/')
def mine():
    """  首页 """
    return render_template('index.html')


@app.route('/user/<int:page>/')
def list_user(page):
    """ 用户分页 """
    per_page = 10  # 每一页的数据大小
    # 1. 查询用户信息
    user_ls = User.query
    # 2. 准备分页的数据
    user_page_data = user_ls.paginate(page, per_page=per_page)
    return render_template('list_user.html', user_page_data=user_page_data)
