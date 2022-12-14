from flask import Flask, render_template, request, send_from_directory
# from functions import ...

from main.main import main_blueprint
from loader.loader import loader_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)




app.run()
