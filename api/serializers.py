from rest_framework import serializers
from .models import Meal , Rating

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id','title','description','average_rate','No_rates']
    
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id','stars','meal','user']