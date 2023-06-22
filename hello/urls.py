from django.urls import path
from hello import views

urlpatterns = [
    path("", views.append_to_file, name="home"),
]
