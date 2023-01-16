import os
from flask import Flask, render_template, request, redirect, url_for
from functions import *
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = '/'
ALLOWED_EXTENSIONS = set(['txt'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


# перестановки
@app.route('/firsttask')
def combination_task():
    return render_template('form.html')


# @app.route("/add", methods=['POST'])
# def combination_task_2():
#     st = str(request.form['name'])
#     st = combinations(st)
#     print(st)
#     return render_template('comb.html', items=st)

@app.route("/add_comb", methods=['POST'])
def combination_task_2():
    st = list(request.form['name'])
    st = permutations(st)
    print(st)
    return render_template('comb.html', items=st)


@app.route('/CNK')
def cnk():
    return render_template('cnk_form.html')


@app.route("/add_cnk", methods=['POST'])
def cnk_ans():
    n = int(request.form['N'])
    k = int(request.form['K'])
    items = print_combination(k=n, n=k)
    return render_template('cnk_ans.html', items=items)


@app.route('/triangle')
def triangle():
    return render_template('triangle_form.html')


@app.route('/triangle_ans', methods=['POST'])
def do():
    tr = Triangle(request.form.get("count"))
    tr.generate()
    return render_template('triangle_ans.html', obj=tr)


@app.route('/colvo_slov')
def colvo_slov():
    return render_template('colvo_slov_form.html')


@app.route('/colvo_slov_ans', methods=['POST'])
def colvo_slov_ans():
    text = request.form.get("text")
    frequency = frequency_words(text)
    return render_template('colvo_slov_ans.html', items=frequency)


@app.route('/inverse')
def inverse():
    return render_template('inverse_form.html')

@app.route('/inverse_ans', methods=['POST'])
def inverse_ans():
    filename = request.form.get("filename")
    if print_rev(filename):
        return 'Успешно. Название файла = 23.txt'
    else:
        return 'Ошибка'

@app.route('/symbols')
def symbols():
    return render_template('symbols_form.html')

@app.route('/symbols_ans', methods=['POST'])
def symbols_ans():
    text = request.form.get("text")
    ans = frequency_letters(text)
    return render_template('symbols_ans.html', items = ans)


@app.route('/image_filter')
def image_filter():
    return render_template('image_filter_form.html')

@app.route('/image_filter_ans', methods=['POST'])
def image_filter_ans():
    url = request.form.get("filename")
    if remove_img_tags(url):
        return 'Успешно. Название файла = del_img.html'
    else:
        return 'Ошибка'

@app.route('/urls')
def urls():
    return render_template('urls_form.html')

@app.route('/urls_ans', methods=['POST'])
def urls_ans():
    url = request.form.get("filename")
    if change_absol(url):
        return 'Успешно. Название файла = urls_absol.html'
    else:
        return 'Ошибка'


@app.route('/tags')
def tags():
    return render_template('tags_form.html')

@app.route('/tags_ans', methods=['POST'])
def tags_ans():
    url = request.form.get("filename")
    if del_tag(url):
        return 'Успешно. Название файла = del_tag.html'
    else:
        return 'Ошибка'




if __name__ == '__main__':
    app.run()
