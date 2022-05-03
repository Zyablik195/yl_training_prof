from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='')

@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof or 'строитель' in prof:
        word = 'Инженерные тренажеры'
        path = '/static/images/2.png'
    else:
        word = 'Научные симуляторы'
        path = '/static/images/1.png'
    return render_template('training.html', path=path, word=word, title='')

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')