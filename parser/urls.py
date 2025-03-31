from django.urls import path
from .views import index, run_parser

urlpatterns = [
    path("", index, name="index"),
    path("run_parser/", run_parser, name="run_parser"),
]
