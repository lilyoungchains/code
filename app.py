from flask import Flask, render_template
from random import randint
app = Flask(__name__)

hero = [
    '一',
    '二',
    '三',
    '四',
    '五',
    '六',
    '七',
    '八',
    '九'

]


@app.route('/index')
def index():
    return render_template('index.html', hero=hero)


@app.route('/choujiang')
def choujiang():
    num = randint(0, len(hero)-1)
    return render_template('index.html', hero=hero, h=hero[num])


app.run(debug=True)
