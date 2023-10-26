from flask import Blueprint, render_template, redirect, url_for, request, flash, Flask
from flask_login import login_required, current_user    
from .models import User
from . import db
import os

fvt= Blueprint('favorites', __name__)


@fvt.route('/favorites')
@login_required
def favorites():
    user = User.query.filter_by(id=current_user.id).first()
    return render_template('favorites.html')


