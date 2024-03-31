from django.urls import path

from api import views


urlpatterns = [
    path("create-letter/", views.create_letter, name="create_letter"),
    path("read-letter/", views.read_letter, name="read_letter"),
]
