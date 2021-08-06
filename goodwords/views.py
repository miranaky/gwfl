from datetime import datetime
from calendar import monthrange
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import GoodWord
from calendars import models as calendar_models
from .serializers import GoodWordsSerializer


class OwnPagination(PageNumberPagination):
    page_size = 7


def get_dates(year, month):
    num_days = monthrange(year, month)[1]
    try:
        first_day = calendar_models.Calendar.objects.get(date=f"{year}-{month}-01")
        last_day = calendar_models.Calendar.objects.get(date=f"{year}-{month}-{num_days}")
    except calendar_models.Calendar.DoesNotExist:
        return {"date__gte": None, "date__lte": None}
    return {"date__gte": first_day, "date__lte": last_day}


@api_view(["GET"])
def goodwords_view(request):
    year = request.GET.get("year", None)
    month = request.GET.get("month", None)
    filter_kwargs = {}
    if year is not None and month is not None:
        filter_kwargs = get_dates(int(year), int(month))
    else:
        today = datetime.today()
        filter_kwargs = get_dates(today.year, today.month)
    paginator = OwnPagination()
    try:
        goodwords = GoodWord.objects.filter(**filter_kwargs)
    except ValueError:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    results = paginator.paginate_queryset(goodwords, request)
    serializer = GoodWordsSerializer(results, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(["GET"])
def goodword_view(request, date):
    try:
        _date = calendar_models.Calendar.objects.get(date=date)
        goodword = GoodWord.objects.get(date=_date)
    except GoodWord.DoesNotExist or calendar_models.Calendar.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = GoodWordsSerializer(goodword).data
    return Response(serializer)
