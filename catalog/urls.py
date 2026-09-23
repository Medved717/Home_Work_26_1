from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('contacts/', views.ContactsTemplateView.as_view(), name ='contact'),
    path('product_list/', views.ProductListView.as_view(), name ='product_list'),
    path('product_detail/<int:pk>', views.ProductDetailView.as_view(), name ='product_detail'),
    path('product_form/', views.ProductCreateView.as_view(), name ='product_create'),
]
