# https://flask.palletsprojects.com/en/3.0.x/tutorial/blog/ [REFER HERE]

from werkzeug.exceptions import abort
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from bnb.auth import login_required
from bnb.db import get_db

bp = Blueprint('recommend', __name__)

@bp.route('/recommend')
def recommend_popular():
    print("Popular books here")

