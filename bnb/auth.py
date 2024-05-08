# https://flask.palletsprojects.com/en/3.0.x/tutorial/views/ [REFER HERE]

import functools

from werkzeug.security import check_password_hash, generate_password_hash
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from bnb.db import get_db


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


bp = Blueprint('auth', __name__, url_prefix='/auth')

# @bp.route('/logout')
# @bp.route('/login')
# @bp.route('/signUp')
