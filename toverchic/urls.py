
from django.contrib import admin
from django.urls import path
from views import Productdetail, createComment, Products

urlpatterns = [
    path(r'^tovachic', Products.as_view(), name='home'),
    path(r'/product-detail/<int:pk>', Productdetail.as_view(), name='product-detail')
    
]
