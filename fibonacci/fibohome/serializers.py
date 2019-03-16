from rest_framework import serializers


class HomeViewSerializer(serializers.Serializer):
    result= serializers.IntegerField()
    end_time = serializers.FloatField()

