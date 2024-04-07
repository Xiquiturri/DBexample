from rest_framework import serializers
from .models import Expense
from .models import Toggle

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class ToggleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toggle
        fields = '__all__'