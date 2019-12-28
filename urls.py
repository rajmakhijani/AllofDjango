from django.urls import path
from .views import add,thanks

urlpatterns = [
    path('<int:id>/', thanks, name='thanks'),
    path('add/', add, name='add'),
]