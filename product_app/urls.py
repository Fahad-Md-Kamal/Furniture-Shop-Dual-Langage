from django.urls import path
from product_app import views

app_name = 'products'

urlpatterns = [
    path('', views.home, name='home' ),
    path('carousal', views.carousal_form, name="carousal-form"),
    path('list', views.product_list, name="list")
]