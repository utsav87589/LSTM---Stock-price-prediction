import yfinance as yf
import plotly.express as px
import json
import plotly
from datetime import date, timedelta


today = date.today()
end_date = today + timedelta(days = 1)
start_date = today - timedelta(days = (365 * 6))


def get_plot_data(ticker) : 

    df = yf.download(ticker, start = start_date, end = end_date, multi_level_index = False)
    df = df.drop('Volume', axis = 1)

    all_graphs = {}

    for feature in df.columns : 

        fig = px.line(df, x = df.index, y = df[feature])
        fig.update_layout(template="plotly_dark")

        all_graphs[feature] = json.dumps(fig, cls = plotly.utils.PlotlyJSONEncoder)

    return all_graphs