from flask import Flask, current_app, request, make_response, \
    render_template, abort

app = Flask(__name__)


@app.route('/index')
def index():
    print(app)
    print(current_app)
    print(app == current_app)
    print(app is current_app)
    return 'index'


@app.route('/')
def hello_world():
    """ 视图函数 """
    # 访问/时重定向到/index这个页面
    # return redirect('/index')
    # ip拦截
    ip_list = ['127.0.0.2']
    ip = request.remote_addr
    if ip in ip_list:
        abort(403)
    return 'hello, success'


@app.route('/user/')
@app.route('/user/<page>')
def list_user(page=1):
    return '您好，你是第{}页用户'.format(page)


@app.route('/test/req')
def test_request():
    """ 请求报文练习 """
    get_args = request.args
    print(get_args)
    # 页码一定是正整数
    page = request.args.get('page', 1)
    print(page)
    # 服务器所在的主机地址
    headers = request.headers
    print(headers)
    print(headers.get('host'))
    # 获取ip地址
    ip = request.remote_addr
    print('远程IP地址')
    print(ip)

    # 获取User-agent
    user_agent = request.headers.get('user-agent', None)
    print('User-Agent：')
    print(user_agent)

    return 'request success'


@app.before_first_request
def first_request():
    """ 服务器启动后第一个请求到达 """
    print('first_request')


@app.before_request
def per_request():
    """ 每一个请求到达前 """
    print('before request')


@app.route('/test/resp')
def test_response():
    """ 测试响应 """
    # return 'response success', 401, {
    #     'user_id': 'my_user_id'
    # }

    # 构造一个响应对象
    # resp = make_response('这是一个响应对象', 403, {
    #     'token': 'abc123'
    # })
    # resp.headers['user_id'] = 'myid_123'
    # resp.status_code = 200

    # 响应html
    html = "<html><body><h1 style='color:#f00'>HTML文本显示</h1></body></html>"
    resp = make_response(html)
    return resp


@app.route('/test/html')
def test_html():
    """ 从文件中响应html """
    html = render_template('index.html')
    resp = make_response(html, 400)
    return resp


@app.errorhandler(403)
def forbidden_page(err):
    """ 你没有权限访问的页面 """
    print(err)
    return '您没有权限访问，请联系管理员开通权限'


# 使用api添加路由配置，不使用注解
app.add_url_rule('/home', 'home', hello_world)
# 打印所有路由配置
print(app.url_map)

# v1.0之后的版本，不推荐的写法
# if __name__ == '__main__':
#    app.run()
