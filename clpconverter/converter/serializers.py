from rest_framework import serializers

class InputSerilizer(serializers.Serializer):
    date = serializers.DateField(required=False, input_formats=["%Y-%m-%d"])
    conversion = serializers.CharField(required=True)