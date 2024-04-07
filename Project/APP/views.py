from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Expense
from .models import Toggle
from .serializers import ExpenseSerializer
from .serializers import ToggleSerializer

#Views of Expense Model
class ListExpenseAPIView(ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class CreateExpenseAPIView(CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class UpdateExpenseAPIView(UpdateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class DeleteExpenseAPIView(DestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

#Views of Toggle model
class ListToggleAPIView(ListAPIView):
    queryset = Toggle.objects.all()
    serializer_class = ToggleSerializer

class CreateToggleAPIView(CreateAPIView):
    queryset = Toggle.objects.all()
    serializer_class = ToggleSerializer

class UpdateToggleAPIView(UpdateAPIView):
    queryset = Toggle.objects.all()
    serializer_class = ToggleSerializer

class DeleteToggleAPIView(DestroyAPIView):
    queryset = Toggle.objects.all()
    serializer_class = ToggleSerializer