from flask import Blueprint, render_template, request, url_for, redirect

### setting up the home app
home_bp = Blueprint('home', __name__)

### main home route
@home_bp.route('/')
def home() : 

    return render_template('home.html')