
from django.urls import path
from main import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("api-key", views.api_key, name="api_key"),
]
