from clpconverter.converter.models import CLPPerUFModel

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import InputSerilizer
from django.http import Http404
from datetime import date

MODELS = {
    "clp_per_uf": CLPPerUFModel
}

class APIView(APIView):
    def get(self, request, *args, **kwargs):
        model = request.query_params.get("conversion")
        date_ = request.query_params.get("date", date.today())
        InputSerilizer(data=request.query_params, many=False).is_valid(raise_exception=True)
        try:
            model = MODELS[model]
        except KeyError:
            return Response({"error": "Conversion name does not match valid options"})
        try:
            return Response({"date": date_, "value": model.objects.get(date=date_).value})
        except model.DoesNotExist:
            return Response({"error": "Value for specified date does not exist"})
