from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

    path('sales/', views.SaleView.as_view(), name='sales-list'),
    path('sales/new', views.SaleCreateView.as_view(), name='new-sale'),
    path('sales/<pk>/delete', views.SaleDeleteView.as_view(), name='delete-sale'),
    path("sales/<billno>", views.SaleBillView.as_view(), name="sale-bill"),
]