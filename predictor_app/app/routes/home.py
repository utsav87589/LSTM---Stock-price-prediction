from flask import Blueprint, render_template, request, url_for, redirect

### setting up the home app
home_bp = Blueprint('home', __name__)

### main home route
@home_bp.route('/', methods = ['GET', 'POST'])
def home() : 

    if request.method == 'POST' : 
        ticker = request.form.get('ticker')

        print(f"ticker entered : {ticker}")

        return redirect(url_for('predictions.predictions', ticker = ticker))


    return render_template('home.html')