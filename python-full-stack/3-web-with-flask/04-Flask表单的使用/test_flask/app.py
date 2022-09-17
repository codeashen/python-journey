import os

from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

from forms import LoginForm, RegisterForm, UserAvatarForm

app = Flask(__name__)
# 配置数据库的连接参数
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/test_flask'
app.config['WTF_CSRF_SECRET_KEY'] = 'abc1234abc'
app.config['SECRET_KEY'] = 'abc'
# 自定义的配置扩展，表示文件上传的路径
app.config['UPLOAD_PATH'] = os.path.join(os.path.dirname(__file__), 'medias')
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
def index():
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


@app.route('/form', methods=['GET', 'POST'])
def page_form():
    """ form 表单练习 """
    form = LoginForm()
    if form.validate_on_submit():
        print('登录成功')
    else:
        print(form.errors)
    return render_template('page_form.html', form=form)


@app.route('/user/register', methods=['GET', 'POST'])
def page_register():
    """ 新用户注册 """
    # csrf_enabled为False表示不做csrf校验
    # form = RegisterForm(csrf_enabled=False)
    form = RegisterForm()
    # 用户在提交表单的时候，会触发validate_on_submit
    if form.validate_on_submit():
        # 表单验证通过，接下来处理业务逻辑
        # 1. 获取表单数据
        username = form.username.data
        password = form.password.data
        birth_date = form.birth_date.data
        age = form.age.data
        # 2. 构建用户对象
        user = User(
            username=username,
            password=password,
            birth_date=birth_date,
            age=age
        )
        # 3. 提交到数据库
        db.session.add(user)
        db.session.commit()
        print('添加成功')
        # 4. 跳转到登录页面
        return redirect(url_for('index'))
    else:
        # 打印错误信息
        print(form.errors)
    return render_template('page_register.html', form=form)


@app.route('/img/upload', methods=['GET', 'POST'])
def img_upload():
    """ 不使用wtf实现的文件上传 """
    if request.method == 'POST':
        # 获取文件列表
        files = request.files
        file1 = files.get('file1', None)
        if file1:
            # 保存文件
            f_name = secure_filename(file1.filename)
            print('filename:', f_name)
            file_name = os.path.join(app.config['UPLOAD_PATH'], f_name)
            file1.save(file_name)
            print('保存成功')
        return redirect(url_for('img_upload'))
    return render_template('img_upload.html')


@app.route('/avatar/upload', methods=['GET', 'POST'])
def avatar_upload():
    """ 头像上传 """
    form = UserAvatarForm()
    if form.validate_on_submit():
        # 获取图片对象
        img = form.avatar.data
        f_name = secure_filename(img.filename)
        file_name = os.path.join(app.config['UPLOAD_PATH'], f_name)
        img.save(file_name)
        print('保存成功')
        return redirect('/')
    else:
        print(form.errors)
    return render_template('avatar_upload.html', form=form)
