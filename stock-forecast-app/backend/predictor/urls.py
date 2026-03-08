from django.urls import path
from .views import predict_stocks

url_pattern = [path("predict/", predict_stock)]
