import yfinance as yf
import plotly.express as px
import json

def get_plot_data(ticker) : 

    df = yf.download(ticker, start = '2020-05-08', end = '2026-05-09')

    fig = px.line(df, x = df.index, y = df[('Close', ticker).values])

    graph_JSON = json.dumps(fig, cls = plotly.utils.PlotlyJSONEncoder)

    return graph_JSON