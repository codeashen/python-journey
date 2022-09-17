from flask import Flask, render_template, flash, redirect, request

app = Flask(__name__)
# session的安全机制，使用flash时需要设置该随机串
app.secret_key = 'secret_keyabcdes334'


# 用户登录之后，跳转到个人中心，在个人中心页面，展示一个提示：登录成功


@app.route('/login', methods=['GET', 'POST'])
def login():
    """  用户登录 """
    if request.method == 'POST':
        print('处理了登录的逻辑')
        flash('登录成功', 'success')
        flash('欢迎回来', 'success')
        flash('错误提示', 'error')
        return redirect('/mine')
    return render_template('login.html')


@app.route('/mine')
def mine():
    """  个人中心 """
    return render_template('mine.html')
