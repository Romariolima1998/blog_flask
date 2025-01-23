from flask import Blueprint

post = Blueprint('post', __name__, static_folder='/static')

from app.posts import views