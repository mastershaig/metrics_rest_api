from collections import OrderedDict

from rest_framework import serializers

from .models import MetricsModel


class MetricsSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField(required=False, allow_null=True)
    channel = serializers.SerializerMethodField(required=False, allow_null=True)
    country = serializers.SerializerMethodField(required=False, allow_null=True)
    os = serializers.SerializerMethodField(required=False, allow_null=True)
    cpi = serializers.FloatField(required=False)

    class Meta:
        model = MetricsModel
        fields = [
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
        ]

    @staticmethod
    def _get_from_model(obj, field):
        return (
            getattr(obj, field)
            if hasattr(obj, field)
            else obj.get(field)
            if isinstance(obj, dict)
            else None
        )

    def get_date(self, obj):
        return self._get_from_model(obj, "date")

    def get_channel(self, obj):
        return self._get_from_model(obj, "channel")

    def get_country(self, obj):
        return self._get_from_model(obj, "country")

    def get_os(self, obj):
        return self._get_from_model(obj, "os")

    def to_representation(self, instance):
        result = super(MetricsSerializer, self).to_representation(instance)
        return OrderedDict(
            [(key, result[key]) for key in result if result[key] is not None],
        )
