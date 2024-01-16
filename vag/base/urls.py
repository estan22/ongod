from django.urls import path
from . import views

app_name = "base"
urlpatterns = [
    path("", views.king, name="king"),
    path("map_lit/", views.get_mail_access, name="mailAccess"),
    path("bop_ad/", views.bop_ad, name="bop_ad"),
    path("cot_in/", views.cot_in, name="cot_in"),
]