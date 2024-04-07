from django.urls import path
from .views import ListExpenseAPIView, CreateExpenseAPIView, UpdateExpenseAPIView, DeleteExpenseAPIView
from .views import ListToggleAPIView, CreateToggleAPIView, UpdateToggleAPIView, DeleteToggleAPIView


#URLs of Expense model
urlpatterns = [
    path('expense/', ListExpenseAPIView.as_view(), name='expense-list'),
    path('expense/create/', CreateExpenseAPIView.as_view(), name='expense-create'),
    path('expense/<int:pk>/', UpdateExpenseAPIView.as_view(), name='expense-update'),
    path('expense/<int:pk>/delete/', DeleteExpenseAPIView.as_view(), name='expense-delete'),
    path('toggle/', ListToggleAPIView.as_view(), name='toggle-list'),
    path('toggle/create/', CreateToggleAPIView.as_view(), name='toggle-create'),
    path('toggle/<int:pk>/', UpdateToggleAPIView.as_view(), name='Toggle-update'),
    path('toggle/<int:pk>/delete/', DeleteToggleAPIView.as_view(), name='toggle-delete'),
]
