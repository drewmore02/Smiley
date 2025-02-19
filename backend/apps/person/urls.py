from django.urls import path
from .views import PersonListView

app_name = 'person'

urlpatterns = [
    path('', PersonListView.as_view(), name='list'),
]