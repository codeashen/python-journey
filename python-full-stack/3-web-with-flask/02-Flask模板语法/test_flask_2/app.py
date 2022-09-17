from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """  首页 """
    return render_template('index.html')


@app.route('/course')
def course():
    """  免费课程 """
    return render_template('course.html')


@app.route('/coding')
def coding():
    """  实战课程 """
    return render_template('coding.html')


@app.route('/article')
def article():
    """  手记 """
    return render_template('article.html')


@app.route('/wenda')
def wenda():
    """  问答 """
    question = 'why?'
    return render_template('wenda.html', question=question)
