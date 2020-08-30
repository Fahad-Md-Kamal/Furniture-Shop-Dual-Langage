from django.urls import path
from product_app import views

app_name = 'products'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home' ),
    path('list/', views.ProductListView.as_view(), name="list"),
    path('detail/<int:pk>/', views.ProductDetailView.as_view(), name="detail"),
    path('create/', views.ProductCreateView.as_view(), name="create"),
    path('Update/<int:pk>/', views.ProductUpdateView.as_view(), name="update"),
    path('search/<int:cat>/', views.searchProduct, name="search"),
]