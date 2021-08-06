import django_filters
from django.db.models import ExpressionWrapper
from django.db.models import F
from django.db.models import FloatField
from django.db.models import Sum
from rest_framework import generics

from .models import MetricsModel
from .serializers import MetricsSerializer


class MetricsFilter(django_filters.FilterSet):
    group_by = django_filters.CharFilter(method="group_by_filter")
    cpi = django_filters.CharFilter(method="cpi_filter")
    ordering = django_filters.OrderingFilter(
        fields=(
            "date",
            "channel",
            "country",
            "os",
            "impressions",
            "clicks",
            "installs",
            "spend",
            "revenue",
            "cpi",
        ),
    )
    date_to = django_filters.DateFilter(field_name="date", lookup_expr="lte")
    date_from = django_filters.DateFilter(field_name="date", lookup_expr="gt")
    os = django_filters.CharFilter(field_name="os")
    country = django_filters.CharFilter(field_name="country")
    date = django_filters.DateFilter(field_name="date")
    channel = django_filters.CharFilter(field_name="channel")

    class Meta:
        model = MetricsModel
        fields = []

    def group_by_filter(self, queryset, name, value):
        group_by = value.split(",")
        queryset = MetricsModel.objects.values(*group_by).annotate(
            impressions=Sum("impressions"),
            clicks=Sum("clicks"),
            installs=Sum("installs", output_field=FloatField()),
            spend=Sum("spend", output_field=FloatField()),
            revenue=Sum("revenue"),
        )
        return queryset

    def cpi_filter(self, queryset, name, value):
        if value == "true":
            queryset = queryset.annotate(
                cpi=ExpressionWrapper(
                    F("spend") / F("installs"),
                    output_field=FloatField(),
                ),
            )
        return queryset


class MetricsView(generics.ListAPIView):
    """
    Available url parameters:
        date_from - get records from the specified date. e.g 2017-06-01
        date_to - get records till the specified date. e.g 2017-05-25
        channel - filter records by chosen channels. e.g 'facebook' or several 'facebook,adcolony,...'
        country - filter records by chosen countries. e.g 'US' or several 'US,CA,...'
        os - filter records by chosen operating system. e.g 'android' or several 'android,ios,...'
        group_by - group by one ore several fields. e.g. 'date' or 'channel,country,os,...'
        ordering - group by one ore several fields. e.g. 'channel' or 'installs,-revenue,os,...' ('-' means descending)
        cpi - CPI metric (cost per install). You can include it by adding 'cpi=true'
    """

    queryset = MetricsModel.objects.all()
    serializer_class = MetricsSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    filterset_class = MetricsFilter
