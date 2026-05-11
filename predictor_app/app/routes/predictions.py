from flask import Blueprint, render_template, request, url_for, redirect
from ..logic.data_fetcher import get_plot_data

predictions_bp = Blueprint('predictions', __name__)

### defining the predictions route
@predictions_bp.route('/predictions/<ticker>')
def predictions(ticker) : 

    graphs = get_plot_data(ticker)

    return render_template(
        '/predictions.html',
        ticker = ticker,
        graphs = graphs
        )