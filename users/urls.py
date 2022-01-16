from django.urls import path
from .views import indexPage, prem
urlpatterns = [
    path("", indexPage, name="starting page"),
    path("prem/",prem, name="prem")
]