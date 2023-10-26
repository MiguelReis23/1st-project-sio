from flask import Blueprint, render_template
from flask_login import login_user, logout_user, login_required, current_user

main = Blueprint('main', __name__)


@main.route('/')
@login_required
def index():
    return render_template('index.html')
