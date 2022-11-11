from flask import Blueprint, render_template, request, send_from_directory
from DZ_12.lesson12_project_source_v3 import functions

loader_blueprint = Blueprint('loader_blueprint', __name__)


@loader_blueprint.route('/loads')
def load_page():
    return render_template('post_form.html')


@loader_blueprint.route('/loads', methods=['POST'])
def add_post_page():
    img = request.files.get('picture')
    content = request.form.get('content')

    if not img or not content:
        return 'Не выбрана картинка или не введен текст'

    saves_img: str = save_img(img)

    post: dict = save_post({'pic': saves_img, 'content': content})
    return render_template('post_uploaded.html', post=post)


@loader_blueprint.route('/uploads/<path:path>')
def static_dir(path):
    return send_from_directory('uploads', path)


