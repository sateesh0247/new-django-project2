from rest_framework import serializers
from .models import square


class SquareSerializer(serializers.modelserializers):
    class Meta:
        model =Square
        fields = '_all_'
        
