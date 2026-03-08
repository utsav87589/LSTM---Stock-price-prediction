from django.http import JsonResponse
import json


def predict_stock(request):

    if request.method == "POST":

        body = json.loads(request.body)
        ticker = body.get("ticker")

        return JsonResponse({"message": f"Received request for {ticker}"})

    return JsonResponse({"error": "Invalid request"})
