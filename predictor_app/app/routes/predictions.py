from flask import Blueprint, render_template, request, url_for, redirect

predictions_bp = Blueprint('predictions', __name__)

### defining the predictions route
@predictions_bp.route('/predictions')
def predictions() : 

    return render_template('/predictions.html')