from flask import Blueprint

bp = Blueprint('image_upload', __name__)

from . import routes
