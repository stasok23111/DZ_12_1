from flask import Blueprint, render_template,request, send_from_directory
from functions import *

main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.route('/')
def main_page():

    return render_template('index.html')

@main_blueprint.route('/search/')
def search_page():
    search_word = request.args.get('s', '')
    try:
        posts = get_search_word(search_word)
    except FileNotFoundError:
        return 'Нет такого файла'
    return render_template('post_list.html',word=search_word, posts=posts)


@main_blueprint.route('/uploads/<path:path>')
def static_dir(path):
    return send_from_directory('uploads',path)

