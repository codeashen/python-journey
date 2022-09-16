### 启动方式

1. 设置环境变量

   Windows: `set FLASK_APP=app.py`

   Linux: `export FLASK_APP=app.py`

2. flask run 启动内置 web 服务器

   指定 IP 及端口：`flask run --host=0.0.0.0 --port=8001`

   或：`flask run -h 0.0.0.0 -p 8001`

### 开启调试模式

开启调试模式后，修改代码不需要重启即可热加载。

1. 设置环境变量

   Windows: `set FLASK_ENV=development`

   Linux: `export FLASK_ENV=development`

2. flask run 启动 web 服务器

> 注意：生产模式不要开启调试模式
