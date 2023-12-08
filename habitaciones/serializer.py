from rest_framework import serializers
from .models import Hab

class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hab
        fields="__all__"