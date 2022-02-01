from django.urls import path

from . import views

app_name = 'customers'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('customer/', views.CustomerView.as_view(), name='customer'),
	path('customer/add_customer/', views.add_customer, name='add_customer'),
	path('<int:customer_id>/delete_customer/', views.delete_customer, name='delete_customer'),
]
