from flask import Blueprint

bp = Blueprint('auth', __name__)

from . import email
from . import routes
from . import forms
